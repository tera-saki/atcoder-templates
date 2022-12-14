# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected
import sys
from library.dfs_tree import DFSTree

input = sys.stdin.readline


N, M = map(int, input().split())
E = [[] for _ in range(N)]
eidx = {}
for i in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
    if u > v:
        u, v = v, u
    j = eidx.get((u, v))
    if j is None:
        eidx[(u, v)] = i
    else:
        print(2)
        print(u, v)
        print(i, j)
        exit()

solver = DFSTree(N, E)
back_edges = solver.back_edge
for i in range(N):
    if not back_edges[i]:
        continue
    backto = back_edges[i][0]
    path = solver.get_path(i)
    ansv = path[path.index(backto):]
    anse = []
    for s, t in zip(ansv, ansv[1:]):
        if s > t:
            s, t = t, s
        anse.append(eidx[(s, t)])
    anse.append(eidx[min(i, backto), max(i, backto)])
    print(len(ansv))
    print(*ansv)
    print(*anse)
    break
else:
    print(-1)
