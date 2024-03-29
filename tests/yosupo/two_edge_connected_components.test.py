# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components
import sys
from library.dfs_tree import DFSTree

input = sys.stdin.readline

N, M = map(int, input().split())
dfs_tree = DFSTree(N)
for _ in range(M):
    a, b = map(int, input().split())
    dfs_tree.add_edge(a, b)
dfs_tree.build()
T = dfs_tree.two_edge_connected_components()
print(len(T))
for tecc in T:
    print(len(tecc), *tecc)
