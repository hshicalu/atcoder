

h,w,n = map(int,input().split())


al = []
bl = []

for i in range(n):
    a,b = map(int,input().split())
    al.append(a)
    bl.append(b)


ad = {a:i+1 for i,a in enumerate(sorted(list(set(al))))}
bd = {b:i+1 for i,b in enumerate(sorted(list(set(bl))))}

#print(ad)
#print(bd)

for i in range(n):
  print(ad[al[i]], bd[bl[i]])
