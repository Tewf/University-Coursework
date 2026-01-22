package TD4;
import java.util.*;
public class Pile<E> extends PileFile<E>{
public Pile () {
rep = new ArrayList<E>();
}
public void empiler(E e){
    rep.add(e);
}
public E depiler(){
    if(estVide()){
        throw new PileFileException("Pile vide");
    }
    return rep.remove(rep.size()-1);
}
public E sommet(){
    if(estVide()){
        throw new PileFileException("Pile vide");
    }
    return rep.get(rep.size()-1);
}
}
