

def main():
    n ,x = map(int,input().split())
    a = list(map(int,input().split()))
    
    d = dict()

    for i in range(n):
        d[i] = a[i]

    ans = list()
    
    i = x
    cnt = 0
    
    while cnt <= n:
        ans.append(i - 1)
        i = d[i - 1]
        cnt += 1
    # print(ans)
    
    print(len(set(ans)))

if __name__ == "__main__":
    main()
