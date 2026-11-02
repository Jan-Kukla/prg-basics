def funkcja(a,b):
    wynik = 0
    for i in range(a,b+1):
        if i % 2 == 0 and i % 4 != 0 and i % 3 == 0:
            wynik += i

    return wynik

def main():
    print(funkcja(10,30))

if __name__ == "__main__":
    main()