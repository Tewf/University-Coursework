package TM1;

import java.util.Scanner;

/**
 * Cette classe décompose une fraction en "fractions égyptiennes".
 * 
 * Qu'est-ce qu'une fraction égyptienne ?
 * Les anciens Égyptiens écrivaient toutes leurs fractions comme des sommes de fractions avec 1 au numérateur.
 * Par exemple : 3/5 = 1/2 + 1/10  (on additionne des "un demi" et des "un dixième")
 * 
 * Cette classe utilise l'algorithme glouton (greedy algorithm) :
 * À chaque étape, on prend la plus grande fraction unitaire possible (1/k)
 * qui ne dépasse pas ce qui reste à décomposer.
 */
public class EgyptianDecomposer {

    /**
     * Décompose une fraction en fractions égyptiennes et retourne le résultat sous forme de texte.
     * 
     * Comment ça marche ?
     * 1. On commence avec la fraction qu'on veut décomposer
     * 2. On trouve le plus petit k tel que 1/k ≤ fraction restante
     * 3. On soustrait 1/k de la fraction
     * 4. On répète jusqu'à ce qu'il ne reste rien
     * 
     * Exemple : 3/5
     * - 3/5 ≥ 1/2 (car 3/5 = 0.6 et 1/2 = 0.5), donc on prend 1/2
     * - Il reste 3/5 - 1/2 = 6/10 - 5/10 = 1/10
     * - On prend 1/10
     * - Il ne reste plus rien
     * - Résultat : "3/5 = 1/2 + 1/10"
     * 
     * @param x la fraction à décomposer
     * @return une chaîne de caractères montrant la décomposition
     */
    public static String decomposeToString(Fraction x) {
        // StringBuilder est comme un cahier où on écrit petit à petit notre résultat
        StringBuilder sb = new StringBuilder();
        // On commence par écrire la fraction originale suivie de " = "
        sb.append(x).append(" = ");

        // On fait une copie de la fraction pour pouvoir la modifier sans toucher l'originale
        Fraction cur = new Fraction(x.getNumerateur(), x.getDenominateur());
        // Ce booléen nous dit si c'est la première fraction unitaire (pour savoir si on met "+" ou pas)
        boolean first = true;

        // On continue tant qu'il reste quelque chose à décomposer (numérateur != 0)
        while (cur.getNumerateur() != 0) {
            // On récupère le numérateur et le dénominateur de ce qui reste
            int n = cur.getNumerateur();
            int d = cur.getDenominateur();
            
            // On calcule k : le plus petit entier tel que 1/k ≤ cur
            // Formule mathématique : k = ceil(d/n) = (d + n - 1) / n
            // Exemple : si cur = 3/5, alors d=5, n=3, k = (5+3-1)/3 = 7/3 = 2
            // Donc 1/k = 1/2, et effectivement 1/2 ≤ 3/5
            int k = (d + n - 1) / n;

            // Si ce n'est pas la première fraction, on ajoute " + "
            if (!first) sb.append(" + ");
            // On ajoute la fraction unitaire 1/k au résultat
            sb.append("1/").append(k);
            first = false;

            // On soustrait 1/k de ce qui reste
            // cur devient cur - 1/k
            cur = cur.moins(new Fraction(1, k));
        }
        // On retourne la chaîne complète (exemple : "3/5 = 1/2 + 1/10")
        return sb.toString();
    }


    /**
     * Programme principal pour tester la décomposition égyptienne.
     * 
     * Ce programme :
     * 1. Demande à l'utilisateur de taper une fraction (comme "3/5")
     * 2. Décompose cette fraction en fractions égyptiennes
     * 3. Affiche le résultat
     * 
     * @param args arguments de la ligne de commande (non utilisés)
     */
    public static void main(String[] args) {
        // Scanner permet de lire ce que l'utilisateur tape au clavier
        Scanner sc = new Scanner(System.in);
        System.out.print("Entrez une fraction (ex: 3/5) : ");
        String s = sc.nextLine();  // On lit une ligne complète de texte
        sc.close();  // On ferme le scanner (bonne pratique)

        try {
            // On essaie de créer une fraction à partir du texte tapé
            Fraction f = Fraction.valueOf(s);
            // On décompose et on affiche le résultat
            System.out.println(decomposeToString(f));
        } catch (Exception e) {
            // S'il y a une erreur (format invalide, etc.), on l'affiche
            System.err.println("Erreur: " + e.getMessage());
        }
    }
}
