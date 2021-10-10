

n=int(input())
s=input()
q=int(input())
s=list(s)

flag=False

for i in range(q):
    t,a,b=map(int,input().split())
    
    if t == 1:
        if not flag:
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
        else:
            if a < n:
                a += n
            else:
                a -= n
            if b < n:
                b += n
            else:
                b -= n
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
    elif t == 2:
        flag=not flag
if flag:
    s=s[n:]+s[:n]
print("".join(s))
