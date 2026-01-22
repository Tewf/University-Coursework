package TD4;

public class FileAttentePr<E extends Priorisable> extends FileAttente<E>{
    public E defiler(){
        if(estVide()){
            throw new PileFileException("File vide");
        }
        int indexMax = 0;
        for(int i=1; i<rep.size(); i++){
            if(rep.get(i).getPriorite() > rep.get(indexMax).getPriorite()){
                indexMax = i;
            }
        }
        return rep.remove(indexMax);
    }

}
