
import itertools

n,m = map(int,input().split())

ab = []

for i in range(m):
    a,b = map(int,input().split())
    ab.append([a,b])

if m == 0:
    print(0)
    exit()
cnt = 0
for i in range(1, m):
    for v in itertools.combinations(ab, i):
        #print(v)
        sub = 0
        if v[0][0] == 1 and v[len(v)-1][1] == n:
            print(v)
            for j in range(len(v)-1):
                if v[j][1] == v[j+1][0]:
                    sub += 1
            if sub == len(v)-1:
                cnt += 1

print(cnt)
