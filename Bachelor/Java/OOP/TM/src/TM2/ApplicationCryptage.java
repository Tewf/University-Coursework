package TM2;

import java.util.Scanner;  // Permet de lire ce que l'utilisateur tape au clavier

/**
 * APPLICATION DE CRYPTAGE - Une console interactive pour tester les chiffrements.
 * 
 * Comment ça marche ?
 * 1. L'utilisateur choisit une méthode de cryptage (Décalage ou Playfair)
 * 2. L'utilisateur entre une clef secrète
 * 3. L'utilisateur entre un texte à crypter
 * 4. Le programme crypte le texte, puis le décrypte pour vérifier
 * 
 * Exemple :
 *   Choix : 1 (Décalage)
 *   Clef : "secret"
 *   Texte : "hello"
 *   => Texte crypté : "snmmv" (chaque lettre est remplacée selon la clef)
 *   => Texte décrypté : "hello" (on retrouve le texte original)
 */
public class ApplicationCryptage {
    /**
     * La méthode main est le point de départ du programme.
     * C'est ici que tout commence quand tu exécutes l'application.
     * 
     * @param args les arguments de la ligne de commande (non utilisés ici)
     */
    public static void main(String[] args) {
        // Créer un objet Scanner pour lire les entrées de l'utilisateur depuis le clavier
        // Créer un objet Scanner pour lire les entrées de l'utilisateur depuis le clavier
        Scanner sc = new Scanner(System.in);

        // --- AFFICHER LE MENU ---
        // On affiche un titre et les options disponibles
        System.out.println("=== APPLICATION DE CRYPTAGE ===");
        System.out.println("Choisissez la méthode de cryptage :");
        System.out.println("1 - Decalage   (chiffrement de César avec clef)");
        System.out.println("2 - Playfair   (chiffrement avec matrice 6x6)");
        System.out.print("Votre choix : ");
        // Lire le choix de l'utilisateur (un nombre : 1 ou 2)
        int choix = sc.nextInt();
        // Le Scanner laisse une fin de ligne en attente; cette ligne l'enlève
        // (c'est comme appuyer sur Entrée après avoir tapé le nombre)
        sc.nextLine();

        // --- DEMANDER LA CLÉ SECRÈTE ---
        System.out.print("Entrez le mot clef : ");
        // Lire la clef et la convertir en minuscules (plus facile à traiter)
        String clef = sc.nextLine().toLowerCase();

        // --- DEMANDER LE TEXTE À CRYPTER ---
        System.out.print("Entrez le texte à crypter : ");
        // Lire le texte et le convertir en minuscules
        String texte = sc.nextLine().toLowerCase();

        // --- CRÉER L'OBJET DE CRYPTAGE APPROPRIÉ ---
        // On déclare une variable de type Cryptage (la classe parent)
        // Elle va contenir soit un Decalage soit un Playfair selon le choix de l'utilisateur
        Cryptage c = null;

        // Vérifier le choix et créer l'objet correspondant
        if (choix == 1) {
            // Créer un chiffrement Décalage avec la clef fournie
            c = new Decalage(clef);
        } else if (choix == 2) {
            // Créer un chiffrement Playfair avec la clef fournie
            c = new Playfair(clef);
        } else {
            // Si le choix n'est ni 1 ni 2, afficher un message d'erreur
            System.out.println("Choix invalide. Veuillez relancer et choisir 1 ou 2.");
            // Fermer le Scanner (libérer les ressources)
            sc.close();
            // Quitter le programme
            return;
        }

        // --- AFFICHER LES INFORMATIONS DU CRYPTAGE ---
        // On affiche la clef utilisée et les alphabets (grâce à la méthode toString())
        System.out.println("\n" + c);

        // --- ÉTAPE 1 : CRYPTER LE TEXTE ---
        // Appeler la méthode cryptage() pour transformer le texte en secret
        String crypte = c.cryptage(texte);
        // Afficher le résultat du cryptage
        System.out.println("\nTexte clair  : " + texte);
        System.out.println("Texte crypté : " + crypte);

        // --- ÉTAPE 2 : DÉCRYPTER LE TEXTE ---
        // Appeler la méthode deCryptage() pour retrouver le texte original
        // Si le cryptage/décryptage fonctionne bien, on devrait obtenir le texte clair original
        String decrypte = c.deCryptage(crypte);
        // Afficher le texte décrypté (devrait être identique au texte clair original)
        System.out.println("Texte décrypté : " + decrypte);

        // --- FERMETURE ---
        // Fermer le Scanner pour libérer les ressources système
        sc.close();
    }
}