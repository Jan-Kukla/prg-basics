def funkcja(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "%":
        return a % b
    elif operator == "**":
        return a ** b

def main():
    print(funkcja(2,3,"-"))

if __name__ == "__main__":
    main()