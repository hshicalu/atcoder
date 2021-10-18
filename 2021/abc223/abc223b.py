

def main():

    s = input()

    s = list(s) * 2
    
    d = []

    for i in range(len(s) // 2):
        d.append(''.join(s[i: i + len(s) // 2]))

    d = sorted(d)

    print(d[0])
    print(d[len(d) - 1])



if __name__ == "__main__":
    main()
