x = int(input("Podaj x "))
y = int(input("Podaj y "))
cwiartka = 0
if x > 0 and y > 0:
    cwiartka = 1
elif x < 0 and y > 0:
    cwiartka = 2
elif x < 0 and y < 0:
    cwiartka = 3
elif x > 0 and y < 0:
    cwiartka = 4

print(f'{cwiartka} ćwiartka.')
