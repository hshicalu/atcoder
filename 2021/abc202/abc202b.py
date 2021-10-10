

s = input()
t = []
for i in range(len(s)):
    if s[len(s)-i-1] == "0":
        t.append("0")
    if s[len(s)-i-1] == "1":
        t.append("1")
    if s[len(s)-i-1] == "6":
        t.append("9")
    if s[len(s)-i-1] == "9":
        t.append("6")
    if s[len(s)-i-1] == "8":
        t.append("8")
t = "".join(t)
print(t)
