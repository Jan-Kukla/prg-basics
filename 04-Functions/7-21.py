def funkcja(z,b,c):
    M = max(z,b,c)
    m = min(z,b,c)
    return M - m

def main():
    print(funkcja(2,12,8))

if __name__ == "__main__":
    main()