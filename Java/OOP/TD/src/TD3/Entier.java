package TD3;

public class Entier extends TermeAtomique {
    private long valeur;

    public Entier(long valeur) { this.valeur = valeur; }

    public long getValeur() { return valeur; }

    @Override
    public String toString() { return Long.toString(valeur); }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj instanceof Entier) return this.valeur == ((Entier) obj).valeur;
        if (obj instanceof Variable) {
            Variable v = (Variable) obj;
            Terme val = v.getValeur();
            return val != null && this.equals(val);
        }
        return false;
    }
}
