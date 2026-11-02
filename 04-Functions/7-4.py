import modul1

def main():
    ile = 0
    zdanie = input("Napisz zdanie: ")
    litera = input("Napisz litere: ")
    for l in zdanie:
        if l.capitalize == litera.capitalize:
            ile += 1
    print(zdanie)
    print(f'Liczba liter {litera} jest równa {ile}')

if __name__ == "__main__":
    #main()
    a = int(input("Zakres od: "))
    b = int(input("Zakres do: "))
    c = int(input("Liczba: "))
    czy = modul1.w_zakresie(a, b, c)
    if czy:
        print("yes")
    else:
        print("no")