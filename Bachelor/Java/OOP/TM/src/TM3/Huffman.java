package TM3;

import java.util.HashMap;
import java.util.Map;

/**
 * Classe principale du codage de Huffman : compresse du texte en utilisant des codes binaires.
 * 
 * QU'EST-CE QUE LE CODAGE DE HUFFMAN ? (expliqué comme si vous aviez 5 ans)
 * 
 * Imaginez que vous envoyez un message secret avec des lumières qui clignotent :
 * - Chaque lettre est représentée par une série de clignotements (0 = éteint, 1 = allumé)
 * - Les lettres qu'on utilise SOUVENT ont des codes COURTS (peu de clignotements)
 * - Les lettres qu'on utilise RAREMENT ont des codes LONGS (beaucoup de clignotements)
 * 
 * Exemple avec le texte "aaabbc" :
 * - 'a' apparaît 3 fois (très fréquent) → code court : "0"
 * - 'b' apparaît 2 fois (moyen) → code moyen : "10"
 * - 'c' apparaît 1 fois (rare) → code long : "11"
 * 
 * Le texte "aaabbc" devient : "0" + "0" + "0" + "10" + "10" + "11" = "00010011"
 * (8 bits au lieu de 48 bits si on utilisait 8 bits par caractère !)
 * 
 * COMMENT ÇA MARCHE ?
 * 
 * 1. CONSTRUIRE L'ARBRE (initArbre) :
 *    On crée un arbre binaire spécial où :
 *    - Chaque feuille = un caractère
 *    - Le chemin vers une feuille = le code du caractère
 *    - Gauche = '0', Droite = '1'
 * 
 * 2. CRÉER LE DICTIONNAIRE (initDictionnaire) :
 *    On parcourt l'arbre pour créer un "livre de codes" :
 *    Caractère → Code binaire (ex: 'a' → "0", 'b' → "10")
 * 
 * 3. CODER (code) :
 *    On remplace chaque caractère par son code du dictionnaire
 * 
 * 4. DÉCODER (decode) :
 *    On parcourt l'arbre en suivant les bits jusqu'à trouver un caractère
 */
public class Huffman {

	// Le dictionnaire : associe chaque caractère à son code binaire
	// Exemple : {'a' → "0", 'b' → "10", 'c' → "11"}
	private Map<Character, String> dictionnaire;
	
	// L'arbre de Huffman : structure qui permet de décoder le texte
	private NoeudAbstrait arbre;
	
	/**
	 * Constructeur : crée un système de codage de Huffman pour un texte donné.
	 * 
	 * ÉTAPES :
	 * 1. On compte combien de fois chaque caractère apparaît dans le texte
	 * 2. On construit l'arbre de Huffman avec ces comptes
	 * 3. On crée le dictionnaire en parcourant l'arbre
	 * 
	 * @param texte le texte de référence pour créer le codage
	 */
	public Huffman(String texte) {
		initArbre(compteCaracteres(texte));  // Étapes 1 et 2
		initDictionnaire();                   // Étape 3
	}

	private Map<Character, Integer> compteCaracteres(String texte) {
		Map<Character, Integer> comptes = new HashMap<>();
		for (int i = 0; i < texte.length(); i++) {
			Character caractere = texte.charAt(i);
			// Récupère le compte actuel pour ce caractère. 
			// Si le caractère n'est pas encore dans la Map, get(caractere) retourne null.
			Integer count = comptes.get(caractere);

			if (count == null) {
				// Première occurrence : initialise le compte à 1
				comptes.put(caractere, 1);
			} else {
				// Occurrence suivante : incrémente le compte
				comptes.put(caractere, count + 1);
			}
		}

		return comptes;
	}
	  private void initArbre(Map<Character, Integer> comptes) {
	        // Cas texte vide ou null : pas d'arbre
	        if (comptes == null || comptes.isEmpty()) {
	            this.arbre = null;
	            return;
	        }

	        // 1 & 2 : créer une liste triée contenant une feuille par caractère
	        ListeTriee liste = new ListeTriee();
	        for (Map.Entry<Character, Integer> e : comptes.entrySet()) {
	            Character c = e.getKey();
	            int poids = e.getValue();
	            liste.add(new Feuille(c, poids));
	        }

	        // 3 : fusionner jusqu'à ce qu'il ne reste qu'un nœud
	        while (liste.size() >= 2) {
	            // 2 plus petits éléments (liste triée)
	            NoeudAbstrait n1 = liste.removeFirst();
	            NoeudAbstrait n2 = liste.removeFirst();

	            // nouveau nœud interne avec somme des poids
	            Noeud parent = new Noeud(n1.getPoids() + n2.getPoids(), n1, n2);

	            // on le réinsère dans la liste triée
	            liste.add(parent);
	        }

	        // 4 : le dernier élément restant est la racine de l'arbre de Huffman
	        this.arbre = liste.removeFirst();
	    }

	  private void initDictionnaire() {
	        dictionnaire = new HashMap<>();
	        if (arbre != null) {
	            arbre.fournitCodes(dictionnaire, "");
	        }
	    }
	  
	  
	  /**
	   * CODE (crypte) un texte en utilisant le codage de Huffman.
	   * 
	   * COMMENT ÇA MARCHE ? (expliqué simplement)
	   * 
	   * C'est comme remplacer chaque lettre par un code secret !
	   * On regarde chaque lettre du texte, on cherche son code dans le dictionnaire,
	   * et on met tous les codes bout à bout.
	   * 
	   * EXEMPLE :
	   * 
	   * Texte à coder : "abc"
	   * Dictionnaire : 'a' → "0", 'b' → "10", 'c' → "11"
	   * 
	   * Étape par étape :
	   * 1. On regarde 'a' → code = "0"
	   * 2. On regarde 'b' → code = "10"
	   * 3. On regarde 'c' → code = "11"
	   * 4. On colle tout : "0" + "10" + "11" = "01011"
	   * 
	   * Résultat : "abc" devient "01011"
	   * 
	   * ATTENTION : On ne peut coder que des caractères qui étaient dans le texte de référence !
	   * Si on essaie de coder un caractère nouveau, ça lance une erreur.
	   * 
	   * @param texte le texte en clair à coder
	   * @return une chaîne de '0' et '1' (le texte codé)
	   * @throws CaractereInconnuException si un caractère n'est pas dans le dictionnaire
	   */
	  public String code(String texte) throws CaractereInconnuException {
		    // Si le texte est vide, on retourne une chaîne vide
		    if (texte == null || texte.isEmpty()) {
		        return "";
		    }

		    // Vérification : on doit avoir un dictionnaire !
		    if (dictionnaire == null || dictionnaire.isEmpty()) {
		        throw new CaractereInconnuException("Aucun dictionnaire Huffman disponible.");
		    }

		    // StringBuilder = un "cahier" où on écrit le résultat petit à petit
		    // C'est plus rapide que de faire "résultat = résultat + code"
		    StringBuilder sb = new StringBuilder();

		    // On parcourt chaque caractère du texte
		    for (int i = 0; i < texte.length(); i++) {
		        char c = texte.charAt(i);  // On prend le caractère à la position i
		        
		        // On cherche le code de ce caractère dans le dictionnaire
		        String code = dictionnaire.get(c);
		        
		        // Si le code est null, c'est que le caractère n'existe pas dans le dictionnaire
		        if (code == null) {
		            // On lance une alarme (exception) pour dire qu'on ne peut pas coder ce caractère
		            throw new CaractereInconnuException(
		                "Caractère inconnu dans le codage de Huffman : '" + c + "'"
		            );
		        }
		        
		        // On ajoute le code au résultat
		        sb.append(code);
		    }

		    // On transforme le StringBuilder en String et on le retourne
		    return sb.toString();
		}
	  
	  
	  
	  public String decode(String binaire) throws FinDeTexteInattendueException {
		    if (binaire == null || binaire.isEmpty()) {
		        return "";
		    }
		    if (arbre == null) {
		        throw new FinDeTexteInattendueException("Aucun arbre de Huffman disponible.");
		    }

		    StringBuilder out = new StringBuilder();

		    // Cas particulier : arbre réduit à une seule feuille (un seul caractère possible)
		    if (arbre instanceof Feuille) {
		        char unique = ((Feuille) arbre).getCaractere();
		        for (int i = 0; i < binaire.length(); i++) {
		            char bit = binaire.charAt(i);
		            // dans ce cas simple, on n'accepte que des '0' (code attribué à ce caractère)
		            if (bit != '0') {
		                throw new FinDeTexteInattendueException(
		                    "Bit invalide pour un alphabet à un seul caractère : " + bit
		                );
		            }
		            out.append(unique);
		        }
		        return out.toString();
		    }

		    // Cas général : arbre avec au moins un nœud interne
		    NoeudAbstrait courant = arbre;

		    for (int i = 0; i < binaire.length(); i++) {
		        char bit = binaire.charAt(i);

		        if (!(courant instanceof Noeud)) {
		            // on ne devrait jamais se retrouver sur une feuille ici sans avoir
		            // déjà consommé le bit précédent et réinitialisé à la racine
		            throw new FinDeTexteInattendueException(
		                "Structure d'arbre incohérente pendant le décodage."
		            );
		        }

		        Noeud n = (Noeud) courant;
		        if (bit == '0') {
		            courant = n.getGauche();
		        } else if (bit == '1') {
		            courant = n.getDroit();
		        } else {
		            throw new FinDeTexteInattendueException(
		                "Caractère non binaire dans le texte codé : " + bit
		            );
		        }

		        // Si on arrive sur une feuille, on a trouvé un caractère
		        if (courant instanceof Feuille) {
		            Feuille f = (Feuille) courant;
		            out.append(f.getCaractere());
		            // On repart de la racine pour décoder le caractère suivant
		            courant = arbre;
		        }
		    }

		    // Si on a fini les bits mais qu'on n'est pas revenu à la racine,
		    // cela veut dire que le dernier code est incomplet
		    if (courant != arbre) {
		        throw new FinDeTexteInattendueException(
		            "Fin du texte codé au milieu d'un code de caractère."
		        );
		    }

		    return out.toString();
		}
	  
	  // Added getters required by GUI and DessinHuffman
	  public NoeudAbstrait getArbre() {
	      return arbre;
	  }
	  
	  public Map<Character, String> getDictionnaire() {
	      return dictionnaire;
	  }
	  
	  
}