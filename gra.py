from random import randint

los = randint(1,100)
odp = -1
i = 0
print("zgadnij liczbe z przedziału od 1 do 100")

while odp != los:
    i += 1
    odp = float(input(" podaj liczbę: "))
    if odp > los:
        print("liczba jest mniejsza od Twojej")
    elif odp < los:
        print(" liczba jest wieksza od Twojej")
print ("Brawo! odgadłeś liczbę za", i, "razem")
