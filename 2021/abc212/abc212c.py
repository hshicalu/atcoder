


def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()
    
    x = 0
    y = 0
    
    ans = 10 ** 9 + 7

    while x < n and y < m:
        ans = min(ans, abs(a[x] - b[y]))
        if a[x] > b[y]:
            y+= 1
        else:
            x+= 1
    
    print(ans)

if __name__ == "__main__":
    main()
