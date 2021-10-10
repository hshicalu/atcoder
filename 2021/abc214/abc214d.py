
import itertools

def main():
    data = []
    n = int(input())

    for i in range(n - 1):
        d = list(map(int,input().split()))
        data.append(d)
    comb = list(itertools.combinations(range(1, n + 1), 2))
    print(data)
    print(comb)
    

if __name__ == "__main__":
    main()
