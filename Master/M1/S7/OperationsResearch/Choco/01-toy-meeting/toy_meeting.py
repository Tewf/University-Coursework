from pychoco import Model
from typing import List

class ToyMeetingChoco:
    """Classe pour modéliser et résoudre le problème Toy Meeting avec PyChoco"""
    
    def __init__(self, n: int) -> None:
        self.nb_meetings: int = n
        self.solution: List[int] = None

    def solve(self) -> List[int]:
        # 1. Créer le modèle
        model = Model("Toy Meeting")

        # 2. Créer les variables
        meet = [model.intvar(1, 5, f"x_{j}") for j in range(self.nb_meetings)]
        # pause dans {1, 2}
        pause = model.intvar(1, 2, "pause")

        # 3. Poster les contraintes
        model.member(meet[0], [1, 2]).post()
        model.member(meet[2], [1, 2, 3]).post()

        model.scalar([meet[1], pause, meet[3]], [1, 1, -1], "=", -1).post()
        
        model.arithm(meet[2], "<", meet[1]).post()
        
        model.all_different(meet).post()

        # 4. Résoudre
        print("\nRésolution du modèle (PyChoco)....")
        solver = model.get_solver()
        
        if solver.solve():
            print("Solution:\n")
            self.solution = [m.get_value() for m in meet]
            print("meet = ", self.solution)
            print("pause = ", pause.get_value())
            return self.solution
        else:
            print("Aucune solution trouvée\n")
            return None