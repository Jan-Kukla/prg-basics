def monety(do_zaplaty):
    monety = do_zaplaty // 5
    do_zaplaty = do_zaplaty % 5
    monety += do_zaplaty // 2
    do_zaplaty = do_zaplaty % 2
    monety += do_zaplaty
    return monety

def main():
    zaplacic = int(input("Ile: "))
    odpowiedz = monety(zaplacic)
    print(odpowiedz)

if __name__ == "__main__":
    main()