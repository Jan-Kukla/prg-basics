def funkcja(zdanie):
    wynik = 0
    for i in range(len(zdanie)):
        if i == 0:
            wynik = int(zdanie[i])
        elif i % 2 == 0:
            if zdanie[i - 1] == "+":
                wynik += int(zdanie[i])
            elif zdanie[i - 1] == "-":
                wynik -= int(zdanie[i])

    return wynik

def main():
    print(funkcja("2+3-4+5-0"))

if __name__ == "__main__":
    main()