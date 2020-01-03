
licznik = 0
nazwa_pliku = input("Wpisz nazwe pliku który chcesz otworzyć:")

with open(nazwa_pliku) as plik:
    slowo = input("Podaj słowo które mam zliczyć:")
    for linia in plik:
        if slowo in linia:
            licznik += 1

    print (f"Słowo '{slowo}' pojawiło się w danym tekscie {licznik} razy")
