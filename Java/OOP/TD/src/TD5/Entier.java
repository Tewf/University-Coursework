package TD5;

/**
 * Represents an integer literal in an expression tree.
 */
class Entier extends Expression {
    /** The integer value stored by this literal. */
    protected int val;

    /**
     * Construct an integer literal with value {@code v}.
     *
     * @param v the integer value
     */
    public Entier(int v) {
        this.val = v;
    }

    @Override
    public int getPriorite() {
        // Highest precedence: literal never needs parentheses
        return 4;
    }

    @Override
    public String toString() {
        return Integer.toString(val);
    }

    @Override
    public String prettyString() {
        return toString();
    }

    @Override
    public int evaluer() {
        return val;
    }

    @Override
    public Object clone() {
        return new Entier(val);
    }

    @Override
    public Rectangle calculRect(int x, int y) {
        // Leaf node: box of fixed size at (x,y)
        return new Rectangle(x, y, NODE_WIDTH, NODE_HEIGHT);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Entier other = (Entier) obj;
        return this.val == other.val;
    }
}
