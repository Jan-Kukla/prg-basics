def funkcja(ciag):
    ktora = 0
    co = 1
    while ktora < ciag:
        co += 1
        ile = 0
        for i in range(1,co + 1):
            if co % i == 0:
                ile += 1
        if ile == 2:
            ktora += 1
        if ktora == ciag:
            return co

def main():
    print(funkcja(5))

if __name__ == "__main__":
    main()