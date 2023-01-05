# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min
import sys
from library.li_chao_tree import LiChaoTree

input = sys.stdin.readline

N, Q = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(N)]
query = [tuple(map(int, input().split())) for _ in range(Q)]
X = []
for l, r, a, b in lines:
    X.append(l)
    X.append(r)
for t, *q in query:
    if t == 0:
        l, r, a, b = q
        X.append(l)
        X.append(r)
    else:
        p, = q
        X.append(p)

X = sorted(set(X))
idx = {x: i for i, x in enumerate(X)}

solver = LiChaoTree(X)
for l, r, a, b in lines:
    solver.add_line_segment((a, b), idx[l], idx[r])
for t, *q in query:
    if t == 0:
        l, r, a, b = q
        solver.add_line_segment((a, b), idx[l], idx[r])
    else:
        p, = q
        v = solver.query(idx[p])
        print(v if v < solver.inf else 'INFINITY')
