package TD4;

public class Tache implements Priorisable {
    private String description;
    private int priorite;

    public Tache(String description, int priorite) {
        this.description = description;
        this.priorite = priorite;
    }

    @Override
    public int getPriorite() {
        return priorite;
    }

    @Override
    public String toString() {
        return "Tache{" +
                "description='" + description + '\'' +
                ", priorite=" + priorite +
                '}';
    }

}
