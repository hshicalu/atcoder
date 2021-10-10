

n = int(input())
a = list(map(int,input().split()))

b = sorted(a)

#print(a)
#print(b)

p = b[n-2]

print(a.index(p)+1)
