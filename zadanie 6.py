def ksiazka(n):
    slownik = {}
    i = 1
    while i <= n:
        nowe_elementy = {i: i ** 2}
        slownik.update(nowe_elementy)
        i += 1
    return slownik


n = int(input("Podaj wartość n: "))
wynik = ksiazka(n)
print(wynik)