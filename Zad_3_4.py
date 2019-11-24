"""
Napisz dekorator `crazy_case`, który co drugą literę w słowie będzie zamieniał na dużą.
```python
@crazy_case
def powiedz_ala():
	return ‘Ala ma kota’
print(powiedz_ala()) # aLa mA KoTa

"""

def crazy_case(func):
    
    def wrapper(*args,**kwargs):

        wynik = func(*args,**kwargs)
        nowe_zdanie = ''
        licznik = 0
        for i in wynik.lower():
            licznik += 1
            if licznik % 2 == 0:
                nowe_zdanie += i.upper()
            else:
                nowe_zdanie += i

        return nowe_zdanie

    return wrapper


@crazy_case
def powiedz_ala():
    return 'Ala ma kota'

print (powiedz_ala())