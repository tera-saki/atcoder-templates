# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching
import sys
from library.bipartite_matching import BipartiteMatching

input = sys.stdin.readline

L, R, M = map(int, input().split())
solver = BipartiteMatching(L, R)
for _ in range(M):
    a, b = map(int, input().split())
    solver.add_edge(a, b)
match = solver.solve()
print(match)
pairs = solver.pairs()
for l, r in pairs:
    print(l, r)
