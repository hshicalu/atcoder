

s1 = input()
s2 = input()
s3 = input()
s4 = input()

s = [s1,s2,s3,s4]

c1 = s.count("H")
c2 = s.count("2B")
c3 = s.count("3B")
c4 = s.count("HR")

if c1 == 1 and c2 == 1 and c3 == 1 and c4 == 1:
    print("Yes")
else:
    print("No")
