import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime
import time
import csv
import requests
from io import StringIO


# Poprawność zadań: 11/11
# Dodatki: 1.5/2
# Znormalizowane: 0,9615384615

def ex_1():
    print("Zadanie 1: ")
    i = 0
    while True:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            continue
        if i >= 101:
            break
    pass

def ex_2():
    print("Zadanie 2: ")
    def losowe_liczby(nazwa_pliku, n):
        with open(nazwa_pliku, 'w') as plik:
            for _ in range(n):
                liczba = random.randint(1, 1000)
                plik.write(str(liczba) + '\n')

    try:
        n = int(input("Podaj ilość elementów: "))
        losowe_liczby("zad2.txt", n)
        print("Pomyślnie zapisano " + str(n) + " elementów")
    except:
        print("Błąd")
    pass

def ex_3():
    print("Zadanie 3:")
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
            print("odchylenie standardowe wynosi: ", odchylenie, file=plik)
            print("Lista wczytana malejaco: ", lista_posortowana, file=plik)
            print("Lista wczytana rosnaco: ", lista_zrewersowana, file=plik)

        with open('zad3.txt', 'r') as plik:
            zawartosc = plik.read()
            print("Zawartość pliku:")
            print(zawartosc)

    except ValueError:
        print("błąd, nieprawidłowe dane podane")

    pass

def ex_4(n):
    lista = []
    a, b = 0, 1
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista, n

def ex_5():
    print("Zadanie 5: ")
    n = int(input("Podaj ilość liczb Fibonacciego: "))
    liczby, _ = ex_4(n)
    plt.plot(liczby, marker="o")
    plt.title(f'Ciąg Fibonacciego dla {n} liczb')
    plt.xlabel('Indeks')
    plt.ylabel('Wartość')
    plt.grid(True)
    plt.show()
    pass

def ex_6():
    print("Zadanie 6: ")
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
    return wynik

    pass

def ex_7(slownik):
    print("Zadanie 7: ")
    def suma_Wartości_slownika(slownik):
        suma = sum(slownik.values())
        return suma

    suma_wartosci = suma_Wartości_slownika(slownik)
    print("Suma wszystkich wartości w slowniku: ", suma_wartosci)
    pass


def ex_8():
    print("Zadanie 8: ")
    for _ in range(1, 11):
        current_time = datetime.now()
        current_time_str = current_time.strftime("%Y_%m_%d_%H_%M_%S_%f")
        file_name = f"{current_time_str}.bin"

        with open(file_name, 'wb') as file:
            for _ in range(10):
                number = random.randint(1, 100)
                file.write(str(number).encode() + b'\n')
        print(file_name)
        time.sleep(1)
    pass

def ex_9():
    print("Zadanie 9: ")
    # Wczytywanie pliku
    url = 'https://raw.githubusercontent.com/uzh-rpg/agile_autonomy/958c0d22e11d28a4d73b627029cf62ef1a1a95ab/data_generation/viz_utils/pole_avoidance/reference_trajectory.csv'
    response = requests.get(url)
    content = response.text
    string_io = StringIO(content)
    reader = csv.reader(string_io)

    # Pomijaj pierwszy wiersz
    next(reader)

    # Listyyyyyyyyyy
    time_start_list = []
    pos_x_list = []
    pos_y_list = []
    pos_z_list = []
    velocities = []

    # Ustawienie kolumn, list
    for line in reader:
        time_start = line[0]
        pos_x = float(line[1])
        pos_y = float(line[2])
        pos_z = float(line[3])
        vel_x = float(line[4])
        vel_y = float(line[5])
        vel_z = float(line[6])

        time_start_list.append(time_start)
        pos_x_list.append(pos_x)
        pos_y_list.append(pos_y)
        pos_z_list.append(pos_z)

        # Szybkość, Nie wiem czy dobrze???????????????
        speed = np.linalg.norm([vel_x, vel_y, vel_z])
        velocities.append(speed)

    # Zapis danych do pliku csv
    with open("velocity.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Time Start", "Speed"])  # Nagłówki kolumn

        for time_start, speed in zip(time_start_list, velocities):
            writer.writerow([time_start, speed])

    # Listy do numpy
    pos_x_array = np.array(pos_x_list)
    pos_y_array = np.array(pos_y_list)
    pos_z_array = np.array(pos_z_list)

    # średnie pozycje
    mean_pos_x = np.mean(pos_x_array)
    mean_pos_y = np.mean(pos_y_array)
    mean_pos_z = np.mean(pos_z_array)

    #  wyniki na konsole
    print(f"Średnia pozycja w osi X: {mean_pos_x}")
    print(f"Średnia pozycja w osi Y: {mean_pos_y}")
    print(f"Średnia pozycja w osi Z: {mean_pos_z}")

    # Tworzenie wykresów
    fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

    # Wykres 1
    axs[0].plot(time_start_list, pos_x_list, color='blue')
    axs[0].set_ylabel('Pos X')
    axs[0].set_title('Wykresy w zależności od Time Start')

    # Wykres 2
    axs[1].plot(time_start_list, pos_y_list, color='red')
    axs[1].set_ylabel('Pos Y')

    # Wykres 3
    axs[2].plot(time_start_list, pos_z_list, color='green')
    axs[2].set_xlabel('Time Start')
    axs[2].set_ylabel('Pos Z')

    # Dodanie timestampów na osi x dla ostatniego wykresu
    axs[2].set_xticks(time_start_list[::10])
    axs[2].set_xticklabels(time_start_list[::10], rotation=45, ha="right")

    plt.show()
    pass


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    slownik_wynik = ex_6()
    ex_7(slownik_wynik)
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
