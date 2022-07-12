
try:
    n = int(input("Ingresa un numero: "))
    z = 10/n
    print(n)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
