

def main():
    from math import comb
    a, b, k = map(int, input().split())
    ans = ""
    while a > 0 and b > 0:
        a_comb = comb(a-1+b, a-1)
        if k <= a_comb:
            ans += "a"
            a -= 1
        else:
            ans += "b"
            b -= 1
            k -= a_comb
    ans += "a" * a
    ans += "b" * b
    print(ans)
 
if __name__ == '__main__':
    main()
