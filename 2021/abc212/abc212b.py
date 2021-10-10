

s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])

flg = False
#print(a,b,c,d)

if a == b:
    if b == c:
        if c == d:
            flg = True
elif b - a == 1 and c - b == 1 and d - c == 1:
    flg = True
elif a == 9 and b == 0 and c == 1 and d == 2:
    flg = True
elif a == 8 and b == 9 and c == 0 and d == 1:
    flg = True
elif a == 7 and b == 8 and c == 9 and d == 0:
    flg = True

if flg:
    print("Weak")
else:
    print("Strong")
