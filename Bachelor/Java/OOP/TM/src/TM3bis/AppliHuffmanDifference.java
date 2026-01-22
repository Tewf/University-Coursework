package TM3bis;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Iterator;
import java.util.Map;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.border.Border;
import javax.swing.border.EtchedBorder;
import javax.swing.border.SoftBevelBorder;

public class AppliHuffmanDifference {

	private JFrame frmTmCodage;
	private Huffman codage1;
	private Huffman codage2;
	private Huffman codage3;
	private JTextArea textAreaClair;
	private JTextArea textAreaCode;
	private JLabel lblMessage;
	private DessinHuffman panelDessinArbre1;
	private DessinHuffman panelDessinArbre2;
	private DessinHuffman panelDessinArbre3;
	private JTextArea textAreaDico1;
	private JTextArea textAreaDico2;
	private JTextArea textAreaDico3;
	private JButton btnCoder1;
	private JButton btnCoder2;
	private JButton btnCoder3;
	private JButton btnDcoder1;
	private JButton btnDcoder2;
	private JButton btnDcoder3;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AppliHuffmanDifference window = new AppliHuffmanDifference();
					window.frmTmCodage.setVisible(true);
				} catch (Exception var2) {
					var2.printStackTrace();
				}

			}
		});
	}

	public AppliHuffmanDifference() {

		this.initialize();
	}


	private void initialize() {

		this.frmTmCodage = new JFrame();
		this.frmTmCodage.setTitle("TM3 - Codage de Huffman");
		this.frmTmCodage.setBounds(100, 100, 1030, 600);
		this.frmTmCodage.setDefaultCloseOperation(3);

		this.lblMessage = new JLabel(" ");
		this.lblMessage.setFont(new Font("Tahoma", 0, 14));
		this.lblMessage.setHorizontalAlignment(0);
		this.frmTmCodage.getContentPane().add(this.lblMessage, "South");

		JPanel panelCentre = new JPanel();
		this.frmTmCodage.getContentPane().add(panelCentre, "Center");
		panelCentre.setLayout(new GridLayout(0, 1, 0, 0));

		JPanel panelCodages = new JPanel();
		panelCentre.add(panelCodages);
		panelCodages.setLayout(new GridLayout(1, 0, 0, 0));

		JPanel panelCodage1 = new JPanel();
		panelCodages.add(panelCodage1);
		panelCodage1.setLayout(new BorderLayout(0, 0));

		JPanel panelDico1 = new JPanel();
		panelCodage1.add(panelDico1, "East");
		panelDico1.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelDico1.setLayout(new BorderLayout(0, 0));

		JLabel lblDico = new JLabel("Dictionnaire");
		lblDico.setFont(new Font("Tahoma", 1, 14));
		lblDico.setHorizontalAlignment(0);
		panelDico1.add(lblDico, "North");

		JScrollPane scrollPaneDico1 = new JScrollPane();
		scrollPaneDico1.setViewportBorder(new SoftBevelBorder(1, (Color)null, (Color)null, (Color)null, (Color)null));
		panelDico1.add(scrollPaneDico1, "Center");

		this.textAreaDico1 = new JTextArea();
		scrollPaneDico1.setViewportView(this.textAreaDico1);

		JPanel panelArbre1 = new JPanel();
		panelCodage1.add(panelArbre1, "Center");
		panelArbre1.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelArbre1.setLayout(new BorderLayout(0, 0));

		JLabel lblArbre1 = new JLabel("Arbre");
		lblArbre1.setFont(new Font("Tahoma", 1, 14));
		lblArbre1.setHorizontalAlignment(0);
		panelArbre1.add(lblArbre1, "North");

		JScrollPane scrollPaneArbre1 = new JScrollPane();
		panelArbre1.add(scrollPaneArbre1, "Center");
		this.panelDessinArbre1 = new DessinHuffman();
		scrollPaneArbre1.setViewportView(this.panelDessinArbre1);

		JPanel panelBoutonArbre1 = new JPanel();
		panelArbre1.add(panelBoutonArbre1, "South");

		JButton btnCrerDepuisTexte1 = new JButton("Créer depuis Texte clair");
		btnCrerDepuisTexte1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					AppliHuffmanDifference.this.codage1 = new Huffman(AppliHuffmanDifference.this.textAreaClair.getText());
					AppliHuffmanDifference.this.panelDessinArbre1.setCodage(AppliHuffmanDifference.this.codage1);
					StringBuffer sDico = new StringBuffer();
					Map<Character, String> dico = AppliHuffmanDifference.this.codage1.getDictionnaire();
					Iterator var5 = dico.keySet().iterator();

					while(var5.hasNext()) {
						Character c = (Character)var5.next();
						sDico.append(c).append(" : ").append((String)dico.get(c)).append('\n');
					}

					AppliHuffmanDifference.this.textAreaDico1.setText(sDico.toString());
					AppliHuffmanDifference.this.message("Codage créé (" + dico.size() + " caractères)", Color.BLACK);
					AppliHuffmanDifference.this.btnCoder1.setEnabled(true);
					AppliHuffmanDifference.this.btnDcoder1.setEnabled(true);
					if (AppliHuffmanDifference.this.codage2 != null) {
						AppliHuffmanDifference.this.creeCodage3();
					}
				} catch (IllegalArgumentException var6) {
					AppliHuffmanDifference.this.message("Impossible de créer le codage : " + var6.getMessage(), Color.RED);
				}

			}
		});
		panelBoutonArbre1.add(btnCrerDepuisTexte1);

		JLabel lblCodage1 = new JLabel("Codage 1");
		lblCodage1.setFont(new Font("Tahoma", 1, 16));
		lblCodage1.setHorizontalAlignment(0);
		panelCodage1.add(lblCodage1, "North");

		JPanel panelCodage2 = new JPanel();
		panelCodages.add(panelCodage2);
		panelCodage2.setLayout(new BorderLayout(0, 0));

		JLabel lblCodage2 = new JLabel("Codage 2");
		lblCodage2.setFont(new Font("Tahoma", 1, 16));
		lblCodage2.setHorizontalAlignment(0);
		panelCodage2.add(lblCodage2, "North");

		JPanel panelDico2 = new JPanel();
		panelCodage2.add(panelDico2, "East");
		panelDico2.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelDico2.setLayout(new BorderLayout(0, 0));

		JLabel lblDico2 = new JLabel("Dictionnaire");
		lblDico2.setFont(new Font("Tahoma", 1, 14));
		lblDico2.setHorizontalAlignment(0);
		panelDico2.add(lblDico2, "North");

		JScrollPane scrollPaneDico2 = new JScrollPane();
		scrollPaneDico2.setViewportBorder(new SoftBevelBorder(1, (Color)null, (Color)null, (Color)null, (Color)null));
		panelDico2.add(scrollPaneDico2, "Center");
		this.textAreaDico2 = new JTextArea();
		scrollPaneDico2.setViewportView(this.textAreaDico2);

		JPanel panelArbre2 = new JPanel();
		panelCodage2.add(panelArbre2, "Center");
		panelArbre2.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelArbre2.setLayout(new BorderLayout(0, 0));

		JLabel lblArbre2 = new JLabel("Arbre");
		lblArbre2.setFont(new Font("Tahoma", 1, 14));
		lblArbre2.setHorizontalAlignment(0);
		panelArbre2.add(lblArbre2, "North");

		JScrollPane scrollPaneArbre2 = new JScrollPane();
		panelArbre2.add(scrollPaneArbre2, "Center");
		this.panelDessinArbre2 = new DessinHuffman();
		scrollPaneArbre2.setViewportView(this.panelDessinArbre2);

		JPanel panelBoutonArbre2 = new JPanel();
		panelArbre2.add(panelBoutonArbre2, "South");

		JButton btnCrerDepuisTexte2 = new JButton("Créer depuis Texte Clair");
		btnCrerDepuisTexte2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					AppliHuffmanDifference.this.codage2 = new Huffman(AppliHuffmanDifference.this.textAreaClair.getText());
					AppliHuffmanDifference.this.panelDessinArbre2.setCodage(AppliHuffmanDifference.this.codage2);
					StringBuffer sDico = new StringBuffer();
					Map<Character, String> dico = AppliHuffmanDifference.this.codage2.getDictionnaire();
					Iterator var5 = dico.keySet().iterator();

					while(var5.hasNext()) {
						Character c = (Character)var5.next();
						sDico.append(c).append(" : ").append((String)dico.get(c)).append('\n');
					}

					AppliHuffmanDifference.this.textAreaDico2.setText(sDico.toString());
					AppliHuffmanDifference.this.message("Codage créé (" + dico.size() + " caractères)", Color.BLACK);
					AppliHuffmanDifference.this.btnCoder2.setEnabled(true);
					AppliHuffmanDifference.this.btnDcoder2.setEnabled(true);
					if (AppliHuffmanDifference.this.codage1 != null) {
						AppliHuffmanDifference.this.creeCodage3();
					}
				} catch (IllegalArgumentException var6) {
					AppliHuffmanDifference.this.message("Impossible de créer le codage : " + var6.getMessage(), Color.RED);
				}

			}
		});
		panelBoutonArbre2.add(btnCrerDepuisTexte2);

		JPanel panelCodage3 = new JPanel();
		panelCodages.add(panelCodage3);
		panelCodage3.setLayout(new BorderLayout(0, 0));

		JPanel panelDico3 = new JPanel();
		panelCodage3.add(panelDico3, "East");
		panelDico3.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelDico3.setLayout(new BorderLayout(0, 0));

		JLabel lblDico3 = new JLabel("Dictionnaire");
		lblDico3.setFont(new Font("Tahoma", 1, 14));
		lblDico3.setHorizontalAlignment(0);
		panelDico3.add(lblDico3, "North");

		JScrollPane scrollPaneDico3 = new JScrollPane();
		scrollPaneDico3.setViewportBorder(new SoftBevelBorder(1, (Color)null, (Color)null, (Color)null, (Color)null));
		panelDico3.add(scrollPaneDico3, "Center");

		this.textAreaDico3 = new JTextArea();
		scrollPaneDico3.setViewportView(this.textAreaDico3);

		JPanel panelArbre3 = new JPanel();
		panelCodage3.add(panelArbre3, "Center");
		panelArbre3.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelArbre3.setLayout(new BorderLayout(0, 0));

		JLabel lblArbre3 = new JLabel("Arbre");
		lblArbre3.setFont(new Font("Tahoma", 1, 14));
		lblArbre3.setHorizontalAlignment(0);
		panelArbre3.add(lblArbre3, "North");

		JScrollPane scrollPaneArbre3 = new JScrollPane();
		panelArbre3.add(scrollPaneArbre3, "Center");
		this.panelDessinArbre3 = new DessinHuffman();
		scrollPaneArbre3.setViewportView(this.panelDessinArbre3);

		JLabel lblCodage3 = new JLabel("Codage Différence");
		lblCodage3.setHorizontalAlignment(0);
		lblCodage3.setFont(new Font("Tahoma", 1, 16));
		panelCodage3.add(lblCodage3, "North");

		JPanel panelTextes = new JPanel();
		panelTextes.setBorder((Border)null);
		panelCentre.add(panelTextes);
		panelTextes.setLayout(new GridLayout(0, 1, 0, 0));

		JPanel panelClair = new JPanel();
		panelClair.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelTextes.add(panelClair);
		panelClair.setLayout(new BorderLayout(0, 0));

		JLabel lblClair = new JLabel("Texte clair");
		lblClair.setFont(new Font("Tahoma", 1, 14));
		panelClair.add(lblClair, "North");

		JPanel panelBoutonsClair = new JPanel();
		FlowLayout flowLayout = (FlowLayout)panelBoutonsClair.getLayout();
		flowLayout.setAlignment(2);
		panelClair.add(panelBoutonsClair, "South");

		this.btnCoder1 = new JButton("Codage 1");
		this.btnCoder1.setEnabled(false);
		this.btnCoder1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AppliHuffmanDifference.this.verifCodage(AppliHuffmanDifference.this.codage1);

				try {
					String res = AppliHuffmanDifference.this.codage1.code(AppliHuffmanDifference.this.textAreaClair.getText());
					AppliHuffmanDifference.this.textAreaCode.setText(res);
					AppliHuffmanDifference.this.statut();
				} catch (CaractereInconnuException var3) {
					AppliHuffmanDifference.this.message("Impossible de coder : au moins un caractère est absent du codage.", Color.RED);
				}

			}
		});

		JLabel lblCoderAvec = new JLabel("Coder avec");
		lblCoderAvec.setFont(new Font("Tahoma", 1, 12));
		panelBoutonsClair.add(lblCoderAvec);
		panelBoutonsClair.add(this.btnCoder1);

		this.btnCoder2 = new JButton("Codage 2");
		this.btnCoder2.setEnabled(false);
		this.btnCoder2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AppliHuffmanDifference.this.verifCodage(AppliHuffmanDifference.this.codage2);

				try {
					String res = AppliHuffmanDifference.this.codage2.code(AppliHuffmanDifference.this.textAreaClair.getText());
					AppliHuffmanDifference.this.textAreaCode.setText(res);
					AppliHuffmanDifference.this.statut();
				} catch (CaractereInconnuException var3) {
					AppliHuffmanDifference.this.message("Impossible de coder : au moins un caractère est absent du codage.", Color.RED);
				}

			}
		});
		panelBoutonsClair.add(this.btnCoder2);

		this.btnCoder3 = new JButton("Codage Différence");
		this.btnCoder3.setEnabled(false);
		this.btnCoder3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AppliHuffmanDifference.this.verifCodage(AppliHuffmanDifference.this.codage3);

				try {
					String res = AppliHuffmanDifference.this.codage3.code(AppliHuffmanDifference.this.textAreaClair.getText());
					AppliHuffmanDifference.this.textAreaCode.setText(res);
					AppliHuffmanDifference.this.statut();
				} catch (CaractereInconnuException var3) {
					AppliHuffmanDifference.this.message("Impossible de coder : au moins un caractère est absent du codage.", Color.RED);
				}

			}
		});
		panelBoutonsClair.add(this.btnCoder3);

		JScrollPane scrollPaneClair = new JScrollPane();
		scrollPaneClair.setViewportBorder(new SoftBevelBorder(1, (Color)null, (Color)null, (Color)null, (Color)null));
		panelClair.add(scrollPaneClair, "Center");

		this.textAreaClair = new JTextArea();
		scrollPaneClair.setViewportView(this.textAreaClair);

		JPanel panelCode = new JPanel();
		panelCode.setBorder(new EtchedBorder(1, (Color)null, (Color)null));
		panelTextes.add(panelCode);
		panelCode.setLayout(new BorderLayout(0, 0));

		JLabel lblTexteCod = new JLabel("Texte codé");
		lblTexteCod.setFont(new Font("Tahoma", 1, 14));
		panelCode.add(lblTexteCod, "North");

		JPanel panelBoutonsCode = new JPanel();
		FlowLayout flowLayout_1 = (FlowLayout)panelBoutonsCode.getLayout();
		flowLayout_1.setAlignment(2);
		panelCode.add(panelBoutonsCode, "South");

		this.btnDcoder1 = new JButton("Codage 1");
		this.btnDcoder1.setEnabled(false);
		this.btnDcoder1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AppliHuffmanDifference.this.verifCodage(AppliHuffmanDifference.this.codage1);

				try {
					String res = AppliHuffmanDifference.this.codage1.decode(AppliHuffmanDifference.this.textAreaCode.getText());
					AppliHuffmanDifference.this.textAreaClair.setText(res);
					AppliHuffmanDifference.this.statut();
				} catch (FinDeTexteInattendueException var3) {
					AppliHuffmanDifference.this.message("Impossible de décoder : fin de texte inattendue.", Color.RED);
				}

			}
		});

		JLabel lblDcoderAvec = new JLabel("Décoder avec");
		lblDcoderAvec.setFont(new Font("Tahoma", 1, 12));
		panelBoutonsCode.add(lblDcoderAvec);
		panelBoutonsCode.add(this.btnDcoder1);

		this.btnDcoder2 = new JButton("Codage 2");
		this.btnDcoder2.setEnabled(false);
		this.btnDcoder2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AppliHuffmanDifference.this.verifCodage(AppliHuffmanDifference.this.codage2);

				try {
					String res = AppliHuffmanDifference.this.codage2.decode(AppliHuffmanDifference.this.textAreaCode.getText());
					AppliHuffmanDifference.this.textAreaClair.setText(res);
					AppliHuffmanDifference.this.statut();
				} catch (FinDeTexteInattendueException var3) {
					AppliHuffmanDifference.this.message("Impossible de décoder : fin de texte inattendue.", Color.RED);
				}

			}
		});
		panelBoutonsCode.add(this.btnDcoder2);

		this.btnDcoder3 = new JButton("Codage Différence");
		this.btnDcoder3.setEnabled(false);
		this.btnDcoder3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				AppliHuffmanDifference.this.verifCodage(AppliHuffmanDifference.this.codage3);

				try {
					String res = AppliHuffmanDifference.this.codage3.decode(AppliHuffmanDifference.this.textAreaCode.getText());
					AppliHuffmanDifference.this.textAreaClair.setText(res);
					AppliHuffmanDifference.this.statut();
				} catch (FinDeTexteInattendueException var3) {
					AppliHuffmanDifference.this.message("Impossible de décoder : fin de texte inattendue.", Color.RED);
				}

			}
		});
		panelBoutonsCode.add(this.btnDcoder3);

		JScrollPane scrollPaneCode = new JScrollPane();
		scrollPaneCode.setViewportBorder(new SoftBevelBorder(1, (Color)null, (Color)null, (Color)null, (Color)null));
		panelCode.add(scrollPaneCode, "Center");

		this.textAreaCode = new JTextArea();
		scrollPaneCode.setViewportView(this.textAreaCode);
	}

	private void message(String texte, Color col) {
		this.lblMessage.setForeground(col);
		this.lblMessage.setText(texte);
	}

	private void statut() {
		int lgClair = this.textAreaClair.getText().length();
		String stat = "Texte clair : " + lgClair + "caractères = " + lgClair * 16 + " bits / texte codé : ";
		stat = stat + this.textAreaCode.getText().length() + " bits.";
		this.message(stat, Color.BLACK);
	}

	private void verifCodage(Huffman codage) {
		if (codage == null) {
			this.message("Ce codage n'a pas été créé !", Color.RED);
		}

	}

	private void creeCodage3() {
		try {
			this.codage3 = this.codage1.difference(this.codage2);
			this.panelDessinArbre3.setCodage(this.codage3);
			StringBuffer sDico = new StringBuffer();
			Map<Character, String> dico = this.codage3.getDictionnaire();
			Iterator var4 = dico.keySet().iterator();

			while(var4.hasNext()) {
				Character c = (Character)var4.next();
				sDico.append(c).append(" : ").append((String)dico.get(c)).append('\n');
			}

			this.textAreaDico3.setText(sDico.toString());
			this.btnCoder3.setEnabled(true);
			this.btnDcoder3.setEnabled(true);
		} catch (RuntimeException var5) {
			var5.printStackTrace();
			this.message("Impossible de créer le codage différence", Color.RED);
		}

	}
}