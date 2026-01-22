package TM3bis;

import java.util.Map;

public class Feuille extends NoeudAbstrait {
    private final Character caractere;

    public Feuille(Character c, int poids) {
        super(poids);
        this.caractere = c;
    }

    public Character getCaractere() {
        return caractere;
    }

    @Override
    public void fournitCodes(Map<Character, String> m, String prefixe) {
        m.put(this.caractere, prefixe);
    }

    @Override
    public Character getNextChar(String s) {
        return caractere;
    }

    @Override
    public int hauteur() {
        return 1;
    }

    @Override
    public void fournitPoids(Map<Character, Integer> m) {
        // Ajoute l'association (caractere, poids) pour cette feuille
        m.put(this.caractere, this.getPoids());
    }
}