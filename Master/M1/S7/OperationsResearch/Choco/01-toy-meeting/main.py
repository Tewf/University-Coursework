from toy_meeting import ToyMeetingChoco
from extended_toy_meeting import ExtToyMeetingChoco

def test_toy_meeting() -> None:
    """Méthode pour tester le solveur Toy Meeting"""
    toy_meeting = ToyMeetingChoco(4)
    toy_meeting.solve()

def test_extended_toy_meeting() -> None: 
    """Méthode pour tester le solveur Toy Meeting étendu"""
    toy_meeting = ExtToyMeetingChoco(4)
    
    print("******************** \nExemple d'introduction : ")
    toy_meeting.introductive_example()
    
    print("\n********************")
    print("=== Une seule solution + vérification ===")
    toy_meeting.solve()

    
if __name__ == "__main__":
    test_toy_meeting()
    #test_extended_toy_meeting() # Décommentez pour tester l'étendu