

def main():

    l, q = map(int,input().split())

    qry = []

    for i in range(q):
        c, x = map(int,input().split())
        qry.append((c,x))
    #print(qry)
    l_lists = [0, l]

    for i in range(q):
        if qry[i][0] == 1:
            l_lists.append(qry[i][1])
            l_lists.sort()
        else:
            for j in range(len(l_lists) - 1):
                if l_lists[j] <= qry[i][1] and qry[i][1] <= l_lists[j + 1]:
                    print(l_lists[j+1]-l_lists[j])

if __name__ == "__main__":
    main()
