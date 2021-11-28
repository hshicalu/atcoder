
import itertools

def main():
    s = input()
    k = int(input())
    
    n = len(s)

    if s.count(".") <= k:
        print(n)
        exit()
    
    cnt = [0 for i in range(n + 1)]
    for i in range(n):
        if s[i] == ".":
            cnt[i + 1] = cnt[i] + 1
        else:
            cnt[i + 1] = cnt[i]
    #print(cnt)        
    ans = 0
    r = 0

    for i in range(n):
        while (r <= n - 1 and cnt[r + 1] - cnt[i] <= k):
            r = r + 1
        ans = max(ans, r - i)
    print(ans)

if __name__ == "__main__":
    main()
