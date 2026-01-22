package TM3bis;

import java.util.HashMap;
import java.util.Map;

public class Huffman {

    private Map<Character, String> dictionnaire;
    private NoeudAbstrait arbre;
    
    public Huffman(String texte) {
        initArbre(compteCaracteres(texte));
        initDictionnaire();
    }

    public Huffman(Map<Character, Integer> comptes) {
        initArbre(comptes);
        initDictionnaire();
    }

    private Map<Character, Integer> compteCaracteres(String texte) {
        Map<Character, Integer> comptes = new HashMap<>();
        for (int i = 0; i < texte.length(); i++) {
            Character caractere = texte.charAt(i);
            Integer count = comptes.get(caractere);
            if (count == null) {
                comptes.put(caractere, 1);
            } else {
                comptes.put(caractere, count + 1);
            }
        }
        return comptes;
    }

    private void initArbre(Map<Character, Integer> comptes) {
        if (comptes == null || comptes.isEmpty()) {
            this.arbre = null;
            return;
        }
        ListeTriee liste = new ListeTriee();
        for (Map.Entry<Character, Integer> e : comptes.entrySet()) {
            Character c = e.getKey();
            int poids = e.getValue();
            if (poids > 0) {
                liste.add(new Feuille(c, poids));
            }
        }
        
        if (liste.isEmpty()) {
            this.arbre = null;
            return;
        }

        while (liste.size() >= 2) {
            NoeudAbstrait n1 = liste.removeFirst();
            NoeudAbstrait n2 = liste.removeFirst();
            Noeud parent = new Noeud(n1.getPoids() + n2.getPoids(), n1, n2);
            liste.add(parent);
        }
        this.arbre = liste.removeFirst();
    }

    private void initDictionnaire() {
        dictionnaire = new HashMap<>();
        if (arbre != null) {
            arbre.fournitCodes(dictionnaire, "");
        }
    }
    
    public Huffman difference(Huffman h) {
        if (this.arbre == null || h.getArbre() == null) {
             throw new RuntimeException("Impossible de faire la différence : un des arbres est vide.");
        }

        Map<Character, Integer> poids1 = new HashMap<>();
        this.arbre.fournitPoids(poids1);

        Map<Character, Integer> poids2 = new HashMap<>();
        h.getArbre().fournitPoids(poids2);

        Map<Character, Integer> nouveauxPoids = new HashMap<>();

        for (Map.Entry<Character, Integer> entry : poids1.entrySet()) {
            Character c = entry.getKey();
            int p1 = entry.getValue();

            if (!poids2.containsKey(c)) {
                nouveauxPoids.put(c, p1);
            } else {
                int p2 = poids2.get(c);
                int diff = p1 - p2;

                if (diff < 0) {
                    throw new RuntimeException("Poids négatif détecté pour '" + c + "' lors de la différence.");
                } else if (diff > 0) {
                    nouveauxPoids.put(c, diff);
                }
            }
        }

        return new Huffman(nouveauxPoids);
    }

    public String code(String texte) throws CaractereInconnuException {
        if (texte == null || texte.isEmpty()) return "";
        if (dictionnaire == null || dictionnaire.isEmpty()) throw new CaractereInconnuException("Aucun dictionnaire Huffman disponible.");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < texte.length(); i++) {
            char c = texte.charAt(i);
            String code = dictionnaire.get(c);
            if (code == null) throw new CaractereInconnuException("Caractère inconnu : '" + c + "'");
            sb.append(code);
        }
        return sb.toString();
    }
      
    public String decode(String binaire) throws FinDeTexteInattendueException {
        if (binaire == null || binaire.isEmpty()) return "";
        if (arbre == null) throw new FinDeTexteInattendueException("Aucun arbre de Huffman disponible.");
        StringBuilder out = new StringBuilder();
        if (arbre instanceof Feuille) {
            char unique = ((Feuille) arbre).getCaractere();
            for (int i = 0; i < binaire.length(); i++) {
                if (binaire.charAt(i) != '0') throw new FinDeTexteInattendueException("Bit invalide.");
                out.append(unique);
            }
            return out.toString();
        }
        NoeudAbstrait courant = arbre;
        for (int i = 0; i < binaire.length(); i++) {
            char bit = binaire.charAt(i);
            Noeud n = (Noeud) courant;
            if (bit == '0') courant = n.getGauche();
            else if (bit == '1') courant = n.getDroit();
            else throw new FinDeTexteInattendueException("Caractère non binaire.");

            if (courant instanceof Feuille) {
                out.append(((Feuille) courant).getCaractere());
                courant = arbre;
            }
        }
        if (courant != arbre) throw new FinDeTexteInattendueException("Fin du texte inattendue.");
        return out.toString();
    }
      
    public NoeudAbstrait getArbre() { return arbre; }
    public Map<Character, String> getDictionnaire() { return dictionnaire; }
}