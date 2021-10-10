


def main():
    x = input()
    n = int(input())

    s = []

    for i in range(n):
        t = input()
        s.append(t)
    
    d = {}
    for i in range(26):
        d[x[i]] = chr(i + ord('a'))
    #print(d)
    
    new = {}
    for i in range(n):
        a = ''
        #print(s[i])
        for j in range(len(s[i])):
            a += d[s[i][j]]
        new[s[i]] = a
    #print(new)
    ans = sorted(new.items(), key=lambda x:x[1])
    #print(ans)
    #print(ans.keys())
    for i in range(n):
        print(ans[i][0])

if __name__ == "__main__":
    main()
