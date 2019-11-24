'''
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.

Logikę obliczania liczby dni wydziel do osobnej funkcji.

**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.

'''


miesiac = input("Podaj nazwę miesiąca który Cie interesuje: ")

def dni_miesiaca(miesiac):
    if miesiac == 'styczen' or miesiac == 'marzec' or miesiac == 'maj' or miesiac =='lipiec' or miesiac == 'sierpien' \
        or miesiac == 'pazdziernik' or miesiac == 'grudzien':
        return ("Ten miesiąc ma 31 dni")
    elif miesiac == 'kwiecien' or miesiac == 'czerwiec' or miesiac == 'wrzesien' or miesiac == 'listopad':
        return ("Ten miesiac ma 30 dni")
    elif miesiac == 'luty':
        rok = int(input("A jaki rok Cię interesuje?"))
        lata_przestepne = [i for i in range (0,100000,4)]
        if rok in lata_przestepne:
            return (f"W roku {rok} luty mial 29 dni, poniewaz rok ten był rokiem przestepnym")
        else:
            return (f"W roku {rok} luty mial 28 dni")

print (dni_miesiaca(miesiac))

