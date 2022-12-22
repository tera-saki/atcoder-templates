# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected
import sys
from library.dfs_tree import DFSTree

input = sys.stdin.readline


N, M = map(int, input().split())
dfs_tree = DFSTree(N)
for i in range(M):
    u, v = map(int, input().split())
    dfs_tree.add_edge(u, v)
dfs_tree.build()

for i in range(N):
    if not dfs_tree.back_edge[i]:
        continue
    backto, eidx = dfs_tree.back_edge[i][0]
    V = [backto]
    E = [eidx]
    cur = i
    while True:
        if cur == backto:
            break
        v, eidx = dfs_tree.par[cur]
        V.append(cur)
        E.append(eidx)
        cur = v
    print(len(V))
    print(*V)
    print(*E)
    break
else:
    print(-1)
