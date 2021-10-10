

import math

s = input()

a=[]
b=[]

for ele in s:
    if ele=="o":
        a.append(ele)
    elif ele=="?":
        b.append(ele)

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

# a = cmb(n,r)
a = len(a)
b = len(b)
#print(a)
#print(b)

if a > 4:
    print(0)
elif a == 4:
    print(math.factorial(4))
elif a == 3:
    if b == 0:
        print(36)
    else:
        print(math.factorial(4) * b + 36)
elif a == 2:
    if b == 0:
        print(14)
    elif b == 1:
        print(14 + 36)
    else:
        print(14 + 36 * b + math.factorial(4) * cmb(b,2))
elif a == 1:
    if b == 0:
        print(1)
    elif b == 1:
        print(1 + 14)
    elif b == 2:
        print(1 + 14 * 2 + 36)
    else:
        print(1 + 14 * b + 36 * cmb(b,2))
else:
    if b == 0:
        print(0)
    else:
        print(b**4)
