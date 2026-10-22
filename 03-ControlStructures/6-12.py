ile = int(input("Ile kupujesz? "))
cena = int(input("Ile za sztukę? "))
wartosc = 0
if(ile > 2):
    wartosc = 2 * cena
    for ktory in range(3,ile + 1):
        wartosc += cena * 0.75
else:
    wartosc = ile * cena

print(f"Razem wychodzi {wartosc} zł")