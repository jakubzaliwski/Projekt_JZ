def fibonacci(n):
    lista = []
    a, b = 0, 1
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista


n = int(input("Podaj ilość liczb Fibonacciego:"))
lista = fibonacci(n)
for i in lista:
    print(i)

