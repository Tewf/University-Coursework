from pychoco import Model
from typing import List, Optional

class ABCDE:
    """
    If ABCDE times 4 equals EDCBA, and each letter is a different digit from 0 to 9,
    what is the value of each letter?
    <a href="https://mindyourdecisions.com/blog/2023/11/22/abcde-times-4-equals-edcba/">[source]</a>
    """

    def __init__(self):
        """
        A public constructor without parameter.
        """
        self.model = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.E = None
        self.modelling()

    def get_choco_model(self):
        """
        A method that returns the current model.
        <b>Caution</b>: this method should not be modified.
        """
        return self.model

    def modelling(self):
        """
        Method to declare variables and post constraints.
        """
        self.model = Model("ABCDE")

        # declare the variables with their initial domain
        self.A = self.model.intvar(0, 9, "A")
        # TODO:
        # declare the other variables by copying and pasting the code for A
        # self.B = ...
        # self.C = ...
        # self.D = ...
        # self.E = ...

        # Constraint 1:
        # "each letter is a different digit from 0 to 9"
        # the second part of the constraint is defined
        # by the domain of each variable
        # REMARK:
        # Calling the `.post()` method is required to activate the constraint
        # TODO:
        
        # Constraint 2:
        # "ABCDE times 4 equals EDCBA"
        # declare the 2nd constraint using the `scalar` constraint
        # https://choco-solver.org/docs/modeling/intconstraints/#sum-and-scalar
        # Don't forget to post it
        
    def next_solution(self) -> Optional[List[int]]:
        """
        Return the next solution found as a list of int.
        The elements are, in order of declaration: A, B, C, D, E.
        If no solution is found, return None.
        <b>Caution</b>: this method should not be modified.
        """
        solver = self.model.get_solver()
        if solver.solve():
            return [
                self.A.get_value(),
                self.B.get_value(),
                self.C.get_value(),
                self.D.get_value(),
                self.E.get_value()
            ]
        else:
            return None

def main() -> None:
    print("A first puzzle with Choco-solver")
    pb = ABCDE()
    print("Run solving step")
    solution = pb.next_solution()
    if solution is not None:
        A, B, C, D, E = solution
        print(f" {A}{B}{C}{D}{E}")
        print("x    4")
        print("------")
        print(f" {E}{D}{C}{B}{A}")
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
