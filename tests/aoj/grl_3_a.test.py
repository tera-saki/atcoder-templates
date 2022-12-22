# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
import sys
from library.dfs_tree import DFSTree

input = sys.stdin.readline

N, M = map(int, input().split())
dfs_tree = DFSTree(N)
for _ in range(M):
    s, t = map(int, input().split())
    dfs_tree.add_edge(s, t)
dfs_tree.build()

points = dfs_tree.articulation_points()
for p in points:
    print(p)
