# Napisz funkcję, która wczyta do listy liczby z pliku z poprzedniego zadania. Napisz funkcje do wyznaczenia
# średniej, odchylenia standardowego, wartości maksymalnej oraz minimalnej wczytanych liczb a następnie
# wywołaj je i otrzymane wartości wyświetl na ekranie. Następnie posortuj wczytane liczby malejąco i
# ponownie wyświetl je na ekranie. Nie korzystaj z z biblioteki nu
import random

def losowe_liczby(nazwa_pliku, n):
    lista = []
    with open(nazwa_pliku, 'w') as plik:
        for _ in range(n):
            liczba = random.randint(1, 100)
            plik.write(str(liczba) + '\n')
            lista.append(liczba)
        return lista

def odchylenie_stand(l):
    i = 0
    sum_wariancja = 0

    while i < len(l):
        sum_wariancja += (l[i] - srednia) ** 2
        i += 1

    wariancja = sum_wariancja / len(lista)
    odchylenie_standardowe = (wariancja ** 0.5)
    return odchylenie_standardowe

try:
    n = int(input("Podaj ilość elementow: "))
    lista = losowe_liczby('zad3.txt', n)
    srednia = sum(lista) / len(lista)
    odchylenie = odchylenie_stand(lista)

    lista_posortowana = sorted(lista, reverse=True)
    lista_zrewersowana = sorted(lista, reverse=False)
    with open('zad3.txt', 'w') as plik:
        print("Pomyslnie zapisano " + str(n) + " elementow", file=plik)
        print("lista liczb: ", lista, file=plik)
        print("Maksymalna wartosc to: ", max(lista), file=plik)
        print("minimalna wartosc to: ", min(lista), file=plik)
        print("srednia calej listy wynosi: ", srednia, file=plik)
        print("odchylenie standardowe wynosi: ", odchylenie, file=plik )
        print("Lista wczytana malejaco: ", lista_posortowana, file=plik)
        print("Lista wczytana rosnaco: ", lista_zrewersowana, file=plik)

except ValueError:
    print("błąd, nieprawidłowe dane podane")
