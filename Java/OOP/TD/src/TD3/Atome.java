package TD3;

public class Atome extends TermeAtomique {
    private String valeur;

    public Atome(String valeur) { this.valeur = valeur; }

    public String getValeur() { return valeur; }

    @Override
    public String toString() { return valeur; }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj instanceof Atome) return this.valeur.equals(((Atome) obj).valeur);
        if (obj instanceof Variable) {
            Variable v = (Variable) obj;
            Terme val = v.getValeur();
            return val != null && this.equals(val);
        }
        return false;
    }
}
