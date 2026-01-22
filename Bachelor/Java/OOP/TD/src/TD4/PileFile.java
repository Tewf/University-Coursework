package TD4;

import java.util.*;

public abstract class PileFile<E> {
AbstractList<E> rep;
public PileFile() {}
public boolean estVide(){
    return rep.isEmpty();
}
public String toString(){
    return "[" + rep.toString() + "]";
}
}