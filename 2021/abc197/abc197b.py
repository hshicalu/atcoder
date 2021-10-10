

h,w,x,y = map(int,input().split())
s = []

for i in range(h):
    t = input()
    s.append(list(t))

#print(s)

cnt = 0

for i in range(y-1,w):
    if s[x-1][i] == ".":
        cnt += 1
    else:
        break

for i in range(y):
    if s[x-1][y-1-i] == ".":
        cnt += 1
    else:
        break

for i in range(x-1,h):
    if s[i][y-1] == ".":
        cnt += 1
    else:
        break

for i in range(x):
    if s[x-1-i][y-1] == ".":
        cnt += 1
    else:
        break
print(cnt-3)
