
# działający kalkulator jednak bez możliwości wpisania całego działania w jednej linijce

print ("Oto wirtualny kalkulator matematyczny.. Aby zakończyć działanie kalkulatora wpisz 'koniec'")

wynik = None

while True:
    dzialanie = input("Wpisz operator matematyczny z którego chcesz skorzystać - dostępne opcje: '+, '-', '*', '/\n")
    if '+' in dzialanie:
        liczba_a = float(input("Podaj pierwsza liczbe: "))
        liczba_b = float(input("Podaj druga liczbe: "))
        wynik = liczba_a + liczba_b
        print(wynik)
    elif '-' in dzialanie:
        liczba_a = float(input("Podaj pierwsza liczbe: "))
        liczba_b = float(input("Podaj druga liczbe: "))
        wynik = liczba_a - liczba_b
        print(wynik)
    elif '*' in dzialanie:
        liczba_a = float(input("Podaj pierwsza liczbe: "))
        liczba_b = float(input("Podaj druga liczbe: "))
        wynik = liczba_a * liczba_b
        print(wynik)
    elif '/' in dzialanie:
        liczba_a = float(input("Podaj pierwsza liczbe: "))
        liczba_b = float(input("Podaj druga liczbe: "))
        wynik = liczba_a / liczba_b
        print(wynik)
    elif dzialanie == 'koniec':
        break
    else:
        print("Wystapił błąd - obsługuję jedynie operatory takie jak: '+', '-', '*', '/'")


print ("Do zobaczenia!")

#---------------------------------------------------------------------------
# podejscie do kalkulatora liczb bazujac na LISTACH...
#---------------------------------------------------------------------------

print ("Oto wirtualny kalkulator matematyczny obliczający działania jedynie dla liczb z zakresu od 1 do 9 :D.. Aby zakończyć działanie kalkulatora wpisz 'koniec'")

wynik = None
liczby = []

while True:
    dzialanie = input("Podaj dzialanie do rozwiazania: ")
    liczby.append(dzialanie)
    if liczby[0][1] == "+":
        wynik = int(liczby[0][0]) + int(liczby[0][2])
        print (wynik)
        del liczby[:3]
    elif liczby[0][1] == "-":
        wynik =int(liczby[0][0]) - int(liczby[0][2])
        print (wynik)
        del liczby[:3]
    elif liczby [0][1] == "*":
        wynik = int(liczby[0][0]) * int(liczby[0][2])
        print (wynik)
        del liczby[:3]
    elif liczby [0][1] == "/":
        wynik = int(liczby[0][0]) / int(liczby[0][2])
        print (wynik)
        del liczby[:3]
    elif liczby [0] == "koniec":
        break
    else:
        print ("Wystapił błąd - obsługuję jedynie operatory takie jak: '+', '-', '*', '/'")
        del liczby[:3]

print ("Mam nadzieję, ze pomogłem! Do zobaczenia :) ")

