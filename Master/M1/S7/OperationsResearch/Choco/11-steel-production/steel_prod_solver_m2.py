from pychoco import Model


class SteelProdSlvM2:
    """
    A class to represent the CP model referred to as M2
    """

    def __init__(self, data, withDedicatedSearch=False):
        """
        Constructor
        :param data:
        :param withDedicatedSearch: specify whether a specific branching heuristic is used
        """
        # A reference to the Choco model
        self.model = None

        # Reference to the data set
        self.data = data

        # Use a user defined search strategy
        self.withDedicatedSearch = withDedicatedSearch

        # Optional fields to store solution information
        self.sol = None
        self.loss_value = -1
        self.nbFail = 0
        self.cpu_in_s = 0.0

        self.stateModel()

    def getChocoSolver(self):
        """
        :return: the Choco solver so automatic tests can be performed on it
        WARNING: this method is required by the caseine activity
        """
        return self.model.get_solver()

    def getBestSolValue(self):
        return self.loss_value
        
    def getCpu_in_s(self):
        return self.cpu_in_s

    def stateModel(self):
        """
        Build the Choco model for the Steel Production problem
        """
        # 1. Create a model
        self.model = Model("Steel")

        # 2. Create the variables
        # TODO

        # 3. Post the constraints
        # TODO

    def solve(self):
        """
        Solve the model and return the solution

        :return: an array of length the number of orders that describes the solution.
                 sol[i] is the slab where the i-th order is assigned.
                 Finally, slabs are indexed from 0 to at most nOrders-1.
        """
        sol = None
        solver = self.getChocoSolver()

        while solver.solve():
            # TODO: extract current solution from decision variables
            # Example:
            # sol = [var.get_value() for var in self.x]
            # self.sol = sol
            # self.loss_value = ...
            pass

        self.nbFail = solver.get_backtrack_count()
        self.cpu_in_s = solver.get_time_count()
        return sol

    def makeTimeLimit(self, limitInS):
        """
        This method is used for the test in Caseine, it will be called before
        the call to solve() in order to test the quality of solutions.
        WARNING: this method is required by the caseine activity
        """
        self.getChocoSolver().limit_time(limitInS)