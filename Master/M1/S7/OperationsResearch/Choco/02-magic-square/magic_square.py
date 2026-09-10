from typing import List
from pychoco import Model

Solution = List[List[int]]


class MagicSquarePychoco:
    def __init__(self, n: int) -> None:
        """Construct an instance of the magic square problem of size n."""
        #TODO

    def create_model(self) -> Model:
        """Create the model of the problem instance."""
        #TODO

    def solve(self) -> Solution:
        """"Solve the instance of magic square and return one solution."""
        #TODO

    def sol_enumeration(self) -> List[Solution]:
        """Enumerate and return all solutions."""
        #TODO

    def print_solution(self) -> None:
        """Print the solution of the problem."""
        #TODO


if __name__ == "__main__":
    magic = MagicSquarePychoco(4)
    #TODO  
    # ex: magic.solve() 
    # magic.print_solution()