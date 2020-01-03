import os
import sys
import csv

wzrost_min = None
wzrost_max = None
waga_min = None
waga_max = None
waga_suma = 0
POL = 0
wzrost_pol = 0
GER = 0
wzrost_ger = 0
FIN = 0
wzrost_fin = 0
AUT = 0
wzrost_aut = 0
NOR = 0
wzrost_nor = 0
USA = 0
wzrost_usa = 0

with open ("zawodnicy.csv", encoding="utf8") as plik:
    wybor = int(input("Wybierz jakie informacje chciałbyś uzyskac:\n"
                        "0 - najniższy, najwyższy, najlżejszy oraz najcięższy skoczek\n"
                        "1 - łączna waga skoczków wybranej narodowosci\n"
                        "2 - łączna ilość skoczków poszczególnych narodowosci oraz ich średni wzrost"))
    if wybor == 0:
        for linia in plik:
            imie, nazwisko, narodowosc, data_urodzenia, wzrost, waga = linia.split(";")
            wzrost = int(wzrost)
            waga = int(waga)
            if wzrost_min == None or wzrost < wzrost_min:
                wzrost_min = wzrost
                skoczek_min_wz = imie + " " + nazwisko
            if wzrost_max == None or wzrost > wzrost_max:
                wzrost_max = wzrost
                skoczek_max_wz = imie + " " + nazwisko
            if waga_min == None or waga < waga_min:
                waga_min = waga
                skoczek_min_wg = imie + " " + nazwisko
            if waga_max == None or waga > waga_max:
                waga_max = waga
                skoczek_max_wg = imie + " " + nazwisko
        print(f'Najniższy zawodnik mierzy {wzrost_min} cm i jest to {skoczek_min_wz}')
        print(f'Najwyższy zawodnik mierzy {wzrost_max} cm i jest to {skoczek_max_wz}')
        print(f'Najlżejszy zawodnik waży {waga_min} kg i jest to {skoczek_min_wg}')
        print(f'Najcięższy zawodnik waży {waga_max} kg i jest to {skoczek_max_wg}')
    elif wybor == 1:
        kraj = input("Skoczków jakiej narodowosci mamy podać łączną wagę? Do wyboru: 'POL', 'GER', 'FIN', 'AUT', 'NOR', 'USA'")
        for linia in plik:
            imie, nazwisko, narodowosc, data_urodzenia, wzrost, waga = linia.split(";")
            wzrost = int(wzrost)
            waga = int(waga)
            if narodowosc == kraj:
                waga_suma += waga
        if kraj == 'POL':
            kraj = 'Polska'
        elif kraj == 'GER':
            kraj = 'Niemcy'
        elif kraj == 'FIN':
            kraj = 'Finlandia'
        elif kraj == 'AUT':
            kraj = 'Austria'
        elif kraj == 'NOR':
            kraj = 'Norwegia'
        elif kraj == 'USA':
            kraj = 'Stany Zjednoczone'
        print(f'Lączna waga skoczków z kraju o nazwie {kraj} wynosi {waga_suma} kg')
    elif wybor == 2:
        for linia in plik:
            imie, nazwisko, narodowosc, data_urodzenia, wzrost, waga = linia.split(";")
            wzrost = int(wzrost)
            waga = int(waga)
            if narodowosc == 'POL':
                POL += 1
                wzrost_pol += wzrost
            elif narodowosc == 'GER':
                GER += 1
                wzrost_ger += wzrost
            elif narodowosc == 'FIN':
                FIN += 1
                wzrost_fin += wzrost
            elif narodowosc == 'AUT':
                AUT += 1
                wzrost_aut += wzrost
            elif narodowosc == 'NOR':
                NOR += 1
                wzrost_nor += wzrost
            elif narodowosc == 'USA':
                USA += 1
                wzrost_usa += wzrost
        print(f'Ilość skoczków poszczególnych narodowsci przedstawia się następująco:\n'
              f'"POL" -- {POL} -- średni wzrost polskich skoczków wynosi {wzrost_pol / POL:.2f}\n'
              f'"GER" -- {GER} -- średni wzrost niemieckich skoczków wynosi {wzrost_ger / GER:.2f}\n'
              f'"FIN" -- {FIN} -- średni wzrost fińskich skoczków wynosi {wzrost_fin / FIN:.2f}\n'
              f'"AUT" -- {AUT} -- średni wzrost austryjackich skoczków wynosi {wzrost_aut / AUT:.2f}\n'
              f'"NOR" -- {NOR} -- średni wzrost norweskich skoczków wynosi {wzrost_nor / NOR:.2f}\n'
              f'"USA" -- {USA} -- średni wzrost amerykanskich skoczków wynosi {wzrost_usa / USA:.2f}')


