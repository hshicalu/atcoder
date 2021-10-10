


def main():
    s = input()
    ch = "chokudai"
    inf = 10 ** 9 + 7

    dp = [[0 for _ in range(len(ch)+1)] for _ in range(len(s)+1)]
    #print(dp)

    for i in range(len(s)+1):
        dp[i][0] = 1
    #print(dp)
    for i in range(len(s)):
        for j in range(len(ch)):
            if s[i] != ch[j]:
                dp[i+1][j+1] = dp[i][j+1]
            if s[i] == ch[j]:
                dp[i+1][j+1] = (dp[i][j+1] + dp[i][j]) % inf

    print(dp[len(s)][8])

if __name__ == "__main__":
    main()
