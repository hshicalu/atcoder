


def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    
    sum_a = sum(a)
    
    l = x % sum_a

    ba = x // sum_a

    cnt = 0
    i = 0
    while cnt <= l:
        cnt += a[i]
        i += 1

    print(n * ba + i)

if __name__ == "__main__":
    main()
