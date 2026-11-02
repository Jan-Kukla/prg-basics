
def main():
    liczba = input("Podaj liczbę binarną: ")
    dlugosc = len(liczba)
    ile = 0
    for i in liczba:
        if i == "0" or i == "1":
            ile += 1
    if ile == dlugosc:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()