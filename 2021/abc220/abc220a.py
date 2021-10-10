

def main():
    a,b,c = map(int,input().split())

    x = a // c
    y = b // c

    if y - x >= 0 and a <= y * c and y * c <= b:
        print(y * c)
    else:
        print(-1)

if __name__ == "__main__":
    main()
