from typing import List
from collections import deque

class CarSeqInstance:
    """
    Instance du car sequencing, lecture et checker,
    """

    def __init__(self, file: str) -> None:
        self.name = file.split("/")[-1]
        with open(file, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        it = iter(lines)
        next(it)                     # commentaire
        self.nCars = int(next(it))   # n
        next(it)
        self.nClasses = int(next(it))  # u
        next(it)                     # skip capacities
        self.nOptions = int(next(it))  # m
        next(it)

        self.demand = self._scan_array(next(it), self.nClasses)
        next(it)

        self.required = []
        for _ in range(self.nClasses):
            self.required.append(self._scan_array(next(it), self.nOptions))

        next(it)
        self.block = self._scan_array(next(it), self.nOptions)
        next(it)
        self.maxPerBlock = self._scan_array(next(it), self.nOptions)
        next(it)
        self.minPerBlock = self._scan_array(next(it), self.nOptions)

        self._init_demand_per_option()

    def _scan_array(self, line: str, size: int) -> List[int]:
        parts = [x.strip() for x in line.split(",")]
        return [int(parts[i]) for i in range(size)]

    def _init_demand_per_option(self) -> None:
        self.demandPerOption = [0] * self.nOptions
        for o in range(self.nOptions):
            total = 0
            for k in range(self.nClasses):
                if self.required[k][o] == 1:
                    total += self.demand[k]
            self.demandPerOption[o] = total

    @classmethod
    def from_data(cls, n: int, u: int, m: int, demand: List[int], block: List[int], maxPerBlock: List[int], minPerBlock: List[int], r: List[List[int]], name: str = "manual_instance") -> "CarSeqInstance":
        obj = cls.__new__(cls)
        obj.name = name
        obj.nCars = n
        obj.nClasses = u
        obj.nOptions = m
        obj.demand = demand
        obj.required = r
        obj.block = block
        obj.maxPerBlock = maxPerBlock
        obj.minPerBlock = minPerBlock
        obj._init_demand_per_option()
        return obj

    # --- getters simples ---

    def getName(self) -> str:
        return self.name

    def getNbCars(self) -> int:
        return self.nCars

    def getNbClasses(self) -> int:
        return self.nClasses

    def getNbOptions(self) -> int:
        return self.nOptions

    def getDemand(self, classCar: int) -> int:
        return self.demand[classCar]

    def getBlockSize(self, o: int) -> int:
        return self.block[o]

    def getMaxOccurrence(self, o: int) -> int:
        return self.maxPerBlock[o]

    def getMinOccurrence(self, o: int) -> int:
        return self.minPerBlock[o]

    def getDemandOfOption(self, o: int) -> int:
        return self.demandPerOption[o]

    def isOptionOInClassk(self, o: int, k: int) -> bool:
        return self.required[k][o] == 1

    # --- checker, directement dans la même classe ---

    def checker(self, sol: List[int]) -> str:
        if sol is None:
            return "No solution has been found"
        if not self._checkNbCars(sol):
            return "The demand is not satisfied"
        for o in range(self.getNbOptions()):
            if not self._checkOption(o, sol):
                return f"Option {o} is not correctly sequenced"
        return "Ok"

    def _checkNbCars(self, sol: List[int]) -> bool:
        if any(c == -1 for c in sol):
            return False
        nbPerClass = [0] * self.nClasses
        for c in sol:
            nbPerClass[c] += 1
        for k in range(self.nClasses):
            if nbPerClass[k] != self.demand[k]:
                return False
        return True

    def _checkOption(self, j: int, sol: List[int]) -> bool:
        sequence = [self.required[sol[i]][j] for i in range(self.nCars)]
        q = self.block[j]
        p = self.maxPerBlock[j]
        l = self.minPerBlock[j]

        buf = deque(sequence[:q], maxlen=q)
        for k in range(q, len(sequence)):
            if not self._checkBlock(p, l, buf):
                return False
            buf.append(sequence[k])
        # dernier bloc
        if not self._checkBlock(p, l, buf):
            return False
        return True

    def _checkBlock(self, p: int, l: int, buf: deque) -> bool:
        s = sum(buf)
        return l <= s <= p