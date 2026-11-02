def funkcja(zdanie):
    kontrolna = int(zdanie[3])
    co = (int(zdanie[0]) + int(zdanie[1]) + int(zdanie[2])) % 7
    if co == kontrolna:
        return True
    else:
        return False
def main():
    print(funkcja("7071"))

if __name__ == "__main__":
    main()