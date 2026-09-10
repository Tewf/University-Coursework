from typing import List, Optional
from pychoco import Model

Solution = List[List[bool]]


class NqueensPychoco:
    def __init__(self, n: int) -> None:
        """Construct an instance of the n‑queens problem."""
        self.size: int = n              # data
        self.model: Optional[Model] = None
        self.col: Optional[List["IntVar"]] = None   # colonne de la reine en ligne i
        self.solution: Optional[Solution] = None

    def create_model(self) -> Model:
        """Create the model of the n‑queens problem."""
        #TODO
        pass  # code à remplacer

    def to_solution(self) -> None:
        """Build a solution (boolean board) from the current solver state."""
        #TODO
        # - get the value of each self.col[i]
        # - build self.solution as a boolean matrix:
        #   self.solution[i][col[i]] = True
        pass  # code à remplacer

    def print_solution(self) -> None:
        """Print the solution of the problem."""
        #TODO
        # - if self.solution is not None:
        #   print a board with:
        #     - "#" for a queen
        #     - "-" for an empty cell
        pass  # code à remplacer

    def solve(self) -> None:
        """Solve the instance of n‑queens."""
        #TODO
        # 1. get the model (create_model)
        # 2. get the solver
        # 3. set a time limit (60 seconds)
        # 4. solve and print solver info (print_solver_info(solver))
        # 5. build the solution (to_solution)
        pass  # code à remplacer

    def sol_enumeration(self) -> List[List[int]]:
        """Enumerate and return all solutions (as list of columns)."""
        #TODO
        # 1. self.create_model()
        # 2. get the solver
        # 3. set a time limit (60 seconds)
        # 4. loop while solver.solve():
        #    - get current columns [v.get_value() for v in self.col]
        #    - append to a list of solutions
        # 5. optionally keep last solution in self.solution
        # 6. return list of solutions
        pass  # code à remplacer

    def print_solver_info(self, solver) -> None:
        """Print solver informations: time, nodes, backtracks, fails, restarts."""
        #TODO
        # - print:
        #   - time (ms): solver.get_time_count()
        #   - nodes: solver.get_node_count()
        #   - backtracks: solver.get_backtrack_count()
        #   - fails: solver.get_fail_count()
        #   - restarts: solver.get_restart_count()
        pass  # code à remplacer


if __name__ == "__main__":
    n = 4
    n_queens = NqueensPychoco(n)
    n_queens.solve()
    n_queens.print_solution()