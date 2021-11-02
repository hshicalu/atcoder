

def main():

    n, m = map(int,input().split())

    b = [list(map(int,input().split())) for l in range(n)]
    
    flg = True

    x = b[0][0] // 7
    y = b[0][0] - x * 7

    for i in range(n):
        for j in range(m):
            # print((i + x) * 7 + y + j, i, j)
            if not b[i][j] == (i + x) * 7 + y + j:
                flg = False

    if flg and y - 1 + m <= 7:
        if y == 0 and m != 1:
            print("No")
        else:
            print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
