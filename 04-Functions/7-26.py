def funkcja(zdanie):
    wynik = ""
    for i in (zdanie):
        wynik += i + "-"
    wynik = wynik[:-1]
    return wynik

def main():
    print(funkcja(""))

if __name__ == "__main__":
    main()