

def main():
    cnt = 0
    s, t = map(int,input().split())

    for i in range(s + 1):
        for j in range(s + 1):
            for k in range(s + 1):
                if i * j * k <= t and i + j + k <= s:
                    cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()
