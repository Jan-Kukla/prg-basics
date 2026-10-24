for liczba in range(31):
    co = liczba
    if liczba % 3 == 0 and liczba % 5 == 0:
        co = "BINGO"
    elif liczba % 5 == 0:
        co = "FIVE"
    elif liczba % 3 == 0:
        co = "THREE"
    print(f'{co}')