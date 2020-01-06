import os
import sys
import csv

#plik = open("zawodnicy.csv", encoding="utf8")
#zawartosc = plik.read()
#print(zawartosc)
#plik.close()

wzrost_min = None
wzrost_max = None
waga_min = None
waga_max = None
waga_suma = 0
pol = 0
wzrost_pol = 0
ger = 0
wzrost_ger = 0
fin = 0
wzrost_fin = 0
aut = 0
wzrost_aut = 0
nor = 0
wzrost_nor = 0
usa = 0
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
                pol += 1
                wzrost_pol += wzrost
            elif narodowosc == 'GER':
                ger += 1
                wzrost_ger += wzrost
            elif narodowosc == 'FIN':
                fin += 1
                wzrost_fin += wzrost
            elif narodowosc == 'AUT':
                aut += 1
                wzrost_aut += wzrost
            elif narodowosc == 'NOR':
                nor += 1
                wzrost_nor += wzrost
            elif narodowosc == 'USA':
                usa += 1
                wzrost_usa += wzrost
        print(f'Ilość skoczków poszczególnych narodowsci przedstawia się następująco:\n'
              f'"POL" -- {pol} -- średni wzrost polskich skoczków wynosi {wzrost_pol / pol:.2f}\n'
              f'"GER" -- {ger} -- średni wzrost niemieckich skoczków wynosi {wzrost_ger / ger:.2f}\n'
              f'"FIN" -- {fin} -- średni wzrost fińskich skoczków wynosi {wzrost_fin / fin:.2f}\n'
              f'"AUT" -- {aut} -- średni wzrost austryjackich skoczków wynosi {wzrost_aut / aut:.2f}\n'
              f'"NOR" -- {nor} -- średni wzrost norweskich skoczków wynosi {wzrost_nor / nor:.2f}\n'
              f'"USA" -- {usa} -- średni wzrost amerykanskich skoczków wynosi {wzrost_usa / usa:.2f}')


