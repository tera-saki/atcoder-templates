# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum
import sys
from library.hld import HLD
from library.binary_indexed_tree import BIT

input = sys.stdin.readline


N, Q = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
E = [[] for _ in range(N)]
for i, p in enumerate(P, 1):
    E[i].append(p)
    E[p].append(i)

solver = HLD(N, E)
B = [None] * N
for i, a in enumerate(A):
    B[solver.ord[i]] = a
bit = BIT(N)
bit.build(B)
ans = []
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        p, x = q
        bit.add(solver.ord[p], x)
    else:
        v, = q
        print(bit.range_sum(*solver.subtree_query_range(v)))
