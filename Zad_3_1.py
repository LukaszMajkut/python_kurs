'''
Stwórz następujące metody. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb,
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.
'''

def stopy_na_metry(a: float) -> float:
    """
    Funkcja zamieniajaca stopy na metry
    :param a:
    :return:
    """
    return a/3.2808

print (stopy_na_metry(6))

def max(a: float, b: float) -> float:
    """
    Funkcja zwracajaca większą wartość
    :param a:
    :param b:
    :return:
    """
    if a > b:
        return a
    else:
        return b

print (max(6,8))

def srednia(a: float, b:float) -> float:
    """
    Funkcja obliczająca średnią arytmetyczną dwóch liczb
    :param a:
    :param b:
    :return:
    """
    return (a+b)/2

print (srednia(8,4))

def pole_kola(a: float) -> float:
    """
    Funkcja obliczająca pole kola
    :param a:
    :return:
    """
    import math
    return math.pi*(a**2)

print (pole_kola(4))

def bmi(a: float, b: float) -> float:
    """
    Funkcja obliczająca współczynnik BMI dla wzrostu w metrach i wagi w kg
    :param a: waga w kg
    :param b: wzrost w metrach
    :return:
    """
    return a/(b**2)

print (bmi(86, 1.82))

def pole_trojkata(a: float, b: float, c:float) -> float:
    """
    Funckja oczliająca pole trójkąta o podanych bokach (wg.wzoru Herona)
    :param a:
    :param b:
    :param c:
    :return:
    """
    import math
    polowa_obwodu = (a+b+c)/2
    return math.sqrt(polowa_obwodu*((polowa_obwodu-a)*(polowa_obwodu-b)*(polowa_obwodu-c)))

print (pole_trojkata(2,3,4))

def kilometry_na_mile(a: float) -> float:
    """
    Funkcja przeliczająca km na mile
    :param a:
    :return:
    """
    return a*0.621371192

print(kilometry_na_mile(55))

def mile_na_kilometry(a:float) -> float:
    """
    Funkcja przeliczająca mile na km
    :param a:
    :return:
    """
    return a/0.621371192

print(mile_na_kilometry(34))




