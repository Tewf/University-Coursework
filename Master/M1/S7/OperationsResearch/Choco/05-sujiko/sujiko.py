from pychoco import Model
from typing import List, Optional


class Sujiko:
    """
    Sujiko is a logic-based, combinatorial number-placement puzzle created by Jai Gomer of Kobayaashi Studios.
    <p>
    The puzzle takes place on a 3x3 grid with four circled number clues
    at the centre of each quadrant which indicate the sum of the four numbers in that quadrant.
    The numbers 1-9 must be placed in the grid, in accordance with the circled clues, to complete the puzzle.
    """

    def __init__(self, circles: List[int] = None, clues: List[int] = None):
        """
        Build a Sujiko puzzle with default clues,
        or from given `circles` and `clues`.
        """
        if circles is None:
            # default clues {NW, NE, SW, SE}
            circles = [10, 21, 18, 20]
        if clues is None:
            # default clues {NW, N, NE, W, C, E, SW, S, SE}
            clues = [0, 0, 0, 0, 0, 0, 8, 0, 7]
        self.circles = circles
        self.clues = clues
        self.model = None
        # TODO: rajouter self.grid comme matrice 3x3 de variables IntVar
        self.modelling()

    def get_model(self) -> Model:
        """
        Public accessor.
        """
        return self.model

    def modelling(self) -> None:
        """
        Modelling of the problem.
        """
        # TODO: create the model
        # self.model = ...

        # TODO: declare the 3x3 grid of variables

        # Constraint 1: "The numbers 1-9 must be placed in the grid"
        # implies that all values must be different
        # TODO: flatten the grid and post all_different

        # Constraint 2: "each quadrant which indicate the sum of the four numbers in that quadrant"
        # TODO

        # Constraint 3: "the clues"
        # TODO

    @staticmethod
    def quadrant(grid, i: int) -> List["IntVar"]:
        """
        Returns the four variables in the i-th quadrant (NW, NE, SW, SE).
        """
        x = i // 2
        y = i % 2
        return [
            grid[x][y],
            grid[x + 1][y],
            grid[x][y + 1],
            grid[x + 1][y + 1],
        ]

    def next_solution(self) -> Optional[List[int]]:
        """
        Return the next solution found as array of int of length 9
        that represents the 3x3 flattened grid.
        If no solution is found, return None.
        """
        solver = self.model.get_solver()
        if solver.solve():
            # TODO: replace 0s by the actual values from self.grid
            # and return a flat list of 9 integers.
            flat = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            return flat
        else:
            return None
