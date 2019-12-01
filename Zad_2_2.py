liczba = int(input("Podaj liczbę rzędów choinki:"))

for i in range(liczba):
    print (f'{(" ")*(liczba-i-1)}')
    print (f'{("*")*(i*2+1)}')
