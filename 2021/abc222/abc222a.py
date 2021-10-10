

def main():
    n = input()

    if len(n) == 4:
        print(n)
    elif len(n) == 3:
        print("0" + str(n))
    elif len(n) == 2:
        print("00" + str(n))
    else:
        print("000" + str(n))


if __name__ == "__main__":
    main()
