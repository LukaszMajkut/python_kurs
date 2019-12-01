"""
Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`. Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi)
i jakieś ustawienie, czyli kurs (wyznaczony pojedyncza liczba).
Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.
Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
Metoda `idz` powoduje przejście żółwia o określoną odległość.
Z klasy będzie się korzystać tak:
```python
z = Zolw(100, 100)
z.idz(50)
print(z) # ma sie wypisac: x=100, y=50
z.obroc_sie(90)
z.idz(50)
print(z) # ma sie wypisac: x=150, y=50
"""
class Zolw:
    def __init__(self, x, y, kurs = 0):
        self.x = x
        self.y = y
        self.kurs = kurs
    def obroc_sie(self, obrot):
        self.obrot = obrot
        self.kurs += self.obrot
        if self.kurs >= 360:
            self.kurs = 0
    def idz(self, odleglosc):
        self.odleglosc = odleglosc
        if self.kurs == 0:
            self.y += self.odleglosc
        elif self.kurs == 90:
            self.x += self.odleglosc
        elif self.kurs == 180:
            self.y -= self.odleglosc
        elif self.kurs == 270:
            self.x -= self.odleglosc
    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

z = Zolw(100,100)
z.idz(50)
print(z)
z.obroc_sie(360)
z.idz(50)
print(z)
z.obroc_sie(90)
z.idz(75)
print(z)