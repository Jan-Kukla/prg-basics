def funkcja(zdanie):
    dlugosc = len(zdanie)
    czy = True
    for i in zdanie:
        if zdanie.count(i) > 1:
            czy = False
    if czy and dlugosc >= 6:
        return True
    else:
        return False

def main():
    print(funkcja(""))

if __name__ == "__main__":
    main()