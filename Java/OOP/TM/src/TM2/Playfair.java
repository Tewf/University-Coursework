package TM2;

public class Playfair extends Cryptage {
	private char[][] matrice; // 6x6

	public Playfair(String clef) {
		super(clef);
		construireMatrice();
	}

	private void construireMatrice() {
	    StringBuilder unique = new StringBuilder();

	    // 1. Ajoute les lettres uniques de la clé
	    for (int i = 0; i < clef.length(); i++) {
	        char c = clef.charAt(i);
	        if (unique.indexOf(String.valueOf(c)) == -1 && ALPHABET.indexOf(c) != -1) {
	            unique.append(c);
	        }
	    }

	    // 2. Ajoute le reste de l'alphabet
	    for (int i = 0; i < ALPHABET.length(); i++) {
	        char c = ALPHABET.charAt(i);
	        if (unique.indexOf(String.valueOf(c)) == -1) {
	            unique.append(c);
	        }
	    }

	    // 3. Remplit la matrice 6x6
	    matrice = new char[6][6];
	    int index = 0;
	    for (int i = 0; i < 6; i++) {
	        for (int j = 0; j < 6; j++) {
	            matrice[i][j] = unique.charAt(index);
	            index++;
	        }
	    }
	}
	
	
	private int[] position(char c) {
		// renvoie {ligne, colonne} du caractère c dans la matrice
		for (int i = 0;i < matrice.length; i++) {
			for (int j = 0;j < matrice[i].length;j++) {
				if (matrice[i][j] == c) {
					return new int[]{i, j};
				}
			}
		}
		return null;
	}


	@Override
	public String cryptage(String texte) {
	    StringBuilder rep = new StringBuilder();

	    int i = 0;
	    while (i < texte.length()) {
	        char c1 = texte.charAt(i);
	        char c2;

	        // Si c’est le dernier caractère, on le laisse tel quel
	        if (i + 1 < texte.length()) {
	            c2 = texte.charAt(i + 1);
	        } else {
	            rep.append(c1);
	            break;
	        }

	        int[] pos1 = position(c1);
	        int[] pos2 = position(c2);

	        // Si un des deux n'est pas dans l'alphabet
	        if (pos1 == null || pos2 == null) {
	            rep.append(c1).append(c2);
	        } 
	        // Même ligne
	        else if (pos1[0] == pos2[0]) {
	            rep.append(matrice[pos1[0]][(pos1[1] + 1) % 6]);
	            rep.append(matrice[pos2[0]][(pos2[1] + 1) % 6]);
	        }
	        // Même colonne
	        else if (pos1[1] == pos2[1]) {
	            rep.append(matrice[(pos1[0] + 1) % 6][pos1[1]]);
	            rep.append(matrice[(pos2[0] + 1) % 6][pos2[1]]);
	        }
	        // Rectangle
	        else {
	            rep.append(matrice[pos1[0]][pos2[1]]);
	            rep.append(matrice[pos2[0]][pos1[1]]);
	        }

	        i += 2; // passer au couple suivant
	    }

	    return rep.toString();
	}
	

	@Override
	public String deCryptage(String texte) {
	    StringBuilder rep = new StringBuilder();

	    int i = 0;
	    while (i < texte.length()) {
	        char c1 = texte.charAt(i);
	        char c2;

	        if (i + 1 < texte.length()) {
	            c2 = texte.charAt(i + 1);
	        } else {
	            rep.append(c1);
	            break;
	        }

	        int[] pos1 = position(c1);
	        int[] pos2 = position(c2);

	        if (pos1 == null || pos2 == null) {
	            rep.append(c1).append(c2);
	        }
	        // Même ligne → aller à gauche
	        else if (pos1[0] == pos2[0]) {
	            rep.append(matrice[pos1[0]][(pos1[1] + 5) % 6]);
	            rep.append(matrice[pos2[0]][(pos2[1] + 5) % 6]);
	        }
	        // Même colonne → aller en haut
	        else if (pos1[1] == pos2[1]) {
	            rep.append(matrice[(pos1[0] + 5) % 6][pos1[1]]);
	            rep.append(matrice[(pos2[0] + 5) % 6][pos2[1]]);
	        }
	        // Rectangle (même principe)
	        else {
	            rep.append(matrice[pos1[0]][pos2[1]]);
	            rep.append(matrice[pos2[0]][pos1[1]]);
	        }

	        i += 2;
	    }

	    return rep.toString();
	}

	@Override
	public String toString() {
	    StringBuilder sb = new StringBuilder();
	    sb.append("Cryptage Playfair\n");
	    sb.append("Mot Clef : ").append(clef).append("\n");
	    sb.append("Matrice de cryptage :\n");

	    for (int i = 0; i < 6; i++) {
	        for (int j = 0; j < 6; j++) {
	            sb.append(matrice[i][j]).append(" ");
	        }
	        sb.append("\n");
	    }

	    return sb.toString();
	}
}