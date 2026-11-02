def ujemna(a, b, c):
    if a < 0:
        return True
    elif b < 0:
        return True
    elif c < 0:
        return True
    else:
        return False

def main():
    print(ujemna(5,4,14))

if __name__ == "__main__":
    main()