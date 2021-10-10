

n = int(input())
s=[]
t=[]

for i in range(n):
    a,b = input().split()
    s.append(a)
    t.append(int(b))

#print(s)
#print(t)
u = t.copy()
u.sort()
num = u[len(u)-2]
indx = t.index(num)

print(s[indx])
