

a,b,c = map(int,input().split())

if c+a==2*b or a+b==2*c or c+b==a*2:
    print("Yes")
else:
    print("No")
