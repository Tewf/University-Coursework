package TM3;



import java.util.Map;

public class Noeud extends NoeudAbstrait {
    private final NoeudAbstrait gauche;
    private final NoeudAbstrait droit;

    public Noeud(int poids, NoeudAbstrait gauche, NoeudAbstrait droit) {
        super(poids);
        this.gauche = gauche;
        this.droit = droit;
    }

    /** Requis par DessinHuffman. */
    public NoeudAbstrait getGauche() { return gauche; }
    public NoeudAbstrait getDroit()  { return droit;  }

    @Override
    public void fournitCodes(Map<Character, String> m, String prefixe) {
        gauche.fournitCodes(m, prefixe + "0");
        droit.fournitCodes(m,  prefixe + "1");
    }

    @Override
    public Character getNextChar(String s) throws FinDeTexteInattendueException {
        if (s == null || s.isEmpty()) {
            throw new FinDeTexteInattendueException(
                "Texte codé terminé avant d’atteindre une feuille."
            );
        }
        char bit = s.charAt(0);
        if (bit == '0') {
            return gauche.getNextChar(s.substring(1));
        } else if (bit == '1') {
            return droit.getNextChar(s.substring(1));
        } else {
            throw new FinDeTexteInattendueException("Caractère non binaire rencontré: " + bit);
        }
    }

    @Override
    public int hauteur() {
        return 1 + Math.max(gauche.hauteur(), droit.hauteur());
    }
}