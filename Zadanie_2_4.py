
#Możliwości wpisania liczb w jednej linijce...

pula_liczb = input("Podaj liczby które chciałbyś dodać do puli - oddziel je przecinkami: ").split(",")
print (pula_liczb)
for i in range(len(pula_liczb)):
    pula_liczb[i] = int(pula_liczb[i])
print (len(pula_liczb))
print (sum(pula_liczb))
print (f"{((sum(pula_liczb))/(len(pula_liczb))):.2f}")
print (min(pula_liczb))
print (max(pula_liczb))

# INACZEJ - najpierw określić ile liczb chce się wprowadzić..

pula_liczb = []
ilosc_liczb = int(input("Podaj ile liczb chcialbys wprowadzic: "))
while len(pula_liczb) < ilosc_liczb:
    pula_liczb.append(int(input("Podaj liczbę którą chciałbyś dodać do puli: ")))

print (pula_liczb)
print (len(pula_liczb))
print (sum(pula_liczb))
print(f"{((sum(pula_liczb))/(len(pula_liczb))):.2f}")
print(min(pula_liczb))
print(max(pula_liczb))


#### "na piechote" ze stworzeniem listy z n liczbami

n = [2, 34, 55, 11, 200, 223, 45]

print (n)
print (len(n))
print (sum(n))
print(f"{((sum(n))/(len(n))):.2f}")
print(min(n))
print(max(n))

