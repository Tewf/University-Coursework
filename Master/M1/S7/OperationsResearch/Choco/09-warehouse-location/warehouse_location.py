from pychoco import Model
from typing import List, Optional


class WarehouseLocation:
    """
    Warehouse Location problem: a company considers opening warehouses
    at some candidate locations in order to supply its existing stores.

    n: number of stores
    m: number of potential warehouses
    c_{ij}: cost for connecting store i to warehouse j
    k_j: maximum number of stores that can connect to warehouse j
    F: fixed cost for opening a warehouse.

    At most k_j stores connected to warehouse j.

    The objective is to determine which warehouses to open, and which of these
    warehouses should be connected to the various stores, such
    that the sum of the maintenance and supply costs is minimized.

    <a ref="https://www.csplib.org/Problems/prob034/">CSPLib</a>
    """

    def __init__(
        self,
        warehouses: List[str] = None,
        stores: int = 10,
        fixed_cost: int = 30,
        capacities: List[int] = None,
        supply_costs: List[List[int]] = None
    ):
        if warehouses is None:
            warehouses = ["Bonn", "Bordeaux", "London", "Paris", "Rome"]
        if capacities is None:
            capacities = [1, 4, 2, 1, 3]
        if supply_costs is None:
            supply_costs = [
                [20, 24, 11, 25, 30],
                [28, 27, 82, 83, 74],
                [74, 97, 71, 96, 70],
                [2, 55, 73, 69, 61],
                [46, 96, 59, 83, 4],
                [42, 22, 29, 67, 59],
                [1, 5, 73, 59, 56],
                [10, 73, 13, 43, 96],
                [93, 35, 63, 85, 46],
                [47, 65, 55, 71, 95]
            ]
        # Data
        self.warehouses: List[str] = warehouses
        self.stores: int = stores
        self.fixed_cost: int = fixed_cost
        self.capacities: List[int] = capacities
        self.supply_costs: List[List[int]] = supply_costs

        # Solver parts
        self.model: Model = None
        # TODO: declare supplier, open, cost, tot_cost
        self.supplier = None
        self.open = None
        self.cost = None
        self.tot_cost = None

        self.modelling()

    def get_model(self) -> Model:
        """
        Public accessor.
        """
        return self.model

    def modelling(self) -> None:
        """
        Modelling of the Warehouse Location Problem.
        """
        # TODO: create the model
        # self.model = Model("Warehouse Location")

        # TODO: declare the variables:
        # - supplier: one warehouse index per store
        # - open: boolean for each warehouse
        # - cost: supply cost per store
        # - tot_cost: total cost (fixed + supply)

        # TODO: post constraints:
        # 1. For each store s:
        #    - the warehouse that supplies it must be open (use element)
        #    - its cost is supply_costs[s][supplier[s]] (use element)
        #
        # 2. For each warehouse w:
        #    - count how many stores are supplied by w (count constraint)
        #    - capacity constraint: at most capacities[w] stores per warehouse
        #    - open[w] must be true if at least one store is supplied by w
        #
        # 3. Total cost: tot_cost = sum(fixed_cost * open[w]) + sum(cost[s])
        #    (use scalar with proper coefficient list on open + cost)
        #
        # 4. Declare the objective to minimize tot_cost
        #    self.model.set_objective(self.tot_cost, maximize=False)
        pass

    def next_solution(self) -> Optional[List[int]]:
        """
        Return the next solution found as an array of int
        where each element is the supplier of each store, in the order of declaration.
        An additional element is added at the end of the array, representing the total cost.

        If no solution is found, return None.
        """
        solver = self.model.get_solver()
        if solver.solve():
            # TODO:
            # - read supplier[s] for each store s
            # - read tot_cost
            # - return flat list: [supplier[0], ..., supplier[stores-1], tot_cost]
            stores: int = self.stores
            suppliers = [0] * stores       # à remplacer par supplier[s].get_value()
            total_cost = 0                 # à remplacer par tot_cost.get_value()
            return suppliers + [total_cost]
        else:
            return None


def main() -> None:
    print("Warehouse Location Problem")
    pb = WarehouseLocation()
    print("Run solving step")
    solution_count = 0
    while True:
        solution = pb.next_solution()
        if solution is None:
            break
        solution_count += 1
        stores = pb.stores
        for i in range(stores):
            print(f"Store #{i + 1} is supplied by {pb.warehouses[solution[i]]}")
        print(f"Total cost: {solution[stores]}")
        print()
    if solution_count == 0:
        print("No solution found")


if __name__ == "__main__":
    main()