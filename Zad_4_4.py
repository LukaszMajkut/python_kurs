"""
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).
Niech ta klasa ma metody `dolej` i `odlej`. Obie metody niech przyjmują argument `ile` i niech odpowiednio
 dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody, niż jest w zbiorniku.
Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. Metoda dolej oprócz argumentu `ile`
 powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody. Dolanie wody do zbiornika
 powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
"""

class Zbiorniki:
    def __init__(self, ilosc_wody = 0, temperatura = None):
        self.ilosc_wody = ilosc_wody
        self.temperatura = temperatura
    def dolej(self, ile, temperatura_dolewanej):
        self.ile = ile
        self.temperatura_dolewanej = temperatura_dolewanej
        if self.ilosc_wody == 0:
            self.temperatura = self.temperatura_dolewanej
        else:
            self.temperatura = (self.temperatura + self.temperatura_dolewanej)/2
        self.ilosc_wody += self.ile

    def odlej(self,ile):
        self.ile = ile
        if self.ile > self.ilosc_wody:
            pass
        else:
            self.ilosc_wody -= self.ile
    def __str__(self):
        return f'Zbiornik z {self.ilosc_wody} o temperaturze równej {self.temperatura} stopni C'

zbiornik = Zbiorniki()
print (zbiornik)
zbiornik.dolej(10,30)
print (zbiornik)
zbiornik.dolej(5,10)
print(zbiornik)