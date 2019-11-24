'''
Przygotuj funkcję, która będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

- `suma(liczby)` - zwraca sumę liczb z listy `liczby`
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby`
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `ile_wiekszych(tab, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
'''


def suma(liczby): # tutaj chodzilo ze lista ma byc podana od razu tak jakby
    return sum(liczby)

print (suma([2,45,22]))

def srednia(liczby):
    return suma(liczby)/len(liczby)

print (suma([2,45,22]))

def maksimum(liczby):
    return maksimum(liczby)

print (maksimum([2,45,22]))

def roznica_min_max(liczby):
    return max(liczby) - min(liczby)

print (roznica_min_max([2,45,22]))


def wypisz_wieksze(liczby, x):
    wieksze = [i for i in liczby if x < i]
    return wieksze

print (roznica_min_max([2,45,22]))

def pierwsza_wieksza(liczby, x):
    for i in liczby:
        if x < i:
            return i
        else:
            continue

        return None

print (pierwsza_wieksza([2,45,22], 3))

def suma_wiekszych(liczby, x):
    wieksze = [i for i in liczby if x < i]
    return sum(wieksze)

print (suma_wiekszych([2,45,22],3))

def ile_wiekszych(liczby,x):
    wieksze = [i for i in liczby if x < i]
    return (len(wieksze))

print (ile_wiekszych([2,45,22],3))

def wypisz_podzielne(liczby,x):
    podzielne = [i for i in liczby if i % x == 0]
    return podzielne

print (wypisz_podzielne([2,45,22],2))

def pierwsza_podzielna(liczby,x):
    for i in liczby:
        if i % x == 0:
            return i
        else:
            pass

    return None

print (pierwsza_podzielna([2,45,22],2))

def ile_wiekszych(liczby,x):
    wieksze = [i for i in liczby if x < i]
    return len(wieksze)

print (ile_wiekszych([2,45,22],3))

def znajdz_wspolny(liczby1,liczby2):
    a = set(liczby1)
    b = set(liczby2)
    a &= b
    if len(a) == 0:
        return None
    else:
        return a

print (znajdz_wspolny([1,2,3,4,5],[1,2,3]))