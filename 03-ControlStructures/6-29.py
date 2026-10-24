podana_liczba = int(input("Podaj liczbę: "))
for liczba in range(2, podana_liczba + 1):
    dzielnikow_ile = 0
    for dzielnik in range(1, liczba + 1):
        if liczba % dzielnik == 0:
            dzielnikow_ile += 1
    if dzielnikow_ile == 2:
        print(liczba)