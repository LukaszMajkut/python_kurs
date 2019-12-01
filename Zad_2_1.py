

import random

liczba_a = random.randint(0,99)
liczba_b = random.randint(0,99)
suma = liczba_a + liczba_b

print (liczba_a, liczba_b)
odpowiedz = int(input("Ile wynosi suma tych dwóch liczb?"))
while odpowiedz != suma:
    print ("Błędna odpowiedz - spróbuj jeszcze raz :) ")
    odpowiedz = int(input("Ile wynosi suma tych dwóch liczb?"))

print (f"Brawo! Poprawna odpowiedz - suma tych dwoch liczb wynosi: {suma}")

