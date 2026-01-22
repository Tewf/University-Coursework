package TD3;

public class Variable extends Terme {
    private String nom;
    private Terme valeur;

    public Variable(String nom) { this.nom = nom; this.valeur = null; }

    public Variable(String nom, Terme valeur) { this.nom = nom; this.valeur = valeur; }

    public Terme getValeur() { return valeur; }

    @Override
    public String toString() {
        if (valeur == null) return nom + "=?";
        return nom + "=" + valeur.toString();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj instanceof Variable) {
            Variable v = (Variable) obj;
            if (this.nom.equals(v.nom)) {
                if (this.valeur == null && v.valeur == null) return true;
                if (this.valeur != null) return this.valeur.equals(v.valeur);
                return false;
            }
        }
        if (valeur != null) return valeur.equals(obj);
        return false;
    }
}
