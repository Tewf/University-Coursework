# birthday.py
from pychoco import Model
from typing import List, Optional


class Birthday:
    """
    On my birthday in 2021, my age is equal to the sum of the digits of my birth year.
    I am less than 100 years old. What could my birth year be?
    <a href="https://mindyourdecisions.com/blog/2023/07/03/age-equals-sum-of-birth-year-digits/">[source]</a>
    """

    def __init__(self, year: int = 2021):
        """
        Build a Birthday problem with 2021 as the current year,
        or a given year if provided.
        """
        self.model: Model = None
        self.input_year: int = year
        # Variables des chiffres de l’année de naissance
        self.thousands = None
        self.hundreds = None
        self.tens = None
        self.ones = None
        self.modelling()

    def get_model(self) -> Model:
        """
        <b>Caution:</b> this method should not be modified.
        """
        return self.model

    def get_input_year(self) -> int:
        """
        <b>Caution:</b> this method should not be modified.
        """
        return self.input_year

    def modelling(self) -> None:
        """
        Modelling of the problem.
        """
        # TODO: create the model
        # self.model = ...

        # TODO: declare the variables with their initial domain
        # self.thousands = ...
        # self.hundreds = ...
        # self.tens = ...
        # self.ones = ...

        # Constraint 1: "I am less than 100 years old"
        # TODO: declare age
        
        # Constraint 2:
        # "In 2021, my age is equal to the sum of the digits of my birth year"
        # TODO:
        
    def next_solution(self) -> Optional[List[int]]:
        """
        <b>Caution:</b> this method should not be modified.
        <br/>
        Return the next solution found as an array of int
        with one single int at index 0: the birth year.
        If no solution is found, return None.
        """
        solver = self.model.get_solver()
        if solver.solve():
            # TODO: replace 0 by the correct birth year built from thousands, hundreds, tens, ones
            birth = 0 
            return [birth]
        else:
            return None


def main() -> None:
    print("A second puzzle with Choco-solver")
    pb = Birthday()
    print("Run solving step")
    solution = pb.next_solution()
    if solution is not None:
        birth = solution[0]
        age = pb.get_input_year() - birth
        print(f"My birth year is {birth}")
        print(f"I am {age} years old")
    else:
        print("No solution found")


if __name__ == "__main__":
    main()