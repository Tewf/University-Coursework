package TD5;

public class Test {
	public static void main(String[] args){
		Expression one = new Entier(1);
		Expression two = new Entier(2);
		Expression three = new Entier(3);
		Expression four = new Entier(4);
		Expression six = new Entier(6);
		Expression five = new Entier(5);

		// (+1+2)
		Expression plusOne = new OperationUnaire(one, "+");
		Expression left = new OperationBinaire(plusOne, two, "+");

		// (3+4)
		Expression threePlusFour = new OperationBinaire(three, four, "+");

		// -(6/5)
		Expression sixDivFive = new OperationBinaire(six, five, "/");
		Expression negSixDivFive = new OperationUnaire(sixDivFive, "-");

		// (3+4) * -(6/5)
		Expression right = new OperationBinaire(threePlusFour, negSixDivFive, "*");

		// (+1+2) - ((3+4) * -(6/5))
		Expression expr = new OperationBinaire(left, right, "-");

		System.out.println("prettyString: " + expr.prettyString());
		System.out.println("toString:     " + expr.toString());
		System.out.println("evaluer:      " + expr.evaluer());
	}
}
