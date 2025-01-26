class Auto:  # Klasa bazowa
    def __init__(self, marka, rok_produkcji):
        self.marka = marka  # Atrybuty podstawowe
        self.rok_produkcji = rok_produkcji

    def uruchom_silnik(self): #metody
        print("Silnik uruchomiony!")

    def przedstaw_sie(self):
        print(f"Jestem {self.marka} z {self.rok_produkcji} roku")