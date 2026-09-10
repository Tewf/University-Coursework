from pychoco import Model
from typing import List, Optional
import sys


class ExtToyMeetingChoco:
    """
    Toy Meeting version étendue.
    """

    def __init__(self, n: int) -> None:
        self.nb_meetings: int = n
        self.solution: Optional[List[int]] = None
        self.model: Optional[Model] = None
        self.solver = None
        self.meet = []
        self.pause = None

    def create_model(self) -> Model:
        """Crée le modèle."""
        self.model = Model("Extended Toy Meeting")

        self.meet = [self.model.intvar(1, 5, f"x_{j}") for j in range(self.nb_meetings)]
        self.pause = self.model.intvar(1, 2, "d")

        self.model.member(self.meet[0], [1, 2]).post()
        self.model.member(self.meet[2], [1, 2, 3]).post()
        self.model.scalar([self.meet[1], self.pause, self.meet[3]], [1, 1, -1], "=", -1).post()
        self.model.arithm(self.meet[2], "<", self.meet[1]).post()
        self.model.all_different(self.meet).post()

        self.solver = self.model.get_solver()
        return self.model

    def introductive_example(self) -> None:
        """Introduction complète avec énumération et vérification."""
        self.create_model()

        print("=== 1. Modèle créé ===")
        print(self.model)

        print("\n=== 2. Énumération complète des solutions ===")
        sols = self.sol_enumeration()
        for i, sol in enumerate(sols):
            print(f"Solution {i+1} : meet = {sol}")
        
        print(f"→ {len(sols)} solutions trouvées au total")

        print("\n=== 3. Vérification des solutions ===")
        for sol in sols:
            self.solution = sol
            print(f"  Solution {sol} valide : {self.check_solution()}")

        print("\n=== 4. Statistiques détaillées ===")
        self.print_statistics()

    def solve(self) -> None:
        """Résout une seule solution."""
        self.create_model()
        print("\n=== Résolution d'une seule solution ===")
        if self.solver.solve():
            self.solution = [v.get_value() for v in self.meet]
            self.print_solution()
            print("Solution valide ?", self.check_solution())
        else:
            self.solution = None
            print("Pas de solution trouvée.")

    def sol_enumeration(self) -> List[List[int]]:
        """Énumère toutes les solutions."""
        sols = []
        while self.solver.solve():
            current = [v.get_value() for v in self.meet]
            sols.append(current)
        return sols

    def print_solution(self) -> None:
        """Affiche la solution actuelle."""
        if self.solution:
            print("meet =", self.solution)
            print("pause =", self.pause.get_value())

    def check_solution(self) -> bool:
        """
        Vérification complète de la solution.
        """
        if not self.solution:
            return False
        
        # Vérifications explicites
        if self.solution[0] not in [1, 2]:
            return False
        if self.solution[2] not in [1, 2, 3]:
            return False
        if len(set(self.solution)) != len(self.solution):
            return False  # all_different
        if self.solution[3] - self.solution[1] < 2:
            return False  # x1 + pause - x3 = -1 avec pause>=1
        if self.solution[2] >= self.solution[1]:
            return False  # x2 < x1
        
        return True

    def print_statistics(self) -> None:
        """Statistiques complètes."""
        print("Temps (ms)              :", self.solver.get_time_count())
        print("Nœuds explorés          :", int(self.solver.get_node_count()))
        print("Backtracks              :", int(self.solver.get_backtrack_count()))
        print("Fails                   :", int(self.solver.get_fail_count()))
        print("Restarts                :", int(self.solver.get_restart_count()))
        try:
            print("Solutions trouvées      :", self.solver.get_solution_count())
        except Exception:
            print("Solutions trouvées      :", "N/A")


