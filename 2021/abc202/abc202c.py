
from collections import Counter

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

num = 0

d = []
for i in range(n):
    d.append(b[c[i]-1])
#print(d)
e = Counter(d)
#print(e)
#print(num)
for i in range(n):
    if a[i] in e:
        num += e[a[i]]

print(num)
