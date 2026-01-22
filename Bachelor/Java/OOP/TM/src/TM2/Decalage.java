package TM2;

public class Decalage extends Cryptage {
    
    public Decalage(String clef) {
        super(clef);
        this.alphabetDeCryptage = alphabetDeCryptage(clef);
    }

    // Construit l'alphabet de cryptage
    public String alphabetDeCryptage(String clef) {
        String d = ALPHABET;

        for (int i = 0; i < clef.length(); i++) {
            char c = clef.charAt(i);
            int j = d.indexOf(c);
            if (j != -1) {
                d = d.substring(0, j) + d.substring(j + 1);
            }
        }

        d = clef + d;

        // Décalage vers la droite de la longueur de la clef
        int n = clef.length() % d.length();
        String reste = d.substring(d.length() - n);
        d = reste + d.substring(0, d.length() - n);

        return d;
    }

    @Override
    public String cryptage(String mot) {
        String rep = "";
        for (int i = 0; i < mot.length(); i++) {
            char c = mot.charAt(i);
            int idx = ALPHABET.indexOf(c);
            if (idx != -1)
                rep += alphabetDeCryptage.charAt(idx);
            else
                rep += c; // laisse le caractère inchangé
        }
        return rep;
    }

    @Override
    public String deCryptage(String mot) {
        String rep = "";
        for (int i = 0; i < mot.length(); i++) {
            char c = mot.charAt(i);
            int idx = alphabetDeCryptage.indexOf(c);
            if (idx != -1)
                rep += ALPHABET.charAt(idx);
            else
                rep += c;
        }
        return rep;
    }

    @Override
    public String toString() {
        return "Cryptage Decalage\nMot Clef : " + clef +
               "\nTransformation de cryptage : " + ALPHABET +
               "\n                             " + alphabetDeCryptage;
    }
}