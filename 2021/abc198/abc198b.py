

n = input()

a=[]
for s in n:
    a.append(s)

#print(a)
if n == '0':
    print("Yes")
    exit()
while(True):
    if a[len(a)-1] == "0":
        a.pop()
    else:
        break    

b = list(reversed(a))

#print(a)
#print(b)
if a==b:
    print("Yes")
else:
    print("No")
