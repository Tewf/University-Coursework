package TD5;

/**
 * Represents a unary operation (for example negation) with a single operand.
 */
class OperationUnaire extends Expression {
    protected String op;
    protected Expression gauche;

    /**
     * Create a unary operation with operand {@code g} and operator {@code op}.
     * Typical operators: "-" (negation) or "+" (unary plus).
     */
    public OperationUnaire(Expression g, String op) {
        this.gauche = g;
        this.op = op;
    }

    @Override
    public int getPriorite() {
        // Unary operators bind tighter than binary +,- but weaker than literals
        return 3;
    }

    @Override
    public String toString() {
        return "(" + op + gauche.toString() + ")";
    }

    @Override
    public String prettyString() {
        String gStr = gauche.prettyString();
        if (gauche.getPriorite() < this.getPriorite()) {
            gStr = "(" + gStr + ")";
        }
        return op + gStr;
    }

    @Override
    public int evaluer() {
        if (op.equals("-")) return -gauche.evaluer();
        else return gauche.evaluer();
    }

    @Override
    public Object clone() {
        return new OperationUnaire((Expression) gauche.clone(), op);
    }

    @Override
    public Rectangle calculRect(int x, int y) {
        // Compute child rectangle positioned below this node
        // First, compute child's layout using its own calculRect with provisional x=0;
        Rectangle childRect = gauche.calculRect(0, 0);

        // subtree width is max(node width, child width)
        int subtreeWidth = Math.max(NODE_WIDTH, childRect.width);

        // center child under the node
        int childX = x + (subtreeWidth - childRect.width) / 2;
        int childY = y + NODE_HEIGHT + V_GAP;

        // recompute child's rectangle at the chosen position
        childRect = gauche.calculRect(childX, childY);

        int totalHeight = NODE_HEIGHT + V_GAP + childRect.height;

        return new Rectangle(x, y, subtreeWidth, totalHeight);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        OperationUnaire other = (OperationUnaire) obj;
        if (this.op == null) {
            if (other.op != null) return false;
        } else if (!this.op.equals(other.op)) return false;
        if (this.gauche == null) {
            return other.gauche == null;
        }
        return this.gauche.equals(other.gauche);
    }
}