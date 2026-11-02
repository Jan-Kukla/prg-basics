def suma(liczba, parzysta):
    liczba = str(liczba)
    suma = 0
    for i in liczba:
        if parzysta and int(i) % 2 == 0:
            suma += int(i)
        elif (not parzysta) and int(i) % 2 == 1:
            suma += int(i)
    return suma

def main():
    print(suma(3124,False))

if __name__ == "__main__":
    main()