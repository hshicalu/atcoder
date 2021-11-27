

def main():
    x = input()

    ans = int(float(x))

    if len(x) == 5 and int(x[2]) >= 5:
        ans += 1
    elif len(x) == 6 and int(x[3]) >= 5:
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()
