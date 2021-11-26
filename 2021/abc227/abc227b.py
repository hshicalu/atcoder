

def main():

    n = int(input())

    s = list(map(int,input().split()))

    cnt = 0
    d = {}

    for i in range(n):
        for j in range(1, 143):
            for k in range(1, 143):
                if 4 * j * k + 3 * (j + k) == s[i]:
                    d[i] = s[i]
    
    #print(d)
    print(n - len(d))

if __name__ == "__main__":
    main()
