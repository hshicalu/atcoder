


def main():

    #s = input() 
    a, b = input().split()
    #n = int(input())
    a = list(a)
    b = list(b)
    #print(a)
    #print(b)
    flg = True
    len_max = max(len(a), len(b))

    a = [0] * (len_max - len(a)) + a
    b = [0] * (len_max - len(b)) + b

    #print(a)
    #print(b)
    
    for i in range(len_max):
        ch = int(a[i]) + int(b[i])

        if ch >= 10:
            flg = False
            break

    if flg:
        print("Easy")
    else:
        print("Hard")


if __name__ == "__main__":
    main()
