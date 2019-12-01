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

#WERSJA Z DODAWANIEM PIENIDZY DO OGÓLNEJ PULI

class Cashmachine:
    def __init__(self):
        self._stan = 0

    @property
    def stan(self):
        return self._stan

    def is_available(self):
        if self._stan > 0:
            return True
        else:
            return False
    def put_money(self, ilosc):
        self.ilosc = ilosc
        if ilosc <= 0:
            raise ValueError('Kwota która chesz wpłacić musi być większa od zera')
        self._stan += ilosc
    def withdraw_money(self,ilosc):
        self.ilosc = ilosc
        if  ilosc > self._stan:
            raise ValueError('Nie możesz wybrać więcej pieniędzy niż jest w bankomacie')
        self._stan -= ilosc
    def __str__(self):
        return f'W bankomacie znajduje się {self._stan} PLN'





