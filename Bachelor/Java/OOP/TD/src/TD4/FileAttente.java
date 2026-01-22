package TD4;
import java.util.*;

public class FileAttente<E> extends
PileFile<E> {
public FileAttente() {
rep = new ArrayList<E>();
}
public void enfiler(E e){
    rep.add(0, e);
}
public E defiler(){
    if(estVide()){
        throw new PileFileException("File vide");
    }
    return rep.remove(0);
}
public E premier(){
    if(estVide()){
        throw new PileFileException("File vide");
    }
    return rep.get(rep.size()-1);
}
public E dernier(){
    if(estVide()){
        throw new PileFileException("File vide");
    }
    return rep.get(0);
}
}
