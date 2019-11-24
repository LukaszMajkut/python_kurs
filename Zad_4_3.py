"""
Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).
Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści “Moja predkość to (ileś tam). Mam jeszcze (ileś tam)
litrów paliwa.” Dodatkowo zaimplementuj metodę `__str__`.
Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość. Ta metoda niech zwiększa
predkość pociągu o tyle, ile jest powiedziane w argumencie.
I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (jeśli ktoś spróbuje tak zwiększyć prędkość,
prędkość niech pozostaje po prostu bez zmian). Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa
(jeśli ktoś spróbuje zwiększyć prędkość, kiedy nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).
Przetestuj swoje rozwiązanie i napisz testy, w których:
- zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
"""

class Pociag:
    def __init__(self, predkosc = 10, ilosc_paliwa = 1000):
        self.predkosc = predkosc
        self.ilosc_paliwa = ilosc_paliwa
    def opis(self):
        print (f'Moja predkość to {self.predkosc} km/h. Mam jeszcze {self.ilosc_paliwa} litrów paliwa')
    def __str__(self):
        return f'Moja predkość to {self.predkosc} km/h. Mam jeszcze {self.ilosc_paliwa} litrów paliwa'
    def przyspiesz(self,o_ile):
        self.o_ile = o_ile
        if self.o_ile >= 0.75*self.predkosc or self.ilosc_paliwa == 0:
            pass
        else:
            self.predkosc += self.o_ile
            self.ilosc_paliwa -= (self.predkosc - (self.predkosc-self.o_ile)) * ((self.predkosc-self.o_ile) / 100)

def test_zwieksz_5():
    pociag = Pociag()
    pociag.przyspiesz(5)
    assert pociag.opis == 'Moja predkość to 15 km/h. Mam jeszcze 999.5 litrów paliwa'

def test_zwieksz_20():
    pociag = Pociag()
    pociag.przyspiesz(20)
    assert str(pociag) == 'Moja predkość to 10 km/h. Mam jeszcze 1000 litrów paliwa'

def test_zwieksz_8():
    pociag = Pociag()
    pociag.przyspiesz(8)
    assert str(pociag) == 'Moja predkość to 10 km/h. Mam jeszcze 1000 litrów paliwa'

def test_zwieksz_10():
    pociag = Pociag()
    pociag.przyspiesz(10)
    assert str(pociag) == 'Moja predkość to 10 km/h. Mam jeszcze 1000 litrów paliwa'