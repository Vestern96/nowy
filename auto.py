class Auto:  # Klasa bazowa
    def __init__(self, marka, rok_produkcji):
        self.marka = marka  # Atrybuty podstawowe
        self.rok_produkcji = rok_produkcji

    def uruchom_silnik(self): #metody
        print("Silnik uruchomiony!")

    def przedstaw_sie(self):
        print(f"Jestem {self.marka} z {self.rok_produkcji} roku")

class SamochodOsobowy(Auto):  # Klasa dziedzicząca po Auto
        def __init__(self, marka, rok_produkcji, liczba_drzwi):
                super().__init__(marka, rok_produkcji)  # Wywołanie konstruktora klasy bazowej
                self.liczba_drzwi = liczba_drzwi  # Dodatkowy atrybut specyficzny dla samochodu osobowego

        def uruchom_silnik(self):
                print("Samochód osobowy rusza!")

        def otworz_drzwi(self):
            print(f"Otwieram {self.liczba_drzwi} drzwi!")
class Ciezarowka(Auto):  # Klasa dziedzicząca po Auto
    def __init__(self, marka, rok_produkcji, ladownosc):
        super().__init__(marka, rok_produkcji)  # Wywołanie konstruktora klasy bazowej
        self.ladownosc = ladownosc  # Atrybut specyficzny dla ciężarówki

    def uruchom_silnik(self):
        print("Ciężarówka uruchomiona!")

    def zaladuj(self):
        print(f"Ładuję {self.ladownosc} kg towaru.")