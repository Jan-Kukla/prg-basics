def funkcja(x,n):
    wynik = 0
    if n == 1:
        wynik = x
    else:
        wynik = funkcja(x,n-1) * x
    return wynik

def main():
    print(funkcja(5,3))

if __name__ == "__main__":
    main()