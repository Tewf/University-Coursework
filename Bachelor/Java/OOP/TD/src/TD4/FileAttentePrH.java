package TD4;

public class FileAttentePrH<E extends Priorisable> extends FileAttente<E>{
	/**
	 * Enfile (insert) an element into the heap.
	 * We append the element at the end of the array and then "heapify up"
	 * to restore the max-heap property (parent.priority >= children.priority).
	 */
	public void enfiler(E e){
		java.util.ArrayList<E> a = (java.util.ArrayList<E>) rep;
		a.add(e); // put at the end
		heapifyUp(a.size() - 1);
	}

	/**
	 * Defile (remove) and return the element with highest priority.
	 * Removes the root of the max-heap (index 0). To keep the tree compact
	 * we move the last element to the root, remove the last slot, then
	 * "heapify down" from the root to restore the heap property.
	 */
	public E defiler(){
		if(estVide()){
			throw new PileFileException("File vide");
		}
		java.util.ArrayList<E> a = (java.util.ArrayList<E>) rep;
		// root to return
		E root = a.get(0);
		int last = a.size() - 1;
		if(last == 0){
			// only one element
			a.remove(last);
			return root;
		}
		// move last to root and remove last
		a.set(0, a.get(last));
		a.remove(last);
		heapifyDown(0);
		return root;
	}

	/**
	 * Return (peek) the element with highest priority without removing it.
	 */
	public E premier(){
		if(estVide()){
			throw new PileFileException("File vide");
		}
		java.util.ArrayList<E> a = (java.util.ArrayList<E>) rep;
		return a.get(0);
	}

	/* ----------------- Heap helper methods ----------------- */

	// Return index of parent
	private int parent(int i){
		return (i - 1) / 2;
	}

	// Return index of left child
	private int left(int i){
		return 2 * i + 1;
	}

	// Return index of right child
	private int right(int i){
		return 2 * i + 2;
	}

	// Swap two elements in the underlying ArrayList
	private void swap(int i, int j){
		java.util.ArrayList<E> a = (java.util.ArrayList<E>) rep;
		E tmp = a.get(i);
		a.set(i, a.get(j));
		a.set(j, tmp);
	}

	// Move the element at index 'i' upward until heap property holds
	private void heapifyUp(int i){
		java.util.ArrayList<E> a = (java.util.ArrayList<E>) rep;
		int idx = i;
		while(idx > 0){
			int p = parent(idx);
			if(a.get(idx).getPriorite() > a.get(p).getPriorite()){
				swap(idx, p);
				idx = p;
			} else {
				break;
			}
		}
	}

	// Move the element at index 'i' downward until heap property holds
	private void heapifyDown(int i){
		java.util.ArrayList<E> a = (java.util.ArrayList<E>) rep;
		int n = a.size();
		int idx = i;
		while(true){
			int l = left(idx);
			int r = right(idx);
			int largest = idx;
			if(l < n && a.get(l).getPriorite() > a.get(largest).getPriorite()){
				largest = l;
			}
			if(r < n && a.get(r).getPriorite() > a.get(largest).getPriorite()){
				largest = r;
			}
			if(largest != idx){
				swap(idx, largest);
				idx = largest;
			} else {
				break;
			}
		}
	}

}

