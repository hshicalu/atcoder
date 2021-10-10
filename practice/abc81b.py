

n = int(input())
a = list(map(int,input().split()))

flg = True
cnt = 0

while flg:
    b = []
    for i in range(n):
        if a[i] % 2 == 0:
            b.append(a[i] // 2)
    #print(b)
    if len(b) == n:
        cnt += 1
        a = b
    else:
        flg = False

print(cnt)
