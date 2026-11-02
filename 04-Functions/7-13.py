def ciag(ile):
    ile += 1
    co = ""
    for i in range(1,ile):
        co += str(i)
        #print(i)
    return co

def main():
    print(ciag(11))

if __name__ == "__main__":
    main()