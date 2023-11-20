

import matplotlib.pyplot as mat


def fibonacci(n):
    lista = []
    a, b = 0, 1
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista


def wykres(n):
    liczby = fibonacci(n)

    mat.plot(liczby, marker="o")
    mat.title(f'Ciąg Fibonacciego dla {n} liczb')
    mat.xlabel('Indeks')
    mat.ylabel('Wartość')
    mat.grid(True)
    mat.show()


n = int(input("Podaj ilość liczb Fibonacciego do wygenerowania i wyświetlenia na wykresie: "))
wykres(n)