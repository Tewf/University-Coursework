package TD5;

/**
 * Represents a binary operation with a left and right operand.
 * Supported operators: +, -, *, /
 */
class OperationBinaire extends OperationUnaire {
    protected Expression droit;

    /**
     * Construct a binary operation with left {@code g}, right {@code d}
     * and operator {@code op}.
     *
     * @throws IllegalArgumentException for unsupported operators or division by zero
     */
    public OperationBinaire(Expression g, Expression d, String op) {
        super(g, op);
        if (!(op.equals("+") || op.equals("-") || op.equals("*") || op.equals("/"))) {
            throw new IllegalArgumentException("Operateur binaire invalide : " + op);
        }
        if (op.equals("/") && d.evaluer() == 0) {
            throw new IllegalArgumentException("Division par zero");
        }
        this.droit = d;
    }

    @Override
    public int getPriorite() {
        switch (op) {
            case "+":
            case "-":
                return 1;
            case "*":
            case "/":
                return 2;
        }
        return 0;
    }

    @Override
    public String toString() {
        return "(" + op + gauche.toString() + " " + droit.toString() + ")";
    }

    @Override
    public String prettyString() {
        String gStr = gauche.prettyString();
        String dStr = droit.prettyString();

        // Parenthesize left operand when its priority is lower (binds weaker)
        if (gauche.getPriorite() < this.getPriorite()) {
            gStr = "(" + gStr + ")";
        }

        // Parenthesize right operand when:
        // - its priority is lower (binds weaker), or
        // - its priority is equal and the operator is non-associative on the right
        if (droit.getPriorite() < this.getPriorite()
                || (droit.getPriorite() == this.getPriorite() && (op.equals("-") || op.equals("/")))) {
            dStr = "(" + dStr + ")";
        }

        return gStr + " " + op + " " + dStr;
    }

    @Override
    public int evaluer() {
        int gvalue = gauche.evaluer(), dvalue = droit.evaluer();
        if (op.equals("+")) return gvalue + dvalue;
        if (op.equals("-")) return gvalue - dvalue;
        if (op.equals("*")) return gvalue * dvalue;
        if (op.equals("/")) return gvalue / dvalue;
        return 0;
    }

    @Override
    public Object clone() {
        return new OperationBinaire((Expression) gauche.clone(), (Expression) droit.clone(), op);
    }

    @Override
    public Rectangle calculRect(int x, int y) {
        // Compute left subtree layout first (provisionally at x)
        Rectangle leftRect = gauche.calculRect(0, 0);
        Rectangle rightRect = droit.calculRect(0, 0);

        // total width is left + gap + right, at least node width
        int subtreeWidth = Math.max(NODE_WIDTH, leftRect.width + H_GAP + rightRect.width);

        // compute left child x so that the whole subtree starts at x
        int leftX = x + (subtreeWidth - (leftRect.width + H_GAP + rightRect.width)) / 2;
        int rightX = leftX + leftRect.width + H_GAP;

        int childY = y + NODE_HEIGHT + V_GAP;

        // recompute children at chosen positions
        leftRect = gauche.calculRect(leftX, childY);
        rightRect = droit.calculRect(rightX, childY);

        int totalHeight = NODE_HEIGHT + V_GAP + Math.max(leftRect.height, rightRect.height);

        return new Rectangle(x, y, subtreeWidth, totalHeight);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        OperationBinaire other = (OperationBinaire) obj;
        if (this.op == null) {
            if (other.op != null) return false;
        } else if (!this.op.equals(other.op)) return false;
        if (this.gauche == null) {
            if (other.gauche != null) return false;
        } else if (!this.gauche.equals(other.gauche)) return false;
        if (this.droit == null) {
            return other.droit == null;
        }
        return this.droit.equals(other.droit);
    }
}
