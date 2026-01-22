package TM3;



import java.util.Map;

public abstract class NoeudAbstrait implements Comparable<NoeudAbstrait> {
    private final int poids;

    public NoeudAbstrait(int poids) {
        this.poids = poids;
    }

    public NoeudAbstrait() {
        this(0);
    }

    public int getPoids() {
        return poids;
    }

    @Override
    public int compareTo(NoeudAbstrait n) {
        return Integer.compare(this.poids, n.poids);
    }

    /** Ajoute (caractère -> code) pour tout le sous-arbre, avec préfixe donné. */
    public abstract void fournitCodes(Map<Character, String> m, String prefixe);

    /**
     * Parcourt en suivant les 1ers bits de s depuis ce noeud jusqu'à une Feuille
     * et retourne son caractère. Si on ne tombe pas sur une feuille, lève l’exception.
     */
    public abstract Character getNextChar(String s) throws FinDeTexteInattendueException;

    /** Hauteur (en arêtes) du sous-arbre. Une feuille a hauteur 0. */
    public abstract int hauteur();
}
