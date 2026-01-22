package TM3;

/**
 * Exception levée quand on essaie de crypter un caractère qui n'existe pas dans le dictionnaire Huffman.
 * 
 * Qu'est-ce qu'une exception ?
 * C'est comme une alarme qui se déclenche quand quelque chose ne va pas.
 * 
 * Dans notre cas, cette alarme se déclenche quand :
 * - On essaie de crypter un texte avec un caractère qui n'était pas dans le texte de référence
 * - Par exemple : si on a créé le codage avec "hello", on ne peut pas crypter "bonjour"
 *   car 'b', 'o', 'n', 'j', 'u', 'r' ne sont pas dans le dictionnaire
 */
public class CaractereInconnuException extends Exception {
    /**
     * Constructeur sans message.
     * Crée une exception vide (sans explication).
     */
    public CaractereInconnuException() {
        super();
    }

    /**
     * Constructeur avec un message d'erreur.
     * Crée une exception avec une explication de ce qui s'est mal passé.
     * 
     * @param message le message d'erreur à afficher
     */
    public CaractereInconnuException(String message) {
        super(message);
    }
}