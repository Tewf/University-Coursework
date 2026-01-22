package TM1;

import java.util.Scanner;

/**
 * Cette classe calcule des expressions mathématiques contenant des fractions.
 * 
 * Elle peut comprendre des expressions comme :
 * - "12/34+123/321*5/6=" 
 * - "1/2 + 3/4"
 * - "5/6 - 1/3 * 2/5"
 * 
 * Les opérations supportées sont : + (addition), - (soustraction), * (multiplication), : (division)
 */
public class ExpressionCalculator  {

    /**
     * Programme principal pour tester le calculateur d'expressions.
     * 
     * Ce programme :
     * 1. Demande à l'utilisateur de taper une expression avec des fractions
     * 2. Calcule le résultat
     * 3. Affiche l'expression complète avec son résultat
     * 
     * @param args arguments de la ligne de commande (non utilisés)
     */
    public static void main(String[] args) {
        // Scanner permet de lire ce que l'utilisateur tape
        Scanner sc = new Scanner(System.in);
        System.out.print("Entrez une expression de fractions (ex: 12/34+123/321*5/6=) : ");
        String expr = sc.nextLine();  // On lit l'expression
        sc.close();  // On ferme le scanner

        try {
            // On essaie de calculer l'expression
            Fraction res = evaluate(expr);
            // On affiche l'expression suivie du résultat
            System.out.println(expr + res);
        } catch (Exception e) {
            // S'il y a une erreur, on l'affiche
            System.err.println("Erreur : " + e.getMessage());
        }
    }

    /**
     * Évalue une expression mathématique contenant des fractions.
     * 
     * Comment ça marche ?
     * L'algorithme lit l'expression de gauche à droite :
     * 1. On lit la première fraction
     * 2. On lit un opérateur (+, -, *, :)
     * 3. On lit la fraction suivante
     * 4. On fait le calcul
     * 5. On répète avec le résultat jusqu'à la fin
     * 
     * Exemple : "1/2+1/3*2/1"
     * - On lit 1/2
     * - On voit +, on lit 1/3, on calcule 1/2 + 1/3 = 5/6
     * - On voit *, on lit 2/1, on calcule 5/6 * 2 = 10/6 = 5/3
     * - Résultat : 5/3
     * 
     * ATTENTION : Cette méthode calcule de gauche à droite SANS priorité des opérations !
     * (normalement * devrait être calculé avant +, mais ici on fait tout dans l'ordre)
     * 
     * @param expr l'expression à évaluer (peut contenir des espaces, se terminer par =)
     * @return le résultat sous forme de Fraction
     * @throws IllegalArgumentException si l'expression est invalide
     */
    public static Fraction evaluate(String expr) {
        // Vérification : l'expression ne doit pas être nulle
        if (expr == null) throw new IllegalArgumentException("Expression nulle");

        // ÉTAPE 1 : Nettoyage de l'expression
        // On enlève tous les espaces (\\s+ signifie "un ou plusieurs espaces")
        // On enlève aussi les parenthèses (non gérées dans cette version simple)
        String s = expr.replaceAll("\\s+", "").replace("(", "").replace(")", "");
        
        // Si l'expression se termine par '=', on l'enlève
        int eq = s.indexOf('=');
        if (eq >= 0) s = s.substring(0, eq);
        
        // On vérifie que l'expression n'est pas vide
        if (s.isEmpty()) throw new IllegalArgumentException("Expression vide");

        // ÉTAPE 2 : Lire la première fraction
        // pos est notre position actuelle dans la chaîne
        int pos = 0;
        // On cherche le premier opérateur (ou la fin de la chaîne)
        int opIdx = detect(s, pos);
        // On crée une fraction avec le texte entre pos et opIdx
        // Exemple : si s = "1/2+3/4", alors substring(0, 3) = "1/2"
        Fraction result = new Fraction(s.substring(pos, opIdx));

        // ÉTAPE 3 : Boucler sur tous les (opérateur, fraction) qui suivent
        // On continue tant qu'il y a encore des caractères à lire
        while (opIdx < s.length()) {
            // On lit l'opérateur (+, -, *, :)
            char op = s.charAt(opIdx);
            
            // On se positionne après l'opérateur
            pos = opIdx + 1;
            
            // On cherche le prochain opérateur (ou la fin)
            opIdx = detect(s, pos);
            
            // On lit la fraction entre l'opérateur et le prochain opérateur
            Fraction term = new Fraction(s.substring(pos, opIdx));

            // On applique l'opération selon l'opérateur
            switch (op) {
                case '+': 
                    result = result.plus(term);      // Addition
                    break;
                case '-': 
                    result = result.moins(term);     // Soustraction
                    break;
                case '*': 
                    result = result.fois(term);      // Multiplication
                    break;
                case ':': 
                    result = result.diviserPar(term); // Division (on utilise : au lieu de /)
                    break;
                default:  
                    // Si l'opérateur n'est pas reconnu, on lance une erreur
                    throw new IllegalArgumentException("Operateur inconnu: " + op);
            }
        }
        // On retourne le résultat final
        return result;
    }

    /**
     * Cherche la position du prochain opérateur dans la chaîne.
     * 
     * Cette fonction parcourt la chaîne caractère par caractère à partir de 'from'
     * et s'arrête dès qu'elle trouve un opérateur (+, -, *, :).
     * Si aucun opérateur n'est trouvé, elle retourne la longueur de la chaîne
     * (ce qui signifie "fin de la chaîne").
     * 
     * Exemple : detect("1/2+3/4", 0) retourne 3 (position du '+')
     * Exemple : detect("1/2+3/4", 4) retourne 7 (fin de la chaîne, pas d'autre opérateur)
     * 
     * @param s la chaîne dans laquelle chercher
     * @param from la position de départ de la recherche
     * @return la position du prochain opérateur, ou la longueur de la chaîne
     */
    private static int detect(String s, int from) {
        // On parcourt la chaîne caractère par caractère
        for (int i = from; i < s.length(); i++) {
            char c = s.charAt(i);
            // Si on trouve un opérateur, on retourne sa position
            if (c == '+' || c == '-' || c == '*' || c == ':') return i;
        }
        // Si on n'a rien trouvé, on retourne la longueur (fin de chaîne)
        return s.length();
    }
}
