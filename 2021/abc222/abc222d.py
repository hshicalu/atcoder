

def main():
    
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    ans = 1
    for i in range(n):
        ans *= b[i] - a[i] + 1
    print(ans % 998244353)

if __name__ == "__main__":
    main()
