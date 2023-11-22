def ksiazka(n):
    slownik = {}
    i = 1
    while i <= n:
        nowe_elementy = {i: i ** 2}
        slownik.update(nowe_elementy)
        i += 1
    return slownik
def suma_Wartości_slownika(slownik):
    suma = sum(slownik.values())
    return suma



n = int(input("Podaj wartość n: "))
wynik = ksiazka(n)
print(wynik)
suma_wartosci = suma_Wartości_slownika(ksiazka(n))
print("Suma wszystkich wartości w slowniku: ", suma_wartosci)