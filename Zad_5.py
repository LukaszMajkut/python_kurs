"""
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. Zadbaj o to aby stan bankomatu przetrzymywany
 był w zmiennych prywatnych.
Przykład użycia:
cash_machine = CashMachine()
cash_machine.is_available()
False
cash_machine.put_money([200, 100, 100, 50])
cash_machine.is_available()
True
cash_machine.withdraw_money(150) [100, 50]
"""

#WERSJA Z DODAWANIEM PIENIĘDZY DO OGÓLNEJ PULI

#class Cashmachine:
#    def __init__(self):
#        self._stan = 0
#
#    @property
#    def stan(self):
#        return self._stan
#
#    def is_available(self):
#        if self._stan > 0:
#            return True
#        else:
#            return False
#    def put_money(self, ilosc):
#        self.ilosc = ilosc
#        if ilosc <= 0:
#            raise ValueError('Kwota która chesz wpłacić musi być większa od zera')
#        self._stan += ilosc
#    def withdraw_money(self,ilosc):
#        self.ilosc = ilosc
#        if  ilosc > self._stan:
#            raise ValueError('Nie możesz wybrać więcej pieniędzy niż jest w bankomacie')
#        self._stan -= ilosc
#    def __str__(self):
#        return f'W bankomacie znajduje się {self._stan} PLN'

#WERSJA Z DODAWANIEM KONKRETNYCH BANKNOTÓW DO WSPÓLNEJ LISTY

"""
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. Zadbaj o to aby stan bankomatu przetrzymywany
 był w zmiennych prywatnych.
Przykład użycia:
cash_machine = CashMachine()
cash_machine.is_available()
False
cash_machine.put_money([200, 100, 100, 50])
cash_machine.is_available()
True
cash_machine.withdraw_money(150) [100, 50]
"""
class Cashmachine:

    def __init__(self):
        self._stan = list()

    @property
    def is_available(self):
        if self._stan:
            return True
        else:
            return False

    def put_money(self, lista):
        self.lista = lista
        self._stan += self.lista

    def withdraw_money(self, wartosc):
        self.wartosc = wartosc
        self._stan.sort()
        print(self)
        if self.wartosc > sum(self._stan):
            raise ValueError('Nie ma wystarczającej ilości pieniędzy w bankomacie')
        while self.wartosc != 0:
            for i in self._stan:
                if i <= self.wartosc:
                    self.wartosc -= i
                    self._stan.remove(i)
                else:
                    pass


    def __str__(self):
        return f'banknoty w bankomacie: {self._stan}'







bankomat = Cashmachine()
print (bankomat.is_available)
bankomat.put_money([100,50,50,200])
print (bankomat.is_available)
print (bankomat)
bankomat.withdraw_money(150)
print (bankomat)





