# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_G
# RSQ and RAQ
import sys
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline

e = (0, 0)
id = 0


def op(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mapping(f, x):
    return (x[0] + f * x[1], x[1])


def composition(f, g):
    return f + g


N, Q = map(int, input().split())
lst = LazySegTree(N, op, e, mapping, composition, id)
A = [(0, 1) for _ in range(N)]
lst.build(A)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        s -= 1
        lst.apply(s, t, x)
    else:
        s, t = q
        s -= 1
        print(lst.prod(s, t)[0])
