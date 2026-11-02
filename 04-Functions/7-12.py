def ciag(ile):
    co = ""
    for i in range(ile):
        co += "*"
        if i < ile - 1:
            co += "/"
    return co

def main():
    print(ciag(1))

if __name__ == "__main__":
    main()