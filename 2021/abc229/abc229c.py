


def main():

    n, w = map(int,input().split())

    values = list()

    for i in range(n):
        a, b = map(int,input().split())

        values.append([a, b, a / b])
    #print(values)
    values = sorted(values, key = lambda x: x[0], reverse = True)
    #print(values)
    ans = 0
    am = 0    
    for i in range(len(values)):
        if w == 0:
            break
        else:
            am += min(w, values[i][1])
            #print(min(w, values[i][1]))
            ans += min(w, values[i][1]) * values[i][0]
            w -= min(w, values[i][1])
            #print(f"a is {values[i][0]}, b is {values[i][1]}")
            #print(f"w is {w}")
        #ans += min(w, values[i][1]) * values[i][0]
        #w -= min(w, values[i][1])
    #print(w)
    #print(am)
    rest = 2357689932073 - ans
    #for i in range(n):
        #print(rest / values[i][0])
    print(ans)
    
if __name__ == "__main__":
    main()
