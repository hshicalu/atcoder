

def main():

    n = int(input())

    s = 0
    
    a = []
    for i in range(n):
        x, y = map(int,input().split())
        a.append([x, y])
        s += x / y
    
    s /= 2
    
    ans = 0
    
    for i in range(n):
        x = a[i][0]
        y = a[i][1]
        if s - x / y >= 0:
            s -= x / y
            ans += x
        else:
            ans += s * y
            break
    
    print(ans)    



if __name__ == "__main__":
    main()
