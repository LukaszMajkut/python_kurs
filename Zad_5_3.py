import collections

nazwa_pliku = input("Wpisz nazwe pliku który chcesz otworzyć: ")
ilosc_slow = collections.defaultdict(int)
liczba_slow = []
liczba_znakow = []

with open(nazwa_pliku) as plik:
    for linia in plik:
        slowa = linia.split(" ")
        liczba_slow.extend(slowa)
        for slowo in slowa:
            if slowo not in slowa:
                ilosc_slow[slowo] = 1
            if slowo in slowa:
                ilosc_slow[slowo] += 1
        for znak in linia:
            liczba_znakow.append(znak)
    for key in sorted(ilosc_slow.keys()):
        print (f'{key} --> {ilosc_slow[key]}')

    print (f'Liczba słów w pliku o nazwie {nazwa_pliku} wynosi {len(liczba_slow)}')
    print (f'Liczba znaków w pliku o nazwie {nazwa_pliku} wynosi {len(liczba_znakow)}')