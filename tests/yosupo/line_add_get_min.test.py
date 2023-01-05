# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min
import sys
from library.li_chao_tree import LiChaoTree

input = sys.stdin.readline

N, Q = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(N)]
query = [tuple(map(int, input().split())) for _ in range(Q)]
X = []
for t, *q in query:
    if t == 1:
        p, = q
        X.append(p)
X = sorted(set(X))
solver = LiChaoTree(X)
for line in lines:
    solver.add_line(line)
for t, *q in query:
    if t == 0:
        solver.add_line(q)
    else:
        p, = q
        print(solver.query(p))
