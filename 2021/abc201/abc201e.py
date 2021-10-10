import sys
import itertools
import math
from functools import reduce

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    # for i, v in enumerate(argv):
        # print("argv[{0}]: {1}".format(i, v))
    l = int(argv[0])
    r = int(argv[1])
    m = int(argv[2])
    n = argv[3:]

    #nのリストの要素を整数に直す
    for i in range(len(n)):
        n[i] = int(n[i])
    # print(l, r, m, n)

    if m == 1:
        n = int(n[0])
        if n == 1:
            print(0)
        else:
            num = 0
            a = r // n
            b = l // n
            num = a - b
            print(r - l + 1 - num)

    #nが複数あるときの処理
    else:
        if 1 in n:
            print(0)
        else:
            #m=1と同じ処理
            each = 0
            for i in range(len(n)):
                each += r // n[i] - l // n[i]

            num = 0
            for i in range(2, m + 1):
                c_lists = list(itertools.combinations(n, i))
                sum_lists = []
                for c in c_lists:
                    # print(c)
                    vle = my_lcm(*c)
                    # print(vle)
                    c = r // vle - l // vle
                    # print(c)
                    sum_lists.append(c)
                # print(sum_lists)
                if i % 2 == 0:
                    num -= sum(sum_lists)
                else:
                    num += sum(sum_lists)
            # print(each)
            # print(num)
            print(r - l + 1 - each - num)

if __name__ == '__main__':
    argv = sys.stdin.readline()
    main(sys.argv[1:])
    #main(argv[1:])
