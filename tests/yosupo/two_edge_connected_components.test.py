# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components
import sys
from collections import defaultdict
from library.dfs_tree import DFSTree
from library.union_find import UnionFind

input = sys.stdin.readline

N, M = map(int, input().split())
E = [[] for _ in range(N)]
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges = [(u, v) if u < v else (v, u) for u, v in edges]
cnt = defaultdict(int)
for a, b in edges:
    E[a].append(b)
    E[b].append(a)
    cnt[(a, b)] += 1
dups = set((a, b) for (a, b) in edges if cnt[(a, b)] > 1)

bridges = DFSTree(N, E).bridges()
B = set((u, v) if u < v else (v, u) for u, v in bridges)
for u, v in dups:
    B.discard((u, v))
uf = UnionFind(N)
for u, v in edges:
    if (u, v) in B:
        continue
    uf.unite(u, v)

groups = [[] for _ in range(N)]
for i in range(N):
    par = uf.find(i)
    groups[par].append(i)
groups = [g for g in groups if g]
print(len(groups))
for g in groups:
    print(len(g), *g)
