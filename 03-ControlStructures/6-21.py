kwota = int(input("Ile złotych? "))
ile_5 = 0
ile_2 = 0
ile_1 = 0

ile_5 = kwota // 5
kwota = kwota - ile_5 * 5
ile_2 = kwota // 2
kwota = kwota - ile_2 * 2
ile_1 = kwota
kwota = 0

print(f'5 PLN coins: {ile_5}')
print(f'2 PLN coins: {ile_2}')
print(f'1 PLN coins: {ile_1}')