pierwsza = 0
druga = 1
sekwencja = "0 1 "
for i in range(18):
    nastepna = pierwsza + druga
    sekwencja = sekwencja + str(nastepna) + " "
    if i % 2 == 1:
        druga = nastepna
    else:
        pierwsza = nastepna
print(sekwencja)