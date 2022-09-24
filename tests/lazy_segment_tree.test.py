# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum
import sys
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline


N, Q = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353


def enc(x):
    return x >> 32, x % (1 << 32)


def op(a, b):
    a0, a1 = enc(a)
    b0, b1 = enc(b)
    return (((a0 + b0) % mod) << 32) + a1 + b1


def mapping(f, x):
    f0, f1 = enc(f)
    x0, x1 = enc(x)
    return (((f0 * x0 + f1 * x1) % mod) << 32) + x1


def composition(f, g):
    f0, f1 = enc(f)
    g0, g1 = enc(g)
    return (((f0 * g0) % mod) << 32) + ((g1 * f0 + f1) % mod)


lst = LazySegTree(N, op, 0, mapping, composition, 1 << 32)
A = [(a << 32) + 1 for a in A]
lst.build(A)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        l, r, b, c = q
        lst.apply(l, r, (b << 32) + c)
    else:
        l, r = q
        print(lst.prod(l, r) >> 32)
