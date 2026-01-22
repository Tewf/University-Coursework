package TM1; // ton projet est dans le package TM1, donc on le garde

// On importe les outils de Swing (fenêtre, boutons, champs texte, etc.)
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;

// Notre classe qui crée la fenêtre graphique
public class FractionGUI extends JFrame {

    // On prépare les zones de texte pour garder une "mémoire"
    private JTextField tfExpression; // où l’utilisateur écrit une expression
    private JTextField tfResult;     // où on affiche le résultat

    private JTextField tfFraction;   // où l’utilisateur écrit une fraction
    private JTextField tfEgypt;      // où on affiche la décomposition égyptienne

    // Le constructeur = quand on crée l’objet, on construit la fenêtre
    public FractionGUI() {
        super("TP1 : fractions"); // le titre écrit en haut de la fenêtre

        // On crée un "panneau racine" qui contiendra tout
        JPanel root = new JPanel();
        root.setBorder(new EmptyBorder(8, 8, 8, 8)); // petite marge autour
        root.setLayout(new BoxLayout(root, BoxLayout.Y_AXIS)); // tout sera empilé verticalement
        setContentPane(root); // on dit que c’est ce panneau qui sera affiché

        // ===================== SECTION 1 : Expression =====================
        // Un texte gris pour indiquer la section
        JLabel titre1 = new JLabel("évaluer une expression fraction");
        titre1.setOpaque(true); // pour que la couleur de fond soit visible
        titre1.setBackground(new Color(0xD9,0xD9,0xD9)); // gris clair
        titre1.setBorder(new EmptyBorder(6, 10, 6, 10)); // marges internes
        root.add(titre1); // on ajoute à la fenêtre

        // Un champ pour écrire l’expression (comme 12/34+123/321*5/6=)
        tfExpression = new JTextField();
        tfExpression.setMaximumSize(new Dimension(Integer.MAX_VALUE, 28)); // occupe toute la largeur
        tfExpression.setText("12/34+123/321*5/6="); // texte d’exemple
        root.add(tfExpression);

        // Un bouton "Calculer" pour lancer le calcul
        JButton btnCalc = new JButton("Calculer");
        root.add(btnCalc);

        // Un champ où on mettra le résultat (lecture seule)
        tfResult = new JTextField();
        tfResult.setEditable(false); // on ne peut pas écrire dedans
        tfResult.setMaximumSize(new Dimension(Integer.MAX_VALUE, 28));
        root.add(tfResult);

        // Petit texte d’aide en dessous
        JLabel aide = new JLabel("Entrer une expression terminée par = (la barre de fraction est /)");
        aide.setFont(aide.getFont().deriveFont(Font.PLAIN, 12f)); // plus petit
        root.add(aide);

        // ===================== SECTION 2 : Fractions égyptiennes =====================
        // Deuxième section (pareil que la première mais pour décomposer une fraction)
        JLabel titre2 = new JLabel("fractions égyptiennes");
        titre2.setOpaque(true);
        titre2.setBackground(new Color(0xD9,0xD9,0xD9));
        titre2.setBorder(new EmptyBorder(6, 10, 6, 10));
        root.add(titre2);

        // Champ pour écrire une fraction (ex : 3/5)
        tfFraction = new JTextField();
        tfFraction.setMaximumSize(new Dimension(Integer.MAX_VALUE, 28));
        tfFraction.setText("3/5"); // exemple
        root.add(tfFraction);

        // Bouton pour lancer la décomposition
        JButton btnEgypt = new JButton("Décomposer");
        root.add(btnEgypt);

        // Champ pour afficher le résultat (lecture seule)
        tfEgypt = new JTextField();
        tfEgypt.setEditable(false);
        tfEgypt.setMaximumSize(new Dimension(Integer.MAX_VALUE, 28));
        root.add(tfEgypt);

        // ===================== ACTIONS =====================
        // Quand on clique sur "Calculer" ou qu’on appuie sur Entrée dans le champ
        btnCalc.addActionListener(e -> evaluateExpression());
        tfExpression.addActionListener(e -> evaluateExpression());

        // Quand on clique sur "Décomposer" ou qu’on appuie sur Entrée dans le champ
        btnEgypt.addActionListener(e -> decomposeFraction());
        tfFraction.addActionListener(e -> decomposeFraction());

        // ===================== FENÊTRE =====================
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // fermer quand on clique sur la croix rouge
        setSize(520, 300); // largeur et hauteur
        setLocationRelativeTo(null); // centrer la fenêtre
    }

    // ===================== MÉTHODES =====================

    // Cette fonction prend le texte de l’expression, l’envoie à ExpressionCalculator
    // et affiche le résultat.
    private void evaluateExpression() {
        String input = tfExpression.getText().trim(); // on récupère le texte tapé

        try {
            // On appelle ta classe ExpressionCalculator (déjà écrite ailleurs)
            Fraction result = ExpressionCalculator.evaluate(input);

            // On écrit le résultat dans le champ résultat
            tfResult.setText(result.toString());
        } catch (Exception ex) {
            // S’il y a une erreur (ex : mauvaise syntaxe), on affiche l’erreur
            tfResult.setText("Erreur : " + ex.getMessage());
        }
    }

    // Cette fonction prend une fraction, appelle EgyptianDecomposer
    // et affiche la décomposition égyptienne.
    private void decomposeFraction() {
        String input = tfFraction.getText().trim();

        try {
            Fraction f = new Fraction(input); // on crée une fraction à partir du texte

            // On appelle ta classe EgyptianDecomposer (déjà écrite ailleurs)
            String decomposition = EgyptianDecomposer.decomposeToString(f);

            tfEgypt.setText(decomposition);
        } catch (Exception ex) {
            tfEgypt.setText("Erreur : " + ex.getMessage());
        }
    }

    // ===================== MAIN =====================
    public static void main(String[] args) {
        // Ici on démarre le programme → la fenêtre apparaît
        SwingUtilities.invokeLater(() -> new FractionGUI().setVisible(true));
    }
}
