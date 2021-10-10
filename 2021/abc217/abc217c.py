

def main():

    n = int(input())
    p = list(map(int,input().split()))

    d = {}
    for i in range(n):
        d[i] = p[i]
    #print(d)
    
    d_sort = sorted(d.items(), key = lambda x:x[1])

    #print(d_sort)
    q = []

    for i in range(len(d_sort)):
        q.append(d_sort[i][0] + 1)
    
    print(*q)
if __name__ == "__main__":
    main()
