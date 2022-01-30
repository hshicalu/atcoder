

def main():

    n, m = map(int,input().split())

    s = input().split()
    t = input().split()

    d = {}

    for i in range(n):
        d[s[i]] = False

    for i in range(m):
        d[t[i]] = True

    ans = list(d.values())

    for i in range(n):
        if ans[i]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
