package TM3;

/**
 * Exception levée quand le décodage se termine au milieu d'un code de caractère.
 * 
 * Qu'est-ce que ça veut dire ?
 * Dans le codage Huffman, chaque caractère a un code en 0 et 1.
 * Par exemple : 'a' = "00", 'b' = "01", 'c' = "10"
 * 
 * Cette alarme se déclenche quand :
 * - On essaie de décoder "001" mais le code s'arrête au milieu
 * - On peut décoder 'a' ("00") mais il reste juste "1" qui ne correspond à rien
 * - C'est comme si on avait un mot incomplet : "bonjo" au lieu de "bonjour"
 */
public class FinDeTexteInattendueException extends Exception {
    /**
     * Constructeur sans message.
     * Crée une exception vide (sans explication).
     */
    public FinDeTexteInattendueException() {
        super();
    }

    /**
     * Constructeur avec un message d'erreur.
     * Crée une exception avec une explication de ce qui s'est mal passé.
     * 
     * @param message le message d'erreur à afficher
     */
    public FinDeTexteInattendueException(String message) {
        super(message);
    }
}