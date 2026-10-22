ile_godzin = int(input("Ile godzin parkujesz? "))

if ile_godzin < 3:
    print("5 PLN")
elif ile_godzin < 7:
    print("15 PLN")
else:
    print("20 PLN")