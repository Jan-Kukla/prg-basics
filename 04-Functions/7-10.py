def ile(a, b):
    ile = 0
    if a <= b:
        x = a
        y = b + 1
    else:
        x = b
        y = a + 1
    for i in range(x,y):
        if i < 0 and i % 2 == 0:
            ile += 1
           # print(i)
    return ile

def main():
    print(ile(-7,8))

if __name__ == "__main__":
    main()