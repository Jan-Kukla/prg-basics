def dodawanie_cyfr(liczba_z_klawiatury):
    bezwzgledna = abs(liczba_z_klawiatury)
    liczba_z_klawiatury_string = str(bezwzgledna)
    suma = 0
    for l in range(len(liczba_z_klawiatury_string)):
        liczba_int = int(liczba_z_klawiatury_string[l])
        suma += liczba_int
    return suma

liczba_z_klawiatury = int(input("Podaj liczbę: "))
print(dodawanie_cyfr(liczba_z_klawiatury))
