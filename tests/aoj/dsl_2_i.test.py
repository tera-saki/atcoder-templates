# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_I
# RSQ and RUQ
import sys
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline

e = (0, 0)
INF = 1 << 30
id = INF


def op(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mapping(f, x):
    if f == id:
        return x
    return (f * x[1], x[1])


def composition(f, g):
    return g if f == id else f


N, Q = map(int, input().split())
lst = LazySegTree(N, op, e, mapping, composition, id)
A = [(0, 1)] * N
lst.build(A)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        lst.apply(s, t + 1, x)
    else:
        s, t = q
        print(lst.prod(s, t + 1)[0])
