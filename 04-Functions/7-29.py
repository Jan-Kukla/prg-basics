def funkcja(n):
    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

# n! = n * (n-1)!
    if n > 1:
        return n * funkcja(n-1)

def main():
    print(funkcja(5))

if __name__ == "__main__":
    main()