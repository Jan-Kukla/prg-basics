def funkcja(ciag):
    wynik = ""
    for i in ciag:
        if i != " ":
            wynik += i
    return wynik

def main():
    print(funkcja("A programming language is a system of notation for writing"))

if __name__ == "__main__":
    main()