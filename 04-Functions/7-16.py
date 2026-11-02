def funkcja(ciag):
    a = 0
    b = 1
    wybrane = a
    for i in range(2,ciag):
        if i % 2 == 0:
            a = a + b
            wybrane = a
        else:
            b = a + b
            wybrane = b
    return wybrane

def main():
    print(funkcja(9))

if __name__ == "__main__":
    main()