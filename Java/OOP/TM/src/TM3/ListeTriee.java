package TM3;

import java.util.Collection;
import java.util.LinkedList;

/**
 * Une liste TRIÉE de nœuds de l'arbre de Huffman.
 * 
 * Qu'est-ce qu'une liste triée ?
 * C'est comme une file d'attente où les gens sont toujours rangés du plus petit au plus grand !
 * Ici, on range les nœuds du poids le plus LÉGER au poids le plus LOURD.
 * 
 * Pourquoi c'est important ?
 * Pour construire l'arbre de Huffman, on a besoin de toujours prendre les DEUX nœuds les plus légers.
 * Avec une liste triée, ils sont toujours au début de la liste !
 * 
 * Exemple :
 * Si on a des nœuds avec poids 5, 3, 8, 1, 7
 * La liste triée les range : [1, 3, 5, 7, 8]
 * On peut prendre facilement les deux premiers : 1 et 3
 * 
 * Cette classe hérite de LinkedList (une liste chaînée standard de Java)
 * et modifie la méthode add() pour maintenir le tri automatiquement.
 */
public class ListeTriee extends LinkedList<NoeudAbstrait> {
    /**
     * Constructeur qui crée une liste triée vide.
     */
	public ListeTriee() {
        super();  // Appelle le constructeur de LinkedList
    }
	
    /**
     * Constructeur qui crée une liste triée à partir d'une collection de nœuds.
     * 
     * @param c la collection de nœuds à ajouter (sera triée automatiquement)
     */
	public ListeTriee(Collection<? extends NoeudAbstrait> c) {
        super();  // Crée une liste vide
        this.addAll(c); // Ajoute tous les éléments (la méthode addAll les trie)
    }
	
    /**
     * Ajoute un nœud dans la liste EN GARDANT LE TRI.
     * 
     * Comment ça marche ?
     * 1. On parcourt la liste du début à la fin
     * 2. On s'arrête dès qu'on trouve un élément plus lourd que le nœud à insérer
     * 3. On insère le nœud juste avant cet élément
     * 4. Si tous les éléments sont plus légers, on ajoute le nœud à la fin
     * 
     * Exemple :
     * Liste actuelle : [1, 3, 7, 8]
     * On veut ajouter un nœud de poids 5
     * - 5 > 1 ? Oui, on continue
     * - 5 > 3 ? Oui, on continue
     * - 5 > 7 ? Non ! On s'arrête
     * - On insère 5 avant 7
     * - Résultat : [1, 3, 5, 7, 8]
     * 
     * @param n le nœud à ajouter
     * @return true (toujours, car l'ajout réussit toujours)
     */
	public boolean add(NoeudAbstrait n) {
        int i = 0;
        // On parcourt la liste pour trouver la bonne position
        // n.compareTo(get(i)) retourne > 0 si n est plus lourd que get(i)
        // Donc on continue tant que n est plus lourd
        while (i < size() && n.compareTo(get(i)) > 0) {
            i++;  // On avance d'une position
        }
        // On a trouvé la position ! On insère le nœud ici
        // add(i, n) insère n à la position i (décale les autres vers la droite)
        add(i, n);
        return true;  // L'ajout a réussi
    }
	
    /**
     * Ajoute tous les nœuds d'une collection dans la liste EN GARDANT LE TRI.
     * 
     * Cette méthode ajoute les nœuds un par un en utilisant notre méthode add()
     * qui maintient le tri automatiquement.
     * 
     * @param c la collection de nœuds à ajouter
     * @return true si au moins un élément a été ajouté, false sinon
     */
	public boolean addAll(Collection<? extends NoeudAbstrait> c) {
        boolean changed = false;  // Pour savoir si on a modifié la liste
        // On parcourt tous les nœuds de la collection
        for (NoeudAbstrait n : c) {
            // On ajoute chaque nœud avec notre méthode add() qui trie
            if (this.add(n)) {
                changed = true;  // On a ajouté au moins un élément
            }
        }
        return changed;
    }
}


