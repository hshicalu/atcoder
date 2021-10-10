

k, s = input().split()

k = int(k)
s = int(s)

cnt = 0

for i in range(k + 1):
    for j in range(k + 1):
        if s - i - j <= k and 0 <= s - i - j:
            cnt += 1

print(cnt)
