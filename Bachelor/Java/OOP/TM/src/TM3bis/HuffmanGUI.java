package TM3bis;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Map;
import java.util.Set;

public class HuffmanGUI extends JFrame {
    
    private JTextArea texteClairArea;
    
    private JTextArea texteCodeArea;
    
    private JTextArea dictionnaireArea;
    
    private DessinHuffman arbrePanel;
    
    private JLabel infoLabel;
    
    private Huffman codageHuffman = null;

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                HuffmanGUI frame = new HuffmanGUI();
                frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    public HuffmanGUI() {
        setTitle("Codage de Huffman");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 800, 600);
        getContentPane().setLayout(new BorderLayout());

        JPanel topPanel = new JPanel(new GridLayout(1, 2, 5, 5));
        arbrePanel = new DessinHuffman();
        arbrePanel.setBorder(BorderFactory.createTitledBorder("Arbre"));
        topPanel.add(arbrePanel);

        dictionnaireArea = new JTextArea(10, 20);
        dictionnaireArea.setEditable(false);
        JScrollPane dictionnaireScrollPane = new JScrollPane(dictionnaireArea);
        dictionnaireScrollPane.setBorder(BorderFactory.createTitledBorder("Dictionnaire"));
        topPanel.add(dictionnaireScrollPane);
        getContentPane().add(topPanel, BorderLayout.NORTH);

        JPanel centerPanel = new JPanel(new GridLayout(2, 1, 5, 5));

        JPanel clairPanel = new JPanel(new BorderLayout());
        texteClairArea = new JTextArea(5, 50);
        JScrollPane clairScrollPane = new JScrollPane(texteClairArea);
        clairScrollPane.setBorder(BorderFactory.createTitledBorder("Texte clair"));
        clairPanel.add(clairScrollPane, BorderLayout.CENTER);

        JPanel clairButtonsPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        JButton creerButton = new JButton("Créer");
        JButton coderButton = new JButton("Coder");
        clairButtonsPanel.add(creerButton);
        clairButtonsPanel.add(coderButton);
        clairPanel.add(clairButtonsPanel, BorderLayout.SOUTH);
        centerPanel.add(clairPanel);

        JPanel codePanel = new JPanel(new BorderLayout());
        texteCodeArea = new JTextArea(5, 50);
        JScrollPane codeScrollPane = new JScrollPane(texteCodeArea);
        codeScrollPane.setBorder(BorderFactory.createTitledBorder("Texte codé"));
        codePanel.add(codeScrollPane, BorderLayout.CENTER);

        JPanel codeButtonsPanel = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        JButton decoderButton = new JButton("Décoder");
        codeButtonsPanel.add(decoderButton);
        codePanel.add(codeButtonsPanel, BorderLayout.SOUTH);
        centerPanel.add(codePanel);

        getContentPane().add(centerPanel, BorderLayout.CENTER);

        infoLabel = new JLabel("Prêt.");
        infoLabel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        getContentPane().add(infoLabel, BorderLayout.SOUTH);

        creerButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                actionCreer();
            }
        });

        coderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                actionCoder();
            }
        });

        decoderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                actionDecoder();
            }
        });

        pack();
    }

    private void actionCreer() {
        String texteRef = texteClairArea.getText();
        if (texteRef.isEmpty()) {
            infoLabel.setText("Erreur : Le texte clair est vide. Veuillez entrer un texte de référence.");
            return;
        }

        try {
            codageHuffman = new Huffman(texteRef);
            arbrePanel.setCodage(codageHuffman);
            arbrePanel.repaint();
            dictionnaireArea.setText(formatDictionnaire(codageHuffman.getDictionnaire()));
            infoLabel.setText("Codage de Huffman créé avec succès. Prêt à coder.");
        } catch (Exception ex) {
            infoLabel.setText("Erreur lors de la création du codage: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    private void actionCoder() {
        if (codageHuffman == null) {
            infoLabel.setText("Erreur : Veuillez créer le codage d'abord (bouton 'Créer').");
            return;
        }

        String texteACoder = texteClairArea.getText();

        try {
            String texteCode = codageHuffman.code(texteACoder);
            texteCodeArea.setText(texteCode);
            int tailleClairBits = texteACoder.length() * 8;
            int tailleCodeBits = texteCode.length();
            infoLabel.setText("Texte clair: " + texteACoder.length() + " caractères = " + tailleClairBits 
                              + " bits / Texte codé: " + tailleCodeBits + " bits.");

        } catch (CaractereInconnuException ex) {
            texteCodeArea.setText("");
            infoLabel.setText("Erreur de codage: " + ex.getMessage());

        } catch (Exception ex) {
            infoLabel.setText("Erreur inattendue lors du codage: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    private void actionDecoder() {
        if (codageHuffman == null) {
            infoLabel.setText("Erreur : Veuillez créer le codage d'abord (bouton 'Créer').");
            return;
        }

        String texteABinaire = texteCodeArea.getText();
        if (!texteABinaire.matches("[01]*")) {
            infoLabel.setText("Erreur : Le texte à décoder doit contenir uniquement des '0' et des '1'.");
            return;
        }

        try {
            String texteDecode = codageHuffman.decode(texteABinaire);
            texteClairArea.setText(texteDecode);
            int tailleClairBits = texteDecode.length() * 8;
            int tailleCodeBits = texteABinaire.length();
            infoLabel.setText("Texte clair: " + texteDecode.length() + " caractères = " + tailleClairBits 
                              + " bits / Texte codé: " + tailleCodeBits + " bits.");

        } catch (FinDeTexteInattendueException ex) {
            texteClairArea.setText("");
            infoLabel.setText("Erreur de décodage: " + ex.getMessage());

        } catch (Exception ex) {
            infoLabel.setText("Erreur inattendue lors du décodage: " + ex.getMessage());
            ex.printStackTrace();
        }
    }

    private String formatDictionnaire(Map<Character, String> dictionnaire) {
        StringBuilder sb = new StringBuilder();
        Set<Character> caracteres = dictionnaire.keySet();
        for (Character c : caracteres) {
            String code = dictionnaire.get(c);
            String charAffichage;
            if (c == ' ') {
                charAffichage = "' ' (espace)";
            } else if (c == '\n') {
                charAffichage = "\\n (saut de ligne)";
            } else if (c == '\t') {
                charAffichage = "\\t (tabulation)";
            } else if (c == '-') {
                charAffichage = "-";
            } else {
                charAffichage = "'" + c + "'";
            }
            sb.append(charAffichage);
            sb.append(" : ");
            sb.append(code);
            sb.append("\n");
        }
        return sb.toString();
    }
}