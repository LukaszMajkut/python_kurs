"""
Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.
Na przykład ogłoszenia o cenach z określonego przedziału.
Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
Użyj poznanych kolekcji do trzymania ogłoszeń. Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.
"""
class Ogloszenie:
    def __init__(self, id, marka, rok_produkcji, przebieg, silnik, cena):
        self.id = id
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        self.silnik = silnik
        self.cena = cena
    def __str__(self):
        opis = f'marka: {self.marka} \n rok produkcji: {self.rok_produkcji} \n przebieg: {self.przebieg} km \n silnik: {self.silnik} \n cena: {self.cena} PLN'
        return opis
    def print_info(self):
        print (f'Oto samochod marki {self.marka} z roku {self.rok_produkcji}. Samochód przejechał {self.przebieg} km, posiada silnik {self.silnik}. Cena wynosi {self.cena} PLN - do negocjacji')

opel = Ogloszenie(1, "Opel Astra", 2008, 190000, "1.6 diesel", 30000)
mazda = Ogloszenie(2, "Mazda CX3", 2012, 150000, "2.0 benzyna", 45000)
mercedes = Ogloszenie(3, "Mercedes C klasa", 2016, 112000, "2.0 diesel", 100000)
audi = Ogloszenie(4, "Audi A5", 2011, 250000, "2.0 diesel", 55000)

lista_ogloszen = []
lista_ogloszen.append(opel)
lista_ogloszen.append(mazda)
lista_ogloszen.append(mercedes)
lista_ogloszen.append(audi)


cena_max = int(input("Do jakiej ceny poszukujesz samochodu?"))

wynik = list(filter(lambda ogloszenie: ogloszenie.cena <= cena_max, lista_ogloszen ))

for i in wynik:
    print (i.__str__())

