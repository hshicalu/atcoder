

a,b,w = map(int,input().split())

z = 1000 * w

ans_max = 0
ans_min = 0

if z % a == 0:
    ans_max = z // a
else:
    ans_max = z // a
 
if z % b == 0:
    ans_min = z // b
else:
    ans_min = z // b + 1

if (ans_min - 1 != ans_max):
    print(ans_min, ans_max)
else:
    print("UNSATISFIABLE")
