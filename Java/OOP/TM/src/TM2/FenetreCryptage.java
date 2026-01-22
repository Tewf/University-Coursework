package TM2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FenetreCryptage extends JFrame {

    private Cryptage cryptageSystem; // The current encryption object (Decalage or Playfair)

    // GUI Components
    private JTextField keyField;
    private JTextArea clairText;
    private JTextArea cryptedText;

    private JRadioButton encryptRadio;
    private JRadioButton decryptRadio;
    
    private JTabbedPane cipherTabs;

    public FenetreCryptage() {
        setTitle("Cryptage...");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));

        // --- 1. Top Panel (Selection, Key, Radios) ---
        JPanel topPanel = new JPanel();
        topPanel.setLayout(new BoxLayout(topPanel, BoxLayout.Y_AXIS));

        // 1a. Cipher Selection (Tabs: Décalage / Playfair)
        cipherTabs = new JTabbedPane();
        cipherTabs.addTab("Décalage", createCipherPanel("Décalage"));
        cipherTabs.addTab("Playfair", createCipherPanel("Playfair"));
        cipherTabs.addChangeListener(e -> updateCipherSystem());
        topPanel.add(cipherTabs);

        // 1b. Key Input
        JPanel keyPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        keyPanel.add(new JLabel("Clef:"));
        keyField = new JTextField(15);
        keyPanel.add(keyField);
        topPanel.add(keyPanel);

        // 1c. Action Radios
        JPanel actionPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        encryptRadio = new JRadioButton("cryptage", true);
        decryptRadio = new JRadioButton("décryptage");
        
        ButtonGroup group = new ButtonGroup();
        group.add(encryptRadio);
        group.add(decryptRadio);
        
        actionPanel.add(encryptRadio);
        actionPanel.add(decryptRadio);
        topPanel.add(actionPanel);
        
        add(topPanel, BorderLayout.NORTH);
        
        // --- 2. Center/South Panels (Text Areas and Button) ---
        
        JPanel centerPanel = new JPanel(new GridLayout(2, 1, 10, 10));
        
        // Texte Clair
        clairText = createTextArea("Texte clair");
        centerPanel.add(new JScrollPane(clairText));

        // Texte Crypté
        cryptedText = createTextArea("Texte crypté");
        centerPanel.add(new JScrollPane(cryptedText));
        
        add(centerPanel, BorderLayout.CENTER);

        // --- 3. Execution Button ---
        JButton executeButton = new JButton("Execute");
        executeButton.addActionListener(this::executeCipher);
        add(executeButton, BorderLayout.SOUTH);
        
        // Initial setup
        updateCipherSystem();
        
        setSize(400, 550);
        setVisible(true);
    }

    // A placeholder panel for tabs (you could add info/settings here if needed)
    private JPanel createCipherPanel(String name) {
        JPanel panel = new JPanel();
        // panel.add(new JLabel("Selected: " + name)); // Optional: to show which cipher is active
        return panel;
    }
    
    // Helper method to create a titled text area
    private JTextArea createTextArea(String title) {
        JTextArea area = new JTextArea(5, 30);
        area.setBorder(BorderFactory.createTitledBorder(title));
        area.setLineWrap(true);
        area.setWrapStyleWord(true);
        return area;
    }
    
    // Updates the current cryptage system based on the selected tab and key
    private void updateCipherSystem() {
        String clef = keyField.getText();
        
        if (cipherTabs.getSelectedIndex() == 0) {
            // Décalage Tab is selected
            cryptageSystem = new Decalage(clef);
        } else {
            // Playfair Tab is selected
            cryptageSystem = new Playfair(clef);
        }
    }

    // Executes the encryption or decryption based on radio button selection
    private void executeCipher(ActionEvent event) {
        // 1. Update the system with the current key
        updateCipherSystem(); 
        
        String input;
        String output;
        
        if (encryptRadio.isSelected()) {
            // ENCRYPTION
            input = clairText.getText();
            output = cryptageSystem.cryptage(input);
            cryptedText.setText(output);
            
        } else if (decryptRadio.isSelected()) {
            // DECRYPTION
            input = cryptedText.getText();
            // We use the same cipher object (with the same key) to decrypt
            output = cryptageSystem.deCryptage(input);
            clairText.setText(output);
        }
    }

    public static void main(String[] args) {
        // Run the GUI on the Event Dispatch Thread
        SwingUtilities.invokeLater(FenetreCryptage::new);
    }
}