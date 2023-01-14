# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
import sys
from library.hld import HLD
from library.binary_indexed_tree import BIT

input = sys.stdin.readline


N, Q = map(int, input().split())
A = list(map(int, input().split()))
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

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
        u, v = q
        a = 0
        for l, r in solver.path_query_range(u, v):
            a += bit.range_sum(l, r)
        ans.append(a)
print(*ans, sep='\n')
