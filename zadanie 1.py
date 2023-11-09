
#def zad1():
#    for i in range(1, 101):
#        if i % 3 == 0 and i % 5 == 0:
#            print("FizzBuzz")
#        elif i % 3 == 0:
#            print("Fizz")
#        elif i % 5 == 0:
#            print("Buzz")
#        else:
#            print(i)
#zad1()
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
