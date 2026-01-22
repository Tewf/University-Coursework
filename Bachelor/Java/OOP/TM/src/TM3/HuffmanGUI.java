package TM3;

// ========== IMPORTS (Les outils qu'on va utiliser) ==========
// Ce sont comme des boîtes à outils qu'on ouvre au début

import javax.swing.*;        // Swing = la boîte à outils pour créer des fenêtres et des boutons
import java.awt.*;           // AWT = outils pour dessiner et organiser les choses dans la fenêtre
import java.awt.event.ActionEvent;      // Pour détecter quand on clique sur un bouton
import java.awt.event.ActionListener;   // Pour écouter les clics de bouton
import java.util.Map;        // Map = comme un dictionnaire (mot → définition)
import java.util.Set;        // Set = comme un ensemble d'éléments uniques

/**
 * =====================================================================
 * INTERFACE GRAPHIQUE POUR LE CODAGE DE HUFFMAN
 * =====================================================================
 * 
 * C'EST QUOI CETTE CLASSE ?
 * C'est une FENÊTRE (comme les fenêtres que tu vois sur ton ordinateur).
 * Cette fenêtre permet de :
 * 1. Taper un texte
 * 2. Le transformer en code secret (pleins de 0 et de 1)
 * 3. Le décoder pour retrouver le texte original
 * 
 * COMMENT C'EST ORGANISÉ ?
 * La fenêtre est divisée en plusieurs zones :
 * 
 *  ┌─────────────────────────────────────────┐
 *  │ [Arbre de Huffman]  [Dictionnaire]      │ ← En haut
 *  ├─────────────────────────────────────────┤
 *  │ Texte clair:                            │
 *  │ ┌─────────────────────────────────────┐ │
 *  │ │ abracadabra                         │ │ ← Zone pour taper
 *  │ └─────────────────────────────────────┘ │
 *  │          [Créer]  [Coder]               │ ← Boutons
 *  ├─────────────────────────────────────────┤
 *  │ Texte codé:                             │
 *  │ ┌─────────────────────────────────────┐ │
 *  │ │ 01010011010...                      │ │ ← Résultat
 *  │ └─────────────────────────────────────┘ │
 *  │               [Décoder]                 │ ← Bouton
 *  ├─────────────────────────────────────────┤
 *  │ Prêt.                                   │ ← Messages en bas
 *  └─────────────────────────────────────────┘
 */
public class HuffmanGUI extends JFrame {
    // JFrame = une fenêtre de base fournie par Java
    // "extends" = notre classe HÉRITE de JFrame (elle a toutes ses fonctionnalités)

    // ========== VARIABLES D'INSTANCE (Les "tiroirs" de notre fenêtre) ==========
    // Ce sont comme des tiroirs où on range les différentes parties de la fenêtre
    
    // Zone de texte pour le texte NORMAL (en clair)
    // JTextArea = une grande zone où on peut écrire plusieurs lignes
    private JTextArea texteClairArea;
    
    // Zone de texte pour le texte CODÉ (les 0 et les 1)
    private JTextArea texteCodeArea;
    
    // Zone de texte pour afficher le DICTIONNAIRE (quel caractère = quel code)
    private JTextArea dictionnaireArea;
    
    // Panneau pour DESSINER l'arbre de Huffman (avec des branches)
    private DessinHuffman arbrePanel;
    
    // Étiquette pour afficher des MESSAGES en bas de la fenêtre
    // (comme "Prêt.", "Erreur !", etc.)
    private JLabel infoLabel;
    
    // ========== LA CHOSE LA PLUS IMPORTANTE ==========
    // L'objet Huffman qui contient tout le système de codage/décodage
    // Au début, il est null (vide) car on ne l'a pas encore créé
    // On le créera quand on cliquera sur le bouton "Créer"
    private Huffman codageHuffman = null;

    /**
     * =====================================================================
     * MÉTHODE MAIN - LE POINT DE DÉPART DU PROGRAMME
     * =====================================================================
     * 
     * C'EST QUOI ?
     * C'est la PREMIÈRE chose qui s'exécute quand on lance le programme.
     * Comme le bouton "Start" d'un jeu vidéo !
     * 
     * QUE FAIT-ELLE ?
     * Elle crée la fenêtre et la rend visible à l'écran.
     * 
     * @param args les arguments de la ligne de commande (on ne les utilise pas ici)
     */
    public static void main(String[] args) {
        // EventQueue.invokeLater = façon spéciale de démarrer une interface graphique
        // Pourquoi ? Car les fenêtres doivent être créées dans un "thread spécial"
        // (c'est une règle de Java pour les interfaces graphiques)
        
        EventQueue.invokeLater(() -> {
            // Ce code s'exécute dans le bon "thread" (fil d'exécution)
            
            try {
                // On essaie de créer la fenêtre
                
                // Étape 1 : On crée une nouvelle fenêtre HuffmanGUI
                HuffmanGUI frame = new HuffmanGUI();
                
                // Étape 2 : On la rend VISIBLE (sinon elle existe mais on ne la voit pas)
                frame.setVisible(true);
                
            } catch (Exception e) {
                // Si quelque chose se passe mal, on affiche l'erreur dans la console
                e.printStackTrace();
            }
        });
    }

    /**
     * =====================================================================
     * CONSTRUCTEUR - LA RECETTE POUR CONSTRUIRE LA FENÊTRE
     * =====================================================================
     * 
     * C'EST QUOI ?
     * C'est la fonction qui est appelée quand on fait "new HuffmanGUI()".
     * Elle construit TOUTE la fenêtre pièce par pièce, comme assembler un puzzle !
     * 
     * QUE FAIT-ELLE ?
     * 1. Configure les paramètres de base de la fenêtre (titre, taille, etc.)
     * 2. Crée tous les composants (zones de texte, boutons, etc.)
     * 3. Les place au bon endroit dans la fenêtre
     * 4. Connecte les boutons aux actions (quand on clique, que se passe-t-il ?)
     */
    public HuffmanGUI() {
        // ========== CONFIGURATION DE BASE DE LA FENÊTRE ==========
        
        // Le TITRE qui apparaît en haut de la fenêtre (dans la barre bleue)
        setTitle("Codage de Huffman");
        
        // Que se passe-t-il quand on clique sur la croix rouge (fermer) ?
        // EXIT_ON_CLOSE = le programme s'arrête complètement
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // La POSITION et la TAILLE de la fenêtre
        // setBounds(x, y, largeur, hauteur)
        // x=100, y=100 : position sur l'écran (100 pixels du bord gauche et du bord haut)
        // largeur=800, hauteur=600 : la taille de la fenêtre
        setBounds(100, 100, 800, 600);
        
        // ========== ORGANISATION GÉNÉRALE ==========
        
        // BorderLayout = un système d'organisation en 5 zones :
        //    NORTH (nord = haut)
        //    SOUTH (sud = bas)
        //    EAST (est = droite)
        //    WEST (ouest = gauche)
        //    CENTER (centre = milieu)
        // 
        // On va mettre :
        // - NORTH : arbre + dictionnaire
        // - CENTER : zones de texte clair et codé
        // - SOUTH : messages d'information
        getContentPane().setLayout(new BorderLayout());

        // ========== PANNEAU DU HAUT (NORTH) : ARBRE + DICTIONNAIRE ==========
        
        // On crée un panneau (conteneur) qui va contenir l'arbre ET le dictionnaire
        // GridLayout(1, 2, 5, 5) = grille avec :
        //   - 1 ligne
        //   - 2 colonnes (arbre à gauche, dictionnaire à droite)
        //   - 5 pixels d'espacement horizontal
        //   - 5 pixels d'espacement vertical
        JPanel topPanel = new JPanel(new GridLayout(1, 2, 5, 5));
        
        // ---------- 1. ZONE POUR DESSINER L'ARBRE ----------
        
        // On crée le panneau qui va dessiner l'arbre de Huffman
        // DessinHuffman est une classe spéciale qui sait dessiner des arbres
        arbrePanel = new DessinHuffman(); 
        
        // On ajoute un cadre avec un titre "Arbre" autour du dessin
        // createTitledBorder = crée une bordure avec un titre
        arbrePanel.setBorder(BorderFactory.createTitledBorder("Arbre"));
        
        // On ajoute le panneau d'arbre au panneau du haut
        topPanel.add(arbrePanel);
        
        // ---------- 2. ZONE POUR AFFICHER LE DICTIONNAIRE ----------
        
        // On crée une zone de texte pour afficher le dictionnaire
        // JTextArea(10, 20) = 10 lignes visibles, 20 colonnes de largeur
        dictionnaireArea = new JTextArea(10, 20);
        
        // setEditable(false) = l'utilisateur ne peut PAS modifier le texte
        // (on veut juste afficher, pas laisser modifier)
        dictionnaireArea.setEditable(false);
        
        // On met la zone de texte dans un JScrollPane
        // Pourquoi ? Pour avoir des barres de défilement si le texte est trop long !
        JScrollPane dictionnaireScrollPane = new JScrollPane(dictionnaireArea);
        
        // On ajoute un cadre avec un titre "Dictionnaire"
        dictionnaireScrollPane.setBorder(BorderFactory.createTitledBorder("Dictionnaire"));
        
        // On ajoute le panneau du dictionnaire au panneau du haut
        topPanel.add(dictionnaireScrollPane);
        
        // On ajoute le panneau complet (arbre + dictionnaire) EN HAUT de la fenêtre
        getContentPane().add(topPanel, BorderLayout.NORTH);
        
        // ========== PANNEAU DU CENTRE : TEXTE CLAIR + TEXTE CODÉ ==========
        
        // On crée un panneau principal qui contiendra 2 parties empilées :
        // GridLayout(2, 1, 5, 5) = grille avec :
        //   - 2 lignes (texte clair en haut, texte codé en bas)
        //   - 1 colonne
        //   - 5 pixels d'espacement
        JPanel centerPanel = new JPanel(new GridLayout(2, 1, 5, 5));
        
        // ---------- 3. ZONE POUR LE TEXTE CLAIR (texte normal) ----------
        
        // On crée un panneau pour organiser le texte clair et ses boutons
        // BorderLayout permet de mettre la zone de texte au centre et les boutons en bas
        JPanel clairPanel = new JPanel(new BorderLayout());
        
        // On crée la zone de texte où l'utilisateur pourra taper
        // JTextArea(5, 50) = 5 lignes visibles, 50 colonnes de largeur
        texteClairArea = new JTextArea(5, 50);
        
        // On met la zone de texte dans un JScrollPane (pour les barres de défilement)
        JScrollPane clairScrollPane = new JScrollPane(texteClairArea);
        
        // On ajoute un cadre avec le titre "Texte clair"
        clairScrollPane.setBorder(BorderFactory.createTitledBorder("Texte clair"));
        
        // On place la zone de texte au CENTRE du panneau
        clairPanel.add(clairScrollPane, BorderLayout.CENTER);
        
        // ---------- BOUTONS POUR LE TEXTE CLAIR ----------
        
        // On crée un panneau pour les boutons
        // FlowLayout(FlowLayout.RIGHT) = les boutons seront alignés À DROITE
        JPanel clairButtonsPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        
        // On crée le bouton "Créer" (pour créer le codage de Huffman)
        JButton creerButton = new JButton("Créer");
        
        // On crée le bouton "Coder" (pour transformer le texte en 0 et 1)
        JButton coderButton = new JButton("Coder");
        
        // On ajoute les deux boutons au panneau de boutons
        clairButtonsPanel.add(creerButton);
        clairButtonsPanel.add(coderButton);
        
        // On place le panneau de boutons EN BAS de la zone de texte clair
        clairPanel.add(clairButtonsPanel, BorderLayout.SOUTH);
        
        // On ajoute tout le panneau "texte clair" au panneau central
        centerPanel.add(clairPanel);

        // ---------- 4. ZONE POUR LE TEXTE CODÉ (les 0 et les 1) ----------
        
        // On crée un panneau pour organiser le texte codé et son bouton
        JPanel codePanel = new JPanel(new BorderLayout());
        
        // On crée la zone de texte pour afficher/entrer le texte codé
        // JTextArea(5, 50) = 5 lignes visibles, 50 colonnes de largeur
        texteCodeArea = new JTextArea(5, 50);
        
        // On met la zone de texte dans un JScrollPane (pour les barres de défilement)
        JScrollPane codeScrollPane = new JScrollPane(texteCodeArea);
        
        // On ajoute un cadre avec le titre "Texte codé"
        codeScrollPane.setBorder(BorderFactory.createTitledBorder("Texte codé"));
        
        // On place la zone de texte au CENTRE du panneau
        codePanel.add(codeScrollPane, BorderLayout.CENTER);
        
        // ---------- BOUTON POUR LE TEXTE CODÉ ----------
        
        // On crée un panneau pour le bouton
        // FlowLayout(FlowLayout.RIGHT) = le bouton sera aligné À DROITE
        JPanel codeButtonsPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        
        // On crée le bouton "Décoder" (pour retransformer les 0 et 1 en texte normal)
        JButton decoderButton = new JButton("Décoder");
        
        // On ajoute le bouton au panneau
        codeButtonsPanel.add(decoderButton);
        
        // On place le panneau de bouton EN BAS de la zone de texte codé
        codePanel.add(codeButtonsPanel, BorderLayout.SOUTH);
        
        // On ajoute tout le panneau "texte codé" au panneau central
        centerPanel.add(codePanel);

        // On ajoute le panneau central complet (texte clair + texte codé) AU CENTRE de la fenêtre
        getContentPane().add(centerPanel, BorderLayout.CENTER);

        // ========== PANNEAU DU BAS (SOUTH) : ZONE D'INFORMATION ==========
        
        // On crée une étiquette (label) pour afficher des messages
        // Au départ, elle affiche "Prêt." pour dire que tout est OK
        infoLabel = new JLabel("Prêt.");
        
        // On ajoute un peu d'espace autour du texte (5 pixels de chaque côté)
        // createEmptyBorder(haut, gauche, bas, droite)
        infoLabel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        
        // On place l'étiquette EN BAS de la fenêtre
        getContentPane().add(infoLabel, BorderLayout.SOUTH);
        
        // ========== CONNEXION DES BOUTONS AUX ACTIONS ==========
        // C'est comme brancher des fils : "quand on clique sur ce bouton, fais cette action"
        
        // ---------- BOUTON "CRÉER" ----------
        // addActionListener = "écoute les clics sur ce bouton"
        // On crée un ActionListener (écouteur d'action) anonyme
        creerButton.addActionListener(new ActionListener() {
            // Méthode qui s'exécute QUAND on clique sur le bouton
            public void actionPerformed(ActionEvent e) {
                actionCreer();  // On appelle notre méthode actionCreer()
            }
        });
        
        // ---------- BOUTON "CODER" ----------
        coderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                actionCoder();  // On appelle notre méthode actionCoder()
            }
        });

        // ---------- BOUTON "DÉCODER" ----------
        decoderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                actionDecoder();  // On appelle notre méthode actionDecoder()
            }
        });
        
        // ========== FINITION ==========
        
        // pack() = ajuste automatiquement la taille de la fenêtre pour que tout rentre bien
        // C'est comme "emballer" tous les composants dans la taille parfaite
        pack();
        
        // Et voilà ! La fenêtre est construite et prête à être utilisée !
    }

    /**
     * =====================================================================
     * ACTION DU BOUTON "CRÉER"
     * =====================================================================
     * 
     * QUAND EST-ELLE APPELÉE ?
     * Quand l'utilisateur clique sur le bouton "Créer"
     * 
     * QUE FAIT-ELLE ?
     * 1. Lit le texte dans la zone "Texte clair"
     * 2. Crée l'arbre de Huffman et le dictionnaire basés sur ce texte
     * 3. Dessine l'arbre à l'écran
     * 4. Affiche le dictionnaire (quel caractère = quel code)
     * 
     * POURQUOI C'EST IMPORTANT ?
     * Il FAUT d'abord créer le codage avant de pouvoir coder/décoder !
     * C'est comme créer le "code secret" avant de l'utiliser.
     */
    private void actionCreer() {
        // ========== ÉTAPE 1 : RÉCUPÉRER LE TEXTE ==========
        
        // On lit tout le texte que l'utilisateur a tapé dans la zone "Texte clair"
        String texteRef = texteClairArea.getText();
        
        // Vérification : est-ce que le texte est vide ?
        if (texteRef.isEmpty()) {
            // Si oui, on affiche un message d'erreur et on s'arrête
            infoLabel.setText("Erreur : Le texte clair est vide. Veuillez entrer un texte de référence.");
            return;  // On sort de la fonction sans rien faire d'autre
        }

        try {
            // On essaie de créer le codage (peut échouer si problème)
            
            // ========== ÉTAPE 2 : CRÉER LE CODAGE DE HUFFMAN ==========
            
            // On crée un nouvel objet Huffman avec le texte de référence
            // C'est LÀ que tout se passe :
            // - Comptage des occurrences de chaque caractère
            // - Construction de l'arbre
            // - Génération du dictionnaire
            codageHuffman = new Huffman(texteRef);
            
            // ========== ÉTAPE 3 : DESSINER L'ARBRE ==========
            
            // On dit au panneau de dessin quel codage utiliser
            arbrePanel.setCodage(codageHuffman);
            
            // On force le panneau à se redessiner (rafraîchir l'affichage)
            // repaint() = "redessine-toi maintenant !"
            arbrePanel.repaint();
            
            // ========== ÉTAPE 4 : AFFICHER LE DICTIONNAIRE ==========
            
            // On récupère le dictionnaire du codage Huffman
            // (Map<Character, String> : caractère → code binaire)
            // On le transforme en texte joli avec formatDictionnaire()
            // Et on l'affiche dans la zone de texte du dictionnaire
            dictionnaireArea.setText(formatDictionnaire(codageHuffman.getDictionnaire()));
            
            // ========== ÉTAPE 5 : AFFICHER UN MESSAGE DE SUCCÈS ==========
            
            // On met à jour le message en bas de la fenêtre
            infoLabel.setText("Codage de Huffman créé avec succès. Prêt à coder.");
            
        } catch (Exception ex) {
            // ========== SI QUELQUE CHOSE SE PASSE MAL ==========
            
            // On affiche le message d'erreur en bas de la fenêtre
            infoLabel.setText("Erreur lors de la création du codage: " + ex.getMessage());
            
            // On affiche aussi les détails dans la console (pour le débogage)
            ex.printStackTrace();
        }
    }

    /**
     * =====================================================================
     * ACTION DU BOUTON "CODER"
     * =====================================================================
     * 
     * QUAND EST-ELLE APPELÉE ?
     * Quand l'utilisateur clique sur le bouton "Coder"
     * 
     * QUE FAIT-ELLE ?
     * 1. Lit le texte dans la zone "Texte clair"
     * 2. Le transforme en code binaire (une suite de 0 et de 1)
     * 3. Affiche le résultat dans la zone "Texte codé"
     * 4. Affiche des statistiques (combien de bits économisés)
     * 
     * EXEMPLE :
     * Texte clair : "abc"
     * Texte codé : "01011"
     */
    private void actionCoder() {
        // ========== VÉRIFICATION : LE CODAGE EST-IL CRÉÉ ? ==========
        
        // On vérifie si l'utilisateur a cliqué sur "Créer" avant
        if (codageHuffman == null) {
            // Si non, on affiche un message d'erreur
            infoLabel.setText("Erreur : Veuillez créer le codage d'abord (bouton 'Créer').");
            return;  // On s'arrête là
        }

        // ========== ÉTAPE 1 : RÉCUPÉRER LE TEXTE À CODER ==========
        
        // On lit le texte que l'utilisateur veut coder
        String texteACoder = texteClairArea.getText();
        
        try {
            // On essaie de coder le texte (peut échouer si caractère inconnu)
            
            // ========== ÉTAPE 2 : CODER LE TEXTE ==========
            
            // On appelle la méthode code() de notre objet Huffman
            // Elle transforme chaque caractère en son code binaire
            // Exemple : "abc" → "01011"
            String texteCode = codageHuffman.code(texteACoder);
            
            // ========== ÉTAPE 3 : AFFICHER LE RÉSULTAT ==========
            
            // On met le texte codé dans la zone "Texte codé"
            texteCodeArea.setText(texteCode);
            
            // ========== ÉTAPE 4 : CALCULER LES STATISTIQUES ==========
            
            // Taille du texte clair en BITS
            // Chaque caractère = 8 bits normalement (1 octet)
            // Exemple : "abc" = 3 caractères × 8 = 24 bits
            int tailleClairBits = texteACoder.length() * 8;
            
            // Taille du texte codé en BITS
            // Chaque '0' ou '1' = 1 bit
            // Exemple : "01011" = 5 bits
            int tailleCodeBits = texteCode.length();
            
            // ========== ÉTAPE 5 : AFFICHER LES STATISTIQUES ==========
            
            // On construit un message qui montre la compression
            // Exemple : "Texte clair: 3 caractères = 24 bits / Texte codé: 5 bits."
            // → On a économisé 19 bits !
            infoLabel.setText("Texte clair: " + texteACoder.length() + " caractères = " + tailleClairBits 
                              + " bits / Texte codé: " + tailleCodeBits + " bits.");
            
        } catch (CaractereInconnuException ex) {
            // ========== SI UN CARACTÈRE N'EST PAS DANS LE DICTIONNAIRE ==========
            
            // On vide la zone de texte codé
            texteCodeArea.setText("");
            
            // On affiche le message d'erreur
            // Exemple : "Caractère inconnu : 'z'"
            infoLabel.setText("Erreur de codage: " + ex.getMessage());
            
        } catch (Exception ex) {
            // ========== SI UNE AUTRE ERREUR SE PRODUIT ==========
            
            infoLabel.setText("Erreur inattendue lors du codage: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    /**
     * =====================================================================
     * ACTION DU BOUTON "DÉCODER"
     * =====================================================================
     * 
     * QUAND EST-ELLE APPELÉE ?
     * Quand l'utilisateur clique sur le bouton "Décoder"
     * 
     * QUE FAIT-ELLE ?
     * 1. Lit le code binaire (les 0 et les 1) dans la zone "Texte codé"
     * 2. Le retransforme en texte normal
     * 3. Affiche le résultat dans la zone "Texte clair"
     * 4. Affiche des statistiques
     * 
     * EXEMPLE :
     * Texte codé : "01011"
     * Texte clair : "abc"
     */
    private void actionDecoder() {
        // ========== VÉRIFICATION : LE CODAGE EST-IL CRÉÉ ? ==========
        
        // On vérifie si l'utilisateur a cliqué sur "Créer" avant
        if (codageHuffman == null) {
            infoLabel.setText("Erreur : Veuillez créer le codage d'abord (bouton 'Créer').");
            return;  // On s'arrête là
        }

        // ========== ÉTAPE 1 : RÉCUPÉRER LE TEXTE CODÉ ==========
        
        // On lit le texte codé (la suite de 0 et de 1)
        String texteABinaire = texteCodeArea.getText();
        
        // ========== VÉRIFICATION : EST-CE BIEN DU BINAIRE ? ==========
        
        // matches("[01]*") = vérifie que la chaîne contient SEULEMENT des '0' et des '1'
        // [01] = un caractère qui est soit '0' soit '1'
        // * = zéro ou plusieurs fois
        // Donc [01]* = une suite de '0' et '1' seulement
        if (!texteABinaire.matches("[01]*")) {
            // Si le texte contient autre chose (comme 'a', '2', etc.), on affiche une erreur
            infoLabel.setText("Erreur : Le texte à décoder doit contenir uniquement des '0' et des '1'.");
            return;
        }

        try {
            // On essaie de décoder (peut échouer si le code est incomplet)
            
            // ========== ÉTAPE 2 : DÉCODER LE TEXTE ==========
            
            // On appelle la méthode decode() de notre objet Huffman
            // Elle parcourt l'arbre en suivant les 0 et les 1
            // Exemple : "01011" → "abc"
            String texteDecode = codageHuffman.decode(texteABinaire);
            
            // ========== ÉTAPE 3 : AFFICHER LE RÉSULTAT ==========
            
            // On met le texte décodé dans la zone "Texte clair"
            texteClairArea.setText(texteDecode);
            
            // ========== ÉTAPE 4 : CALCULER LES STATISTIQUES ==========
            
            // Taille du texte décodé en BITS
            // Chaque caractère = 8 bits normalement
            int tailleClairBits = texteDecode.length() * 8; 
            
            // Taille du texte codé en BITS
            // Chaque '0' ou '1' = 1 bit
            int tailleCodeBits = texteABinaire.length();
            
            // ========== ÉTAPE 5 : AFFICHER LES STATISTIQUES ==========
            
            // On construit un message qui montre les tailles
            infoLabel.setText("Texte clair: " + texteDecode.length() + " caractères = " + tailleClairBits 
                              + " bits / Texte codé: " + tailleCodeBits + " bits.");
            
        } catch (FinDeTexteInattendueException ex) {
            // ========== SI LE CODE EST INCOMPLET ==========
            
            // Exemple : le code "010" s'arrête au milieu d'un caractère
            
            // On vide la zone de texte clair
            texteClairArea.setText("");
            
            // On affiche le message d'erreur
            infoLabel.setText("Erreur de décodage: " + ex.getMessage());
            
        } catch (Exception ex) {
            // ========== SI UNE AUTRE ERREUR SE PRODUIT ==========
            
            infoLabel.setText("Erreur inattendue lors du décodage: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    /**
     * =====================================================================
     * FORMATE LE DICTIONNAIRE POUR L'AFFICHAGE
     * =====================================================================
     * 
     * C'EST QUOI ?
     * Une méthode utilitaire (= aide) qui transforme le dictionnaire
     * (Map<Character, String>) en un texte joli à afficher.
     * 
     * EXEMPLE D'ENTRÉE :
     * Map : {'a' → "0", 'b' → "10", 'c' → "11"}
     * 
     * EXEMPLE DE SORTIE :
     * 'a' : 0
     * 'b' : 10
     * 'c' : 11
     * 
     * @param dictionnaire le dictionnaire à formater (Character → String)
     * @return une chaîne de caractères joliment formatée
     */
    private String formatDictionnaire(Map<Character, String> dictionnaire) {
        // StringBuilder = notre "cahier" où on écrit le résultat ligne par ligne
        StringBuilder sb = new StringBuilder();
        
        // ========== RÉCUPÉRER TOUS LES CARACTÈRES ==========
        
        // keySet() = ensemble de toutes les CLÉS (les caractères)
        // Exemple : {'a', 'b', 'c'}
        Set<Character> caracteres = dictionnaire.keySet();
        
        // Note : On pourrait trier les caractères pour un affichage dans l'ordre alphabétique
        // (mais ce n'est pas fait ici, ils apparaîtront dans un ordre "aléatoire")
        
        // ========== PARCOURIR CHAQUE CARACTÈRE ==========
        
        // Pour chaque caractère dans le dictionnaire
        for (Character c : caracteres) {
            // On récupère le code binaire de ce caractère
            String code = dictionnaire.get(c);
            
            // ========== FORMATER LE CARACTÈRE POUR L'AFFICHAGE ==========
            
            // Certains caractères sont invisibles ou spéciaux, on les affiche différemment :
            
            String charAffichage;
            
            if (c == ' ') {
                // Un ESPACE est invisible, on l'affiche comme "' ' (espace)"
                charAffichage = "' ' (espace)";
            } else if (c == '\n') {
                // Un RETOUR À LA LIGNE est invisible, on l'affiche comme "\n (saut de ligne)"
                charAffichage = "\\n (saut de ligne)";
            } else if (c == '\t') {
                // Une TABULATION est invisible, on l'affiche comme "\t (tabulation)"
                charAffichage = "\\t (tabulation)";
            } else if (c == '-') {
                // Le trait d'union, on le garde tel quel
                charAffichage = "-";
            } else {
                // Pour tous les autres caractères normaux (lettres, chiffres),
                // on les met entre guillemets simples : 'a', 'b', etc.
                charAffichage = "'" + c + "'";
            }
            
            // ========== CONSTRUIRE LA LIGNE ==========
            
            // On ajoute une ligne au format : 'a' : 0
            // append() = ajouter au StringBuilder
            sb.append(charAffichage);     // Le caractère (ex: 'a')
            sb.append(" : ");             // Séparateur
            sb.append(code);              // Le code (ex: 0)
            sb.append("\n");              // Retour à la ligne
        }
        
        // ========== RETOURNER LE RÉSULTAT ==========
        
        // On transforme le StringBuilder en String et on le retourne
        return sb.toString();
    }
}