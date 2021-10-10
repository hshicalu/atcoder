


def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    s = [s1,s2,s3]
    ans = ''
    for i in range(len(t)):
        if t[i] == "1":
            ans += s[0]
        elif t[i] == "2":
            ans += s[1]
        else:
            ans += s[2]
    print(ans)



if __name__ == "__main__":
    main()
