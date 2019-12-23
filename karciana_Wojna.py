"""
KARCIANA GRA W WOJNE
"""

import random

class Karty:
    RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    SUITS = ['c','d','h','s']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}'

    @property
    def value(self):
        return self.RANKS.index(self.rank)

class Reka:
    def __init__(self, imie):
        self.karta_w_rece = []
        self.imie = imie

    def przydziel_karte(self):
        self.karta = Karty(rank = random.choice(Karty.RANKS), suit = random.choice(Karty.SUITS))
        self.karta_w_rece.append(self.karta)

    @property
    def wartosc(self):
        punkty = None
        for karta in self.karta_w_rece:
            punkty = karta.value
        return int(punkty)

    def __str__(self):
        for karta in self.karta_w_rece:
            return f'{karta}'

class Potyczka:
    def __init__(self):
        self.lista_graczy = []
        self.zwyciezca = []

    def dodaj_gracza(self,gracz):
        self.gracz = gracz
        self.lista_graczy.append(self.gracz)

    def walka(self):
        if self.lista_graczy[0].wartosc > self.lista_graczy[1].wartosc:
            print (f' Zwyciezcą zostaje {self.lista_graczy[0].imie} z kartą: {self.lista_graczy[0]}')
        else:
            print (f' Zwyciezca zostaje {self.lista_graczy[1].imie} z kartą: {self.lista_graczy[1]}')

    def __str__(self):
        return 'Wojna to bardzo niebezpieczna gra..'


karta = Karty("2","c")
print(karta)
gracz_1 = Reka("Marek")
gracz_1.przydziel_karte()
gracz_2 = Reka("Andrzej")
gracz_2.przydziel_karte()
print(gracz_1)
print(gracz_2)
print(gracz_1.wartosc)
print(gracz_2.wartosc)
gra = Potyczka()
gra.dodaj_gracza(gracz_1)
gra.dodaj_gracza(gracz_2)
gra.walka()
print (gra)



