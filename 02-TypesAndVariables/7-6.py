predkosc = int(input("Podaj prędkość samochodu w km/h: "))
dopuszczalna_predkosc = (predkosc <= 140 and predkosc >= 40)
print(f'Prędkość jest dopuszczalna: {dopuszczalna_predkosc}')