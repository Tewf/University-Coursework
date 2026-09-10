from typing import Optional
from pychoco import Model

from car_seq_instance import CarSeqInstance


class CarSeqSolver:
    """
    A class to model the solver of the car sequencing problem.
    """

    # ------------------------------------------------------------------
    # Fields
    # ------------------------------------------------------------------

    def __init__(self, data: CarSeqInstance, element_model: bool = True) -> None:
        """
        Constructor of the car sequencing solver with options.
        :param data: reference to the dataset
        :param element_model: True if channeling uses Element,
                              False if it uses reified IfThen constraints
        """
        # Reference to the dataset
        self.data: CarSeqInstance = data

        # True if the channeling is modeled using Element constraints,
        # False if it is modeled using reified IfThen constraints
        self.elementCt: bool = element_model

        # A reference to the PyChoco model
        self.model: Optional[Model] = None

        # Variables of the model
        # TODO: declare slot and x variables
        self.slot = None
        self.x = None

        # Store solution
        self.sol: Optional[list[int]] = None
        self.isSat: bool = False
        self.nbFail: int = 0
        self.cpu_in_s: float = 0.0

        # State the model
        self.stateModel()

    # ------------------------------------------------------------------
    # Getters (for statistics / automatic tests)
    # ------------------------------------------------------------------

    def getNbFail(self) -> int:
        """
        :return: the number of fails of the search tree
        """
        return self.nbFail

    def getCpu_in_s(self) -> float:
        """
        :return: the cpu time
        """
        return self.cpu_in_s

    def isSat_(self) -> bool:
        """
        :return: True if a solution has been found
        """
        return self.isSat

    def getChocoSolver(self):
        """
        :return: the choco solver so automatic tests can be performed on it
        WARNING: this method may be required by the caseine activity
        """
        return self.model.get_solver()

    # ------------------------------------------------------------------
    # Model
    # ------------------------------------------------------------------

    def stateModel(self) -> None:
        """
        State the car sequencing model taking into account the various options.
        """
        d = self.data

        # TODO
        # 1. Create a model
        # self.model = Model("CarSeq_...")

        # 2. Create variables
        #    slot[i] = class of car at position i
        #    x[i][o] = 1 iff option o is present at position i

        # 3. Post constraints
        #    - demand constraints on classes
        #    - window constraints on options
        #    - channeling

        if self.elementCt:   # Channeling based on Element constraints
            # TODO: channel slot <-> x with Element
            pass
        else:                # Channeling based on IfThen constraints
            # TODO: channel slot <-> x with reified IfThen constraints
            pass

    # ------------------------------------------------------------------
    # Solving
    # ------------------------------------------------------------------

    def solve(self, time_limit_s: Optional[int] = None) -> Optional[list[int]]:
        """
        WARNING: this method may be required by the caseine activity.
        This method must return the solution found as a list of integers
        encoding the sequence of cars (sequence of car classes).

        Example:
        a solution to ford10_3_4.car could be [1, 2, 0, 2, 0, 2, 2, 0, 2, 1]

        :param time_limit_s: optional time limit in seconds
        :return: the sequence of cars found or None if no solution has been found
        """
        solver = self.model.get_solver()
        # solver.show_short_statistics()
        # if time_limit_s is not None:
        #     solver.limit_time(f"{time_limit_s}s")

        sol = None
        if solver.solve():
            # TODO: fill the solution array from slot variables
            # sol = [...]
            self.sol = sol
            self.isSat = True
        else:
            self.sol = None
            self.isSat = False

        # Statistics
        # self.nbFail = int(solver.get_backtrack_count())
        # self.cpu_in_s = float(solver.get_time_count())
        return sol