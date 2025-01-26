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

def main():
            # Tworzymy obiekty klasy SamochodOsobowy i Ciezarowka
        samochod = SamochodOsobowy("Toyota", 2020, 5)
        ciezarowka = Ciezarowka("Volvo", 2018, 10000)

            # Prezentacja samochodu osobowego
        print("Samochód osobowy")
        samochod.przedstaw_sie()
        samochod.uruchom_silnik()
        samochod.otworz_drzwi()

            # Prezentacja ciężarówki
        print("\nCiężarówka")
        ciezarowka.przedstaw_sie()
        ciezarowka.uruchom_silnik()
        ciezarowka.zaladuj()
if __name__ == "__main__":
    main()  #if __name__ == "__main__": kod jest uruchamiany bezposreddnio a nie gdy jest importowany