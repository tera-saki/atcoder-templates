# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components
import sys
from library.dfs_tree import DFSTree

input = sys.stdin.readline

N, M = map(int, input().split())
dfs_tree = DFSTree(N)
for _ in range(M):
    a, b = map(int, input().split())
    dfs_tree.add_edge(a, b)
dfs_tree.build()
B = dfs_tree.biconnected_components()
print(len(B))
for bcc in B:
    print(len(bcc), *bcc)
