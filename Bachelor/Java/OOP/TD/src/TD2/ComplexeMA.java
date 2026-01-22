package TD2;

public class ComplexeMA extends Complexe {
    private double module, argument;

    public ComplexeMA(double module, double argument) {
        this.module = module;
        this.argument = argument;
    }

    public ComplexeMA(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        this.module = c.getMod();
        this.argument = c.getArg();
    }

    @Override
    public double getReel() { return module * Math.cos(argument); }

    @Override
    public double getImaginaire() { return module * Math.sin(argument); }

    @Override
    public double getMod() { return module; }

    @Override
    public double getArg() { return argument; }

    @Override
    public Complexe plus(Complexe c) { return new ComplexeRI(this.getReel() + c.getReel(), this.getImaginaire() + c.getImaginaire()); }

    @Override
    public Complexe moins(Complexe c) { return new ComplexeRI(this.getReel() - c.getReel(), this.getImaginaire() - c.getImaginaire()); }

    @Override
    public Complexe multipliePar(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        double newMod = this.module * c.getMod();
        double newArg = this.argument + c.getArg();
        return new ComplexeMA(newMod, newArg);
    }

    @Override
    public Complexe divisePar(Complexe c) {
        if (c == null) throw new NullPointerException("c is null");
        double denom = c.getMod();
        if (denom == 0.0) throw new ArithmeticException("division by zero (complex)");
        double newMod = this.module / denom;
        double newArg = this.argument - c.getArg();
        return new ComplexeMA(newMod, newArg);
    }

    @Override
    public Complexe conjugue() { return new ComplexeMA(module, -argument); }

    @Override
    public Complexe puissance(double x) {
        if (module == 0.0 && x <= 0.0) throw new ArithmeticException("0 to non-positive power");
        double nr = Math.pow(module, x);
        double na = argument * x;
        return new ComplexeMA(nr, na);
    }

    @Override
    public Complexe ln() {
        if (module <= 0.0) throw new ArithmeticException("log undefined for non-positive modulus");
        return new ComplexeRI(Math.log(module), argument);
    }

    @Override
    public String toString() {
        return String.format("%f * exp(i%f)", module, argument);
    }
}
