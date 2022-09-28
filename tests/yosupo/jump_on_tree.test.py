# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree
import sys
from library.lca import LCA

input = sys.stdin.readline

N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

solver = LCA(N, E)
for _ in range(Q):
    s, t, i = map(int, input().split())
    print(solver.jump(s, t, i))
