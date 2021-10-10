

n = int(input())

ans = 0
if n <= 10 ** 2:
    ans += n // 11
    print(ans)
    exit()
ans += 9
if n <= 10 ** 4:
    if n - 1010 >= 0:
        ans += (n - 1010) // 101 + 1
    print(ans)
    exit()
ans += 90
if n <= 10 ** 6:
    if n - 100100 >= 0:
        ans += (n - 100100) // 1001 + 1
    print(ans)
    exit()
ans += 900
if n <= 10 ** 8:
    if n - 10001000 >= 0:
        ans += (n - 10001000) // 10001 + 1
    print(ans)
    exit()
ans += 9000
if n <= 10 ** 10:
    if n - 1000010000 >= 0:
        ans += (n - 1000010000) // 100001 + 1
    print(ans)
    exit()
ans += 90000
if n <= 10 ** 12:
    if n - 100000100000 >= 0:
        ans += (n - 100000100000) // 1000001 + 1
    print(ans)
    exit()
