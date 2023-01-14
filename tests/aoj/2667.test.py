# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/2667
import sys
from library.hld import HLD
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline


def op(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mapping(f, x):
    return (x[0] + f * x[1], x[1])


def composition(f, g):
    return f + g


N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

solver = HLD(N, E)
lst = LazySegTree(N, op, (0, 0), mapping, composition, 0)
lst.build([(0, 1) for _ in range(N)])
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        ans = 0
        for l, r in solver.path_query_range(x, y, is_edge_query=True):
            ans += lst.prod(l, r)[0]
        print(ans)
    else:
        l, r = solver.subtree_query_range(x, is_edge_query=True)
        lst.apply(l, r, y)
