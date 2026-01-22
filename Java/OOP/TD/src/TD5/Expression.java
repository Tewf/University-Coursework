package TD5;

/**
 * Abstract base class for all arithmetic expressions used in TD5.
 *
 * Subclasses must implement evaluation, cloning, textual representations
 * and a simple layout algorithm (calculRect) used for visualising the
 * expression tree. The class also provides layout constants used by
 * children when computing subtree bounding rectangles.
 */
public abstract class Expression implements Cloneable {

    /** Create an (empty) expression. Subclasses set specific state. */
    public Expression() {}

    /**
     * Evaluate the expression and return an integer result.
     *
     * @return the integer value of this expression
     */
    public abstract int evaluer();

    /**
     * Produce a deep copy of this expression.
     * Implementations typically return an instance of the concrete type.
     *
     * @return a clone of this expression (type: Expression, returned as Object
     *         to respect the {@code Cloneable} signature)
     */
    @Override
    public abstract Object clone();

    /**
     * Compact textual representation used for debugging (S-expression-like).
     */
    @Override
    public abstract String toString();

    /**
     * Human-friendly infix representation with minimal parentheses.
     * Subclasses should add parentheses only when needed according to
     * operator priorities.
     */
    public abstract String prettyString();

    /**
     * Return operator priority for pretty-printing and parenthesization.
     * Higher numbers bind tighter (higher precedence).
     */
    public abstract int getPriorite();

    // layout constants used by calculRect implementations
    protected static final int NODE_WIDTH = 40;
    protected static final int NODE_HEIGHT = 20;
    protected static final int H_GAP = 10;
    protected static final int V_GAP = 20;

    /**
     * Compute a bounding rectangle for the subtree rooted at this expression.
     * The rectangle's x,y represent the top-left of the subtree; width/height
     * must enclose the node box and its children. Implementations may call
     * child.calculRect(...) to compute child layout.
     *
     * @param x requested left coordinate for the subtree
     * @param y requested top coordinate for the subtree
     * @return a {@link Rectangle} describing the subtree layout
     */
    public abstract Rectangle calculRect(int x, int y);

    /**
     * Structural equality: subclasses should compare type and relevant fields.
     */
    @Override
    public abstract boolean equals(Object obj);
}