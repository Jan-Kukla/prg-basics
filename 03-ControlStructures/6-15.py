numer_z_klawiatury = input("Podaj numer: ")
if len(numer_z_klawiatury) == 13:
    print("Article number is correct.")
    if numer_z_klawiatury[0:3] == "590":
        print("Article manufactured in Poland.")
else:
    print("Article number is not correct.")