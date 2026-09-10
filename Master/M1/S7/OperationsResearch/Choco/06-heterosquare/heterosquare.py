from typing import List, Optional
from pychoco import Model


# Let's define a solution, a square as a List[List[int]].
Solution = List[List[int]]


class HeteroSquarePychoco:
    def __init__(self, n: int) -> None:
        """Construct an instance of the heterosquare problem."""
        #TODO:
        # - keep the size (n)
        # - keep the current solution as None
        # - if you want, keep self.model, self.val, self.sum_lcd as None
        self.size: int = n
        self.model: Optional[Model] = None
        self.val = None
        self.sum_lcd = None
        self.solution: Optional[Solution] = None

    def create_model(self) -> Model:
        """Create the model of the problem instance."""
        #TODO:
        # 1. Create a Model
        # 2. Create variables:
        #    - val: a n x n matrix of IntVar, domain 1..n*n
        #    - sum_lcd: a list of 2*n+2 IntVar for:
        #      - sums of each row
        #      - sums of each column
        #      - sum of main diagonal
        #      - sum of anti-diagonal
        # 3. Post the constraints:
        pass  

    def solve(self) -> None:
        """Solve the instance of heterosquare."""
        # 1. create the model
        mdl = self.create_model()
        print("\nSolving model....")

        # 2. get the solver
        solver = mdl.get_solver()
        # 3. set a time limit (60 seconds) via limit_time
        solver.limit_time("60s")

        # 4. solve and print solver info (stats via solver.get_*)
        if solver.solve():
            # 5. if a solution exists, build self.solution
            n = self.size
            self.solution = [
                [self.val[i][j].get_value() for j in range(n)]
                for i in range(n)
            ]
            print("Solution:\n")
        else:
            print("No solution found\n")
            self.solution = None

    def sol_enumeration(self) -> List[Solution]:
        """Enumerate and return all solutions.
        The method returns a list of Solution, i.e. a List[List[List[int]]]."""
        #TODO:
        # 1. create the model via self.create_model()
        # 2. get the solver
        # 3. set a time limit (optional, but recommended: 60 s)
        # 4. loop while solver.solve() and store each solution
        # 5. keep the last solution in self.solution
        # 6. return the list of solutions
        pass  # code à remplacer

    def print_solution(self) -> None:
        """Print the solution of the problem."""
        #TODO:
        # - if self.solution is not None, print the square as a matrix
        #   print each row on a separate line
        pass  # code à remplacer

    # Call this function in the solve method, after solving the model
    def print_solver_info(self, solver) -> None:
        """Print solver information: time, number of nodes, backtracks, fails, restarts.
        (Note: pychoco does not expose the number of variables and constraints directly.)"""
        print("Statistics:")
        print("Time (ms):        ", solver.get_time_count())
        print("Nodes:            ", solver.get_node_count())
        print("Backtracks:       ", solver.get_backtrack_count())
        print("Fails:            ", solver.get_fail_count())
        print("Restarts:         ", solver.get_restart_count())


if __name__ == "__main__":
    heterosquare = HeteroSquarePychoco(3)
    heterosquare.solve()
    heterosquare.print_solution()

    print("nb sol of size 2 : ", len(HeteroSquarePychoco(2).sol_enumeration()))
    print("nb sol of size 3 : ", len(HeteroSquarePychoco(3).sol_enumeration()))