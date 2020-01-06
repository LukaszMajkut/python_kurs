import collections

nazwa_pliku = input("Wpisz nazwe pliku który chcesz otworzyć: ")
ilosc_slow = collections.defaultdict(int)
liczba_slow = []
liczba_znakow = []

with open(nazwa_pliku) as plik:
    for linia in plik:
        slowa = linia.split(" ")
        slowa_gole = []
        for i in slowa:
            slowa_gole.append(i.strip(" .,;:!?\n"))
        liczba_slow.extend(slowa_gole)
        for slowo in slowa_gole:
            if slowo not in slowa_gole:
                ilosc_slow[slowo] = 1
            elif slowo in slowa_gole:
                ilosc_slow[slowo] += 1
        for znak in linia:
            liczba_znakow.append(znak)
    for key in sorted(ilosc_slow.keys()):
        print (f'{key} --> {ilosc_slow[key]}')

    print (f'Liczba słów w pliku o nazwie {nazwa_pliku} wynosi {len(liczba_slow)}')
    print (f'Liczba znaków w pliku o nazwie {nazwa_pliku} wynosi {len(liczba_znakow)}')