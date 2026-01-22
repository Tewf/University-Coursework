package TD2;

public class ComplexeRI extends Complexe {
    private double reel, imaginaire;

    public ComplexeRI(double reel, double imaginaire) {
        this.reel = reel;
        this.imaginaire = imaginaire;
    }

    public ComplexeRI(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        this.reel = c.getReel();
        this.imaginaire = c.getImaginaire();
    }

    @Override
    public double getReel() { return reel; }

    @Override
    public double getImaginaire() { return imaginaire; }

    @Override
    public double getMod() { return Math.hypot(reel, imaginaire); }

    @Override
    public double getArg() { return Math.atan2(imaginaire, reel); }

    @Override
    public Complexe plus(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        return new ComplexeRI(this.reel + c.getReel(), this.imaginaire + c.getImaginaire());
    }

    @Override
    public Complexe moins(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        return new ComplexeRI(this.reel - c.getReel(), this.imaginaire - c.getImaginaire());
    }

    @Override
    public Complexe multipliePar(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        double a = this.reel, b = this.imaginaire;
        double c2 = c.getReel(), d = c.getImaginaire();
        return new ComplexeRI(a * c2 - b * d, a * d + b * c2);
    }

    @Override
    public Complexe divisePar(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        double a = this.reel, b = this.imaginaire;
        double c2 = c.getReel(), d = c.getImaginaire();
        double denom = c2 * c2 + d * d;
        if (denom == 0.0) throw new ArithmeticException("division by zero (complex)");
        return new ComplexeRI((a * c2 + b * d) / denom, (b * c2 - a * d) / denom);
    }

    @Override
    public Complexe conjugue() { return new ComplexeRI(reel, -imaginaire); }

    @Override
    public Complexe puissance(double x) {
        double r = getMod();
        double theta = getArg();
        double nr = Math.pow(r, x);
        double na = theta * x;
        if (r == 0.0 && x <= 0.0) throw new ArithmeticException("0 to non-positive power");
        return new ComplexeMA(nr, na);
    }

    @Override
    public Complexe ln() {
        double r = getMod();
        double theta = getArg();
        if (r <= 0.0) throw new ArithmeticException("log undefined for non-positive modulus");
        return new ComplexeRI(Math.log(r), theta);
    }

    @Override
    public String toString() {
        return String.format("(%f%+fi)", reel, imaginaire);
    }
}
