def funkcja(zdanie):
    jeden = zdanie.count("1")
    dwa = zdanie.count("2")
    trzy = zdanie.count("3")
    cztery = zdanie.count("4")
    pienc = zdanie.count("5")
    szesc = zdanie.count("6")
    M = max(jeden,dwa,trzy,cztery,pienc,szesc)
    if jeden == M:
        return "1"
    elif dwa == M:
        return "2"
    elif trzy == M:
        return "3"
    elif cztery == M:
        return "4"
    elif pienc == M:
        return "5"
    elif szesc == M:
        return "6"

def main():
    print(funkcja("2133"))

if __name__ == "__main__":
    main()