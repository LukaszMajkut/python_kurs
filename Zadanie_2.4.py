

pula_liczb = []
liczby = input("Podaj liczby które chciałbyś dodać do puli - oddziel je przecinkami: ") #możliwość dodania liczb jedynie z zakresu 0 - 9
for i in range(0,len(liczby),2):
    pula_liczb.append(int(liczby[i]))

print (pula_liczb)

print (pula_liczb)
print (len(pula_liczb))
print (sum(pula_liczb))
print(f"{((sum(pula_liczb))/(len(pula_liczb))):.2f}")
print(min(pula_liczb))
print(max(pula_liczb))


#### póki co "na piechote" ze stworzeniem listy z n liczbami

n = [2, 34, 55, 11, 200, 223, 45]

print (n)
print (len(n))
print (sum(n))
print(f"{((sum(n))/(len(n))):.2f}")
print(min(n))
print(max(n))

