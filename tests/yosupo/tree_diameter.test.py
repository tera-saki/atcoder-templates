# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter
import sys
from library.tree_diameter import TreeDiameter

input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    E[a].append((c, b))
    E[b].append((c, a))
solver = TreeDiameter(N, E)
path = solver.get_path()
print(solver.diameter_weight, len(path))
print(*solver.get_path())
