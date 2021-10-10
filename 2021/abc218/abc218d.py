
import itertools

def main():
    n = int(input())
    p = []
    for i in range(n):
        x,y = map(int,input().split())
        p.append((x,y))
    cnt = 0
    cmb = list(itertools.combinations(p, 4))
    #print(cmb)

    for c in cmb:
        vct = []
        #print(c)
        for i in range(4):
            for j in range(i+1,4):
                v = [c[i][0]-c[j][0],c[i][1]-c[j][1]]
                if v[0] == 0 or v[1] == 0:
                    vct.append(v)
        #print(vct)
        if len(vct) == 4 and vct.count(vct[0]) == 2 and vct.count(vct[1]) == 2:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()
