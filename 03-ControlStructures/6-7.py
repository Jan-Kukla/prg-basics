wiek = int(input("Ile masz lat? "))

if wiek < 13:
    print("Child")
elif wiek < 20:
    print("Teen")
elif wiek < 65:
    print("Adult")
else:
    print("Senior")