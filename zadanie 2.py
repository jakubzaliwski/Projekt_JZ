from random import randint

def losowe_liczby(nazwa_pliku, n):
    with open(nazwa_pliku, 'w') as plik:
        for _ in range(n):
            liczba = randint(1, 1000)
            plik.write(str(liczba) + '\n')  random.


try:
    n = int(input("Podaj ilość elementów: "))
    losowe_liczby("zad2.txt", n)
    print("Pomyślnie zapisano " + str(n) + " elementów")
except:
    print("Błąd")