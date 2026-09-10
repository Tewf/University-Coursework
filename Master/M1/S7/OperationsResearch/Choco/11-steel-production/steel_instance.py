from typing import List


class SteelInstance:
    """
    Orders and slabs are indexed from 0.
    Colors in the input files are numbered from 1..nColors.
    """

    def __init__(
        self,
        file: str = None,
        nOrders: int = None,
        nbSlabCapas: int = None,
        nbColors: int = None,
        orderWeights: List[int] = None,
        orderColors: List[int] = None,
        slabCapacity: List[int] = None,
    ) -> None:
        if file is not None:
            self._read_from_file(file)
        else:
            self.name = "manual_instance"
            self.nOrders = nOrders
            self.nSlabCapas = nbSlabCapas
            self.nColors = nbColors
            self.w = orderWeights
            self.c = orderColors
            self.capa = slabCapacity

    def _read_from_file(self, file: str) -> None:
        self.name = file.split("/")[-1]

        with open(file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]

        self.nOrders = int(lines[1])
        self.nSlabCapas = int(lines[3])
        self.nColors = int(lines[5])
        self.w = self._scan_array(lines[7], self.nOrders)
        self.c = self._scan_array(lines[9], self.nOrders)
        self.capa = self._scan_array(lines[11], self.nSlabCapas)

    def _scan_array(self, line: str, size: int) -> List[int]:
        tab = [int(x.strip()) for x in line.split(",")]
        if len(tab) != size:
            raise ValueError(f"Expected array of size {size}, got {len(tab)}")
        return tab

    def print(self) -> None:
        print(f"Nb Orders : {self.nOrders}")
        print(f"Nb Capacities of Slabs: {self.nSlabCapas}")
        print(f"Nb Colors: {self.nColors}")
        print(f"Weights : {self.w}")
        print(f"Colors : {self.c}")
        print(f"Slabs Capacities : {self.capa}")

    def shortPrint(self) -> None:
        print(f"NbOrd: {self.nOrders} NbCSlab: {self.nSlabCapas} NbCol: {self.nColors}")

    def getName(self) -> str:
        return self.name

    def getnOrders(self) -> int:
        return self.nOrders

    def getnSlabCapas(self) -> int:
        return self.nSlabCapas

    def getnColors(self) -> int:
        return self.nColors

    def getWeight(self, order_idx: int) -> int:
        assert 0 <= order_idx < self.nOrders
        return self.w[order_idx]

    def getColor(self, order_idx: int) -> int:
        assert 0 <= order_idx < self.nOrders
        return self.c[order_idx]

    def getCapacity(self, slab_idx: int) -> int:
        assert 0 <= slab_idx < self.nSlabCapas
        return self.capa[slab_idx]

    def getMaxCapa(self) -> int:
        return max(self.capa)

    def minCapaForSlab(self, weight: int) -> int:
        for cap in self.capa:
            if cap >= weight:
                return cap
        return -1