liczba = int(input('Wpisz liczbę: '))

if liczba > 0:
    jaka = "Dodatnia"
elif liczba < 0:
    jaka = "Ujemna"
else:
    jaka = "0"

print(f'Liczba jest {jaka}')