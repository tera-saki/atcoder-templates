# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
import sys
from library.dfs_tree import DFSTree

input = sys.stdin.readline

N, M = map(int, input().split())
dfs_tree = DFSTree(N)
for _ in range(M):
    s, t = map(int, input().split())
    dfs_tree.add_edge(s, t)
dfs_tree.build()
bridges = dfs_tree.bridges()
bridges = [(s, t) if s < t else (t, s) for s, t in bridges]
for s, t in sorted(bridges):
    print(s, t)
