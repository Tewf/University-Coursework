package TM1;

/**
 * Cette classe représente une fraction mathématique (un nombre rationnel).
 * Une fraction a deux parties : un numérateur (le nombre du haut) et un dénominateur (le nombre du bas).
 * 
 * Par exemple : 3/4 signifie "3 divisé par 4"
 * 
 * Cette classe s'assure que toutes les fractions sont toujours simplifiées (réduites).
 * Par exemple, si vous créez 6/8, la classe va automatiquement la simplifier en 3/4.
 */
public class Fraction {
    // Le numérateur est le nombre du haut de la fraction (comme le 3 dans 3/4)
    private int numerateur;
    
    // Le dénominateur est le nombre du bas de la fraction (comme le 4 dans 3/4)
    private int denominateur;
    
    /**
     * Cette fonction calcule le PGCD (Plus Grand Commun Diviseur) de deux nombres.
     * Le PGCD est le plus grand nombre qui peut diviser les deux nombres sans reste.
     * 
     * Par exemple : PGCD(6, 8) = 2  (car 2 est le plus grand nombre qui divise 6 et 8)
     * On l'utilise pour simplifier les fractions : 6/8 = (6÷2)/(8÷2) = 3/4
     * 
     * @param a le premier nombre
     * @param b le deuxième nombre
     * @return le PGCD des deux nombres
     */
    int pgcd(int a, int b){
        // Cas de base : si b est 0, le PGCD est a
        if(b == 0){
            return a;
        }
        // Sinon, on applique l'algorithme d'Euclide récursivement
        // C'est comme une boucle qui continue jusqu'à ce que b devienne 0
        return pgcd(b, a % b);
    }

    /**
     * Constructeur sans paramètres : crée la fraction 0/1 (qui vaut 0).
     * C'est comme dire "je veux une fraction, mais je ne précise pas laquelle, donc donne-moi zéro".
     */
    public Fraction(){
        this(0);  // Appelle le constructeur avec un seul paramètre (celui juste en dessous)
    } 
    
    /**
     * Constructeur avec un seul nombre : crée une fraction qui représente un nombre entier.
     * Par exemple : Fraction(5) crée 5/1 (qui vaut 5)
     * 
     * @param n le nombre entier à représenter comme fraction
     */
    public Fraction(int n) {
        this(n, 1);  // Appelle le constructeur avec deux paramètres avec dénominateur = 1
    }
    
    /**
     * Constructeur principal avec numérateur et dénominateur.
     * C'est ici que toute la magie se passe !
     * 
     * Ce constructeur fait 3 choses importantes :
     * 1. Vérifie que le dénominateur n'est pas zéro (on ne peut pas diviser par zéro !)
     * 2. Simplifie la fraction en divisant par le PGCD
     * 3. S'assure que le dénominateur est toujours positif (le signe va sur le numérateur)
     * 
     * @param n le numérateur (nombre du haut)
     * @param d le dénominateur (nombre du bas)
     * @throws IllegalArgumentException si le dénominateur est zéro
     */
    public Fraction(int n, int d){
        // Vérification importante : on ne peut pas diviser par zéro !
        if(d == 0){
            throw new IllegalArgumentException("Denominator cannot be zero.");
        }
        
        // On calcule le PGCD pour simplifier la fraction
        // Math.abs() donne la valeur absolue (toujours positive)
        int gcd = pgcd(Math.abs(n), Math.abs(d));
        
        // On divise le numérateur et le dénominateur par le PGCD pour simplifier
        // Exemple : 6/8 avec PGCD=2 devient 3/4
        this.numerateur = n / gcd;
        this.denominateur = d / gcd;
        
        // Si le dénominateur est négatif, on déplace le signe vers le numérateur
        // Exemple : 3/-4 devient -3/4 (c'est plus standard)
        if(this.denominateur < 0){
            this.numerateur = -this.numerateur;
            this.denominateur = -this.denominateur;
        }
    }
    
    /**
     * Constructeur à partir d'une chaîne de caractères.
     * Permet de créer une fraction en écrivant du texte comme "3/4" ou "5".
     * 
     * Exemples :
     * - new Fraction("3/4") crée la fraction 3/4
     * - new Fraction("5") crée la fraction 5/1
     * 
     * @param s la chaîne représentant la fraction (format: "numérateur/dénominateur" ou "nombre")
     * @throws IllegalArgumentException si la chaîne est invalide ou le dénominateur est zéro
     */
    public Fraction(String s){
        // Vérification : la chaîne ne doit pas être vide ou nulle
        if(s == null || s.isEmpty()){
            throw new IllegalArgumentException("Input string cannot be null or empty.");
        }
        
        // On découpe la chaîne avec "/" comme séparateur
        // Exemple : "3/4" devient ["3", "4"]
        String[] parts = s.split("/");
        
        if(parts.length == 1){
            // Pas de "/", c'est un nombre entier
            // Exemple : "5" devient 5/1
            this.numerateur = Integer.parseInt(parts[0]);
            this.denominateur = 1;
        } else if(parts.length == 2){
            // Il y a un "/", on a deux parties
            // Exemple : "3/4"
            int n = Integer.parseInt(parts[0]);  // "3" → 3
            int d = Integer.parseInt(parts[1]);  // "4" → 4
            
            // Vérification : le dénominateur ne peut pas être zéro
            if(d == 0){
                throw new IllegalArgumentException("Denominator cannot be zero.");
            }
            
            // On simplifie la fraction comme dans le constructeur précédent
            int gcd = pgcd(Math.abs(n), Math.abs(d));
            this.numerateur = n / gcd;
            this.denominateur = d / gcd;
            
            // On s'assure que le dénominateur est positif
            if(this.denominateur < 0){
                this.numerateur = -this.numerateur;
                this.denominateur = -this.denominateur;
            }
        } else {
            // Trop de "/" dans la chaîne, format invalide
            throw new IllegalArgumentException("Invalid fraction format.");
        }
    }
    
    // ==================== GETTERS (Accesseurs) ====================
    // Ces méthodes permettent de lire les valeurs du numérateur et dénominateur
    
    /**
     * Retourne le numérateur de la fraction (le nombre du haut).
     * @return le numérateur
     */
    public int getNumerateur() {
        return numerateur;
    }

    /**
     * Retourne le dénominateur de la fraction (le nombre du bas).
     * @return le dénominateur
     */
    public int getDenominateur() {
        return denominateur;
    }
    
    // ==================== SETTERS (Mutateurs) ====================
    // Ces méthodes permettent de changer les valeurs, tout en gardant la fraction simplifiée
    
    /**
     * Change le numérateur de la fraction.
     * Crée une nouvelle fraction temporaire pour garantir que tout reste simplifié.
     * 
     * @param numerateur le nouveau numérateur
     */
    public void setNumerateur(int numerateur) {
        // On crée une nouvelle fraction avec le nouveau numérateur
        // pour s'assurer qu'elle sera simplifiée
        Fraction temp = new Fraction(numerateur, this.denominateur);
        this.numerateur = temp.numerateur;
        this.denominateur = temp.denominateur;
    }

    /**
     * Change le dénominateur de la fraction.
     * Crée une nouvelle fraction temporaire pour garantir que tout reste simplifié.
     * 
     * @param denominateur le nouveau dénominateur
     */
    public void setDenominateur(int denominateur) {
        // On crée une nouvelle fraction avec le nouveau dénominateur
        // pour s'assurer qu'elle sera simplifiée
        Fraction temp = new Fraction(this.numerateur, denominateur);
        this.numerateur = temp.numerateur;
        this.denominateur = temp.denominateur;
    }
    
    // ==================== MÉTHODES D'AFFICHAGE ====================
    
    /**
     * Convertit la fraction en texte pour l'afficher.
     * Si le dénominateur est 1, on affiche juste le numérateur (comme un nombre entier).
     * 
     * Exemples :
     * - 3/4 s'affiche "3/4"
     * - 5/1 s'affiche "5"
     * 
     * @return une représentation textuelle de la fraction
     */
    public String toString() {
        // Si le dénominateur est 1, on affiche juste le numérateur
        if (denominateur == 1) {
            return Integer.toString(numerateur);
        }
        // Sinon on affiche "numérateur/dénominateur"
        return numerateur + "/" + denominateur;
    } 
    
    /**
     * Méthode statique qui crée une fraction à partir d'une chaîne.
     * C'est juste une autre façon d'appeler le constructeur avec String.
     * 
     * @param ch la chaîne représentant la fraction
     * @return une nouvelle fraction
     */
    public static Fraction valueOf(String ch){
        return new Fraction(ch);
    }

    // ==================== MÉTHODES DE COMPARAISON ====================
    
    /**
     * Compare cette fraction avec une autre fraction.
     * Retourne un nombre négatif si cette fraction est plus petite,
     * zéro si elles sont égales, positif si cette fraction est plus grande.
     * 
     * La méthode utilise la multiplication croisée :
     * Pour comparer a/b et c/d, on calcule a*d - c*b
     * 
     * @param f la fraction à comparer
     * @return négatif, zéro, ou positif selon la comparaison
     */
    public int compareTo(Fraction f){
        // Multiplication croisée : a/b vs c/d  →  a*d - c*b
        return this.numerateur * f.denominateur - f.numerateur * this.denominateur;
    }

    /**
     * Vérifie si cette fraction est égale à un autre objet.
     * Deux fractions sont égales si elles représentent le même nombre.
     * 
     * Par exemple : 2/4 est égal à 1/2 (après simplification)
     * 
     * @param obj l'objet à comparer
     * @return true si les fractions sont égales, false sinon
     */
    public boolean equals(Object obj){
        // Si c'est exactement le même objet en mémoire, c'est égal
        if(this == obj) return true;
        // Si l'objet est null, ce n'est pas égal
        if(obj == null) return false;
        // Si ce n'est pas une Fraction, ce n'est pas égal
        if(!(obj instanceof Fraction)) return false;
        // On convertit en Fraction et on compare avec compareTo
        Fraction f = (Fraction) obj;
        return this.compareTo(f) == 0;
    }

    // ==================== OPÉRATIONS ARITHMÉTIQUES ====================
    
    /**
     * Additionne deux fractions (cette fraction + une autre fraction).
     * Pour additionner a/b + c/d, on calcule (a*d + c*b) / (b*d)
     * 
     * Exemple : 1/2 + 1/3 = (1*3 + 1*2) / (2*3) = 5/6
     * 
     * @param f la fraction à ajouter
     * @return une nouvelle fraction qui est la somme
     */
    public Fraction plus(Fraction f){
        // Formule : a/b + c/d = (a*d + c*b) / (b*d)
        int n = this.numerateur * f.denominateur + f.numerateur * this.denominateur;
        int d = this.denominateur * f.denominateur;
        return new Fraction(n, d);  // Le constructeur va simplifier automatiquement
    }
    
    /**
     * Multiplie deux fractions (cette fraction × une autre fraction).
     * Pour multiplier a/b × c/d, on calcule (a*c) / (b*d)
     * 
     * Exemple : 2/3 × 3/4 = (2*3) / (3*4) = 6/12 = 1/2 (après simplification)
     * 
     * @param f la fraction à multiplier
     * @return une nouvelle fraction qui est le produit
     */
    public Fraction fois(Fraction f){
        // Formule : a/b × c/d = (a*c) / (b*d)
        int n = this.numerateur * f.numerateur;
        int d = this.denominateur * f.denominateur;
        return new Fraction(n, d);
    } 
    
    /**
     * Soustrait une fraction de cette fraction (cette fraction - une autre fraction).
     * On multiplie l'autre fraction par -1, puis on additionne.
     * 
     * Exemple : 3/4 - 1/4 = 3/4 + (-1/4) = 2/4 = 1/2
     * 
     * @param f la fraction à soustraire
     * @return une nouvelle fraction qui est la différence
     */
    public Fraction moins(Fraction f){
        // On transforme f en -f en multipliant par -1
        Fraction negF = f.fois(new Fraction(-1));
        // Puis on additionne
        return this.plus(negF);
    }
    
    /**
     * Divise cette fraction par une autre fraction (cette fraction ÷ une autre fraction).
     * Pour diviser a/b ÷ c/d, on multiplie a/b × d/c (on inverse la deuxième fraction)
     * 
     * Exemple : 1/2 ÷ 3/4 = 1/2 × 4/3 = 4/6 = 2/3
     * 
     * @param f la fraction par laquelle diviser
     * @return une nouvelle fraction qui est le quotient
     * @throws IllegalArgumentException si on essaie de diviser par zéro (fraction 0/1)
     */
    public Fraction diviserPar(Fraction f){
        // On ne peut pas diviser par une fraction qui vaut zéro
        if(f.numerateur == 0){
            throw new IllegalArgumentException("Cannot divide by zero fraction.");
        }
        // On inverse la fraction f : c/d devient d/c
        Fraction inversef = new Fraction(f.denominateur, f.numerateur);
        // On multiplie par l'inverse
        return this.fois(inversef);
    }

}