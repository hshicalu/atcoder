
import string


def main():

    p = list(map(int,input().split()))


    a = {}
    for i,c in enumerate(range(ord('a'),ord('z')+1)):
        #a[chr(c)] = i + 1
        a[i+1] = chr(c)
    #print(a)
    ans = ''

    for i in p:
        ans += a[i]
    print(ans)
if __name__ == "__main__":
    main()
