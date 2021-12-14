from multiprocessing import Pool
import argparse
import math


def D(a, b, c):
    return b * b - 4 * a * c


def root(lst):
    return (- lst[2] + lst[0]) / (2 * lst[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Аргументы')
    parser.add_argument('a', type=float, default=1.0, help="Это float аргумент, который подразумевает, что аргумент a по умолчанию (1)")
    parser.add_argument('b', type=float, default=2.0, help="Это float аргумент, который подразумевает, что аргумент b по умолчанию (2)")
    parser.add_argument('c', type=float, default=1.0, help="Это float аргумент, который подразумевает, что аргумент c по умолчанию (1)")
    args = parser.parse_args()

    with Pool(4) as p:
        d = D(args.a, args.b, args.c)
        new_list = list(p.map(root, [[math.sqrt(d), args.a, args.b], [-math.sqrt(d), args.a, args.b]]))
        print(new_list)
