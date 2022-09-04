# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

from lca import LCA

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