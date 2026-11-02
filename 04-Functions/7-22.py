def funkcja(zdanie):
    oddac = zdanie[0]
    for i in range(len(zdanie)):
        if zdanie[i] == " ":
            oddac += zdanie[i + 1]
    return oddac

def main():
    print(funkcja("Python"))

if __name__ == "__main__":
    main()