import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))

print("Pole rowne jest: ",triangle_area(a, b, c))