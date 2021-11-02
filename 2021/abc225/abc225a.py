

def main():

    s = list(input())

    s = set(s)

    if len(s) == 3:
        print(6)
    elif len(s) == 2:
        print(3)
    else:
        print(1)

if __name__ == "__main__":
    main()
