def funkcja(ciag):
    suma = 0
    zdarzylo_sie = False
    for i in ciag:
        if i == "+":
            suma += 1
        elif i == "-":
            suma -= 1
        if suma >= 3:
            zdarzylo_sie = True
    return zdarzylo_sie

def main():
    print(funkcja("+-++-++-+---"))

if __name__ == "__main__":
    main()