package TD3;

public class TermeFonctionnel extends Terme {
    private String foncteur;
    private Liste parametres;

    public TermeFonctionnel(String f, Liste p) { this.foncteur = f; this.parametres = p; }

    @Override
    public String toString() {
        return foncteur + parametres.toString();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof TermeFonctionnel)) return false;
        TermeFonctionnel o = (TermeFonctionnel) obj;
        if (!this.foncteur.equals(o.foncteur)) return false;
        if (this.parametres == null) return o.parametres == null;
        return this.parametres.equals(o.parametres);
    }
}
