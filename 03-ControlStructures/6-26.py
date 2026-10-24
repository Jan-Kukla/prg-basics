pin = 8642
pin_szanse = 3
while pin_szanse > 0:
    proba = int(input("Podaj pin"))
    if proba == pin:
        print("Poprawny PIN")
        break
    else:
        print("Niepoprawny PIN")
        pin_szanse -= 1
        if pin_szanse == 0:
            print("Sorry, blokujemy ci kartę.")