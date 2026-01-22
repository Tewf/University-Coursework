package TD3;

public class ListeVide extends Liste {
    public ListeVide() {}

    @Override
    public String toString() { return "[]"; }

    @Override
    public boolean equals(Object obj) { return obj instanceof ListeVide; }
}
