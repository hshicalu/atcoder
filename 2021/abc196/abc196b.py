

#x = float(input())
x = input()
#print(x)

if "." in x:
    ans = x.split(".")
    print(int(ans[0]))
else:
    print(int(x))
