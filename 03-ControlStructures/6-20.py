dziesietna = int(input("Podaj liczbę w systemie dziesiątkowym: "))
binarna = ""
while dziesietna != 0:
    reszta = str(dziesietna % 2)
    binarna = reszta + binarna
    dziesietna = dziesietna // 2
print(f'Ta liczba w postaci binarnej to {binarna}')
