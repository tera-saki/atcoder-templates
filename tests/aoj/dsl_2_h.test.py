# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_H
# RMQ and RAQ
import sys
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline

INF = 1 << 30
e = INF
id = 0


def op(a, b):
    return min(a, b)


def mapping(f, x):
    return f + x


def composition(f, g):
    return f + g


N, Q = map(int, input().split())
lst = LazySegTree(N, op, e, mapping, composition, id)
lst.build([0] * N)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        lst.apply(s, t + 1, x)
    else:
        s, t = q
        print(lst.prod(s, t + 1))
