package TM3;

import java.util.Map;

/**
 * Une feuille de l'arbre de Huffman qui contient un caractère.
 * 
 * Qu'est-ce qu'une feuille ?
 * Dans un arbre, une feuille est un nœud qui n'a PAS d'enfants (pas de branches en dessous).
 * C'est le bout de la branche, là où s'arrête le chemin.
 * 
 * Dans notre arbre de Huffman :
 * - Chaque feuille représente UN caractère du texte (comme 'a', 'b', 'c', etc.)
 * - Le chemin de la racine à cette feuille donne le code binaire du caractère
 * - Le poids de la feuille = combien de fois le caractère apparaît dans le texte
 * 
 * Exemple : si 'a' apparaît 5 fois dans le texte, on crée une Feuille('a', 5)
 */
public class Feuille extends NoeudAbstrait {
    // Le caractère stocké dans cette feuille
    private final Character caractere;

    /**
     * Crée une nouvelle feuille avec un caractère et son poids.
     * 
     * @param c le caractère à stocker dans cette feuille
     * @param poids combien de fois ce caractère apparaît dans le texte
     */
    public Feuille(Character c, int poids) {
        // On appelle le constructeur de la classe parent (NoeudAbstrait) avec le poids
        super(poids);
        // On stocke le caractère
        this.caractere = c;
    }

    /**
     * Retourne le caractère stocké dans cette feuille.
     * 
     * Cette méthode est utilisée par DessinHuffman pour dessiner l'arbre.
     * 
     * @return le caractère
     */
    public Character getCaractere() {
        return caractere;
    }
    		
    /**
     * Ajoute le code de ce caractère dans le dictionnaire.
     * 
     * Comme on est sur une feuille (bout de la branche), le préfixe accumulé jusqu'ici
     * est le code COMPLET du caractère !
     * 
     * Exemple : si on est arrivé ici avec le préfixe "010",
     *           alors le code du caractère est "010"
     * 
     * On ajoute donc dans le dictionnaire : caractère → "010"
     * 
     * @param m le dictionnaire à remplir
     * @param prefixe le code binaire complet de ce caractère
     */
    @Override
    public void fournitCodes(Map<Character, String> m, String prefixe) {
        // Le code complet du caractère est le préfixe
        // On l'ajoute dans le dictionnaire
        m.put(this.caractere, prefixe);
    }

    /**
     * Retourne le caractère de cette feuille.
     * 
     * Comme on est déjà sur une feuille (pas besoin de descendre plus bas),
     * on retourne directement le caractère sans regarder la chaîne s.
     * 
     * @param s la chaîne de bits (non utilisée ici car on est déjà arrivé)
     * @return le caractère de cette feuille
     */
    @Override
    public Character getNextChar(String s) {
        // Déjà sur une feuille: on renvoie le caractère immédiatement
        return caractere;
    }

    /**
     * Retourne la hauteur de cette feuille.
     * 
     * Une feuille a une hauteur de 1 (elle compte comme 1 étage).
     * Il n'y a rien en dessous d'une feuille, donc pas d'étages supplémentaires.
     * 
     * @return 1 (hauteur d'une feuille)
     */
    @Override
    public int hauteur() {
        return 1;
    }
}