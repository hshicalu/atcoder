

def main():
    
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    ans = [0] * n
    f = min(t)
    ans[t.index(f)] = f
    
    for i in range(t.index(f) + 1, n):
        ans[i] = min(t[i], ans[i - 1] + s[i - 1])

    for i in range(t.index(f)):
        if i != 0:
            ans[i] = min(t[i], ans[i - 1] + s[i - 1])
        else:
            ans[i] = min(t[i], ans[n - 1] + s[n - 1])
    #print(ans)
    for i in range(n):
        print(ans[i])
if __name__ == "__main__":
    main()
