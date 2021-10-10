
def main():
    
    n,m = map(int,input().split())
    a = [list(input()) for _ in range(2 * n)]
    l = [[0, i] for i in range(2 * n)]

    for i in range(m):
        for j in range(n):
            if a[l[j * 2][1]][i] == a[l[j * 2 + 1][1]][i]:
                continue
            elif a[l[j * 2][1]][i]=="G" and a[l[j * 2 + 1][1]][i]=="C" or  a[l[j * 2][1]][i]=="C" and a[l[j * 2 + 1][1]][i]=="P" or  a[l[j * 2][1]][i]=="P" and a[l[j * 2 + 1][1]][i]=="G":
                l[j * 2][0] -= 1
            else:
                l[j * 2 + 1][0] -= 1
        l.sort()

    for i in range(2 * n):
        print(l[i][1] + 1)


if __name__ == "__main__":
    main()

