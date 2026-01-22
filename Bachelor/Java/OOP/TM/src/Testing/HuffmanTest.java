package Testing;

import TM3.CaractereInconnuException;
import TM3.FinDeTexteInattendueException;
import TM3.Huffman;

public class HuffmanTest {
    public static void main(String[] args) throws Exception {
        String texte = "exemple de text pour codage huffman";
        Huffman h = new Huffman(texte);
        try {
            String code = h.code(texte);
            String decoded = h.decode(code);
            System.out.println("Original: " + texte);
            System.out.println("Decoded : " + decoded);
            System.out.println("Match   : " + texte.equals(decoded));
        } catch (CaractereInconnuException | FinDeTexteInattendueException e) {
            e.printStackTrace();
        }
    }
}
