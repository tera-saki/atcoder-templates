# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
from library.lca import LCA

input = sys.stdin.readline

N, Q = map(int, input().split())
P = list(map(int, input().split()))
E = [[] for _ in range(N)]
for i, p in enumerate(P, start=1):
    E[i].append(p)
    E[p].append(i)

solver = LCA(N, E)
for _ in range(Q):
    u, v = map(int, input().split())
    print(solver.lca(u, v))
