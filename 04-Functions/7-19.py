def funkcja(ciag):
    ciag = str(ciag)
    suma = 0
    for i in range(10):
        ile = 0
        for j in ciag:
            if j == str(i):
                ile += 1
        if ile > 1:
            suma += ile * int(i)
    return suma

def main():
    print(funkcja(513553007))

if __name__ == "__main__":
    main()