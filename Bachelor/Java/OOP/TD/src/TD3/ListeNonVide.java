package TD3;

public class ListeNonVide extends Liste {
    private Terme tete;
    private Liste queue;

    public ListeNonVide(Terme tete, Liste queue) { this.tete = tete; this.queue = queue; }

    public ListeNonVide(Terme tete, Variable queueVar) {
        this.tete = tete;
        if (queueVar == null) throw new IllegalArgumentException("queue variable required");
        Terme v = queueVar.getValeur();
        if (v == null) this.queue = null;
        else if (v instanceof Liste) this.queue = (Liste) v;
        else throw new IllegalArgumentException("variable's value must be a Liste");
    }

    @Override
    public String toString() {
        // produce [a, b, c] style
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        sb.append(tete.toString());
        Liste cur = queue;
        while (cur instanceof ListeNonVide) {
            ListeNonVide ln = (ListeNonVide) cur;
            sb.append(", ");
            sb.append(ln.tete.toString());
            cur = ln.queue;
        }
        if (cur instanceof ListeVide) {
            // end
        } else if (cur != null) {
            sb.append("|" + cur.toString());
        }
        sb.append(']');
        return sb.toString();
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof ListeNonVide)) return false;
        ListeNonVide o = (ListeNonVide) obj;
        if (!this.tete.equals(o.tete)) return false;
        if (this.queue == null && o.queue == null) return true;
        if (this.queue == null || o.queue == null) return false;
        return this.queue.equals(o.queue);
    }
}
