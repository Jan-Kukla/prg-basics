import hide

def main():
    karta = str(input("Podaj numer karty: "))
    ukryty = hide.hide(karta)
    print(ukryty)

if __name__ == "__main__":
    main()