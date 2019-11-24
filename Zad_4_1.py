"""
Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia (takie jak w serwisie internetowym z ogłoszeniami).
Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.
"""

class Ogloszenie:
    def __init__(self, tytul: str, opis: str, cena: float, dane):
        self.tytul = tytul
        self.opis = opis
        self.cena = cena
        self.dane = dane
    def print_info(self):
        print (f'\t {self.tytul} \n {self.opis} \n Cena wynosi {self.cena} PLN. Zapraszamy do kontaktu: {self.dane} ')
    def __str__(self):
        return f'\t {self.tytul} \n {self.opis} \n Cena wynosi {self.cena} PLN. Zapraszamy do kontaktu: {self.dane}'

mieszkanie = Ogloszenie("Mieszkanie na sprzedaż", "Oferuje na sprzedaż piękne i przestronne mieszkanie na ul. Kochanowskiego 28",500000, "Marek Jozwik nr tel. 567892334")
print (mieszkanie)