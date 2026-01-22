package TM3bis;

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

    public abstract void fournitCodes(Map<Character, String> m, String prefixe);

    public abstract Character getNextChar(String s) throws FinDeTexteInattendueException;

    public abstract int hauteur();

    public abstract void fournitPoids(Map<Character, Integer> m);
}