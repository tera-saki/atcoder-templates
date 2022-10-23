# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_F
# RMQ and RUQ
import sys
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline

e = 1 << 31
id = 1 << 31


def op(a, b):
    return min(a, b)


def mapping(f, x):
    if f == id:
        return x
    return f


def composition(f, g):
    return g if f == id else f


N, Q = map(int, input().split())
lst = LazySegTree(N, op, e, mapping, composition, id)
A = [(1 << 31) - 1] * N
lst.build(A)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        lst.apply(s, t + 1, x)
    else:
        s, t = q
        print(lst.prod(s, t + 1))
