wiek_ludzki = int(input("Enter the dog's age in human years: "))
wiek_psi = 0
for rok in range(1,wiek_ludzki + 1):
    print(rok)
    if rok <= 2:
        wiek_psi += 10.5
    else:
        wiek_psi += 4
print(f"The dog's age in dog's years is {wiek_psi} years.")