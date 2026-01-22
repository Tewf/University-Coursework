package TM3bis;

import java.util.Collection;
import java.util.LinkedList;


public class ListeTriee extends LinkedList<NoeudAbstrait> {
    
	public ListeTriee() {
        super();  // Appelle le constructeur de LinkedList
    }
	
    
	public ListeTriee(Collection<? extends NoeudAbstrait> c) {
        super();  // Crée une liste vide
        this.addAll(c); // Ajoute tous les éléments (la méthode addAll les trie)
    }
	
  
	public boolean add(NoeudAbstrait n) {
        int i = 0;
        while (i < size() && n.compareTo(get(i)) > 0) {
            i++;  
        }
        
        add(i, n);
        return true;  
    }
	
	public boolean addAll(Collection<? extends NoeudAbstrait> c) {
        boolean changed = false;  // Pour savoir si on a modifié la liste
        for (NoeudAbstrait n : c) {
            if (this.add(n)) {
                changed = true;  
            }
        }
        return changed;
    }
}


