package TM2;

public abstract class Cryptage {
    // Alphabet de base
    public static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789";
    
    protected String alphabetDeCryptage;
    protected String clef;

    // Constructeur par défaut
    public Cryptage() {
        this.clef = "";
        this.alphabetDeCryptage = ALPHABET;
    }

    // Constructeur avec mot clef
    public Cryptage(String clef) {
        this.clef = clef;
        this.alphabetDeCryptage = ALPHABET; // valeur par défaut, sera redéfinie dans les sous-classes
    }

    // Méthodes abstraites à implémenter
    public abstract String cryptage(String s);
    public abstract String deCryptage(String s);

    @Override
    public String toString() {
    	return "Cryptage Decalage\nMot Clef : " + this.clef;
    }
}
