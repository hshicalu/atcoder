


def main():
    k = int(input())
    a,b = input().split()

    ax,bx = 0, 0
    if k == 10:
        print(int(a) * int(b))
        exit()

    for i in range(len(a)):
        ax += int(a[len(a)-i-1]) * (k ** i)
    for i in range(len(b)):
        bx += int(b[len(b)-i-1]) * (k ** i)
    print(ax * bx)
if __name__ == "__main__":
    main()
