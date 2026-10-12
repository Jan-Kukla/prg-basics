import math
obwód = int(input("Podaj obwód drzewa: "))
promień = obwód / (2 * math.pi)
średnica = promień * 2
czy = średnica >= 50
print(f'Można ściąć: {czy}')