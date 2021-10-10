
import math

n = int(input())
a = list(map(int,input().split()))

ans = 0

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(n):
    a[i] = a[i] % 200

#print(a)
c=[]
for i in range(200):
    cnt = a.count(i)
    c.append(cnt)

#print(c_lists)
for i in range(200):
    if c[i] >= 2:
        ans += comb(c[i],2)

print(ans)
