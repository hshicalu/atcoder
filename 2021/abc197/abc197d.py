

import math

n = int(input())
x,y = map(int,input().split())
a,b = map(int,input().split())

mx = (x+a)/2
my = (y+b)/2
ang = math.radians(360/n)
#print(mx,my)
#print(ang)
bx = x-mx
by = y-my
#print(bx,by)
x1 = mx+(bx*math.cos(ang)-by*math.sin(ang))
y1 = my+(by*math.cos(ang)+bx*math.sin(ang))
print(x1,y1)
