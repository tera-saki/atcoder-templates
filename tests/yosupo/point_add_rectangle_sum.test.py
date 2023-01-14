# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum
import sys
from library.point_add_rectangle_sum import WaveletMatrixPointAddRectangleSum

input = sys.stdin.readline

N, Q = map(int, input().split())
solver = WaveletMatrixPointAddRectangleSum()
points = [tuple(map(int, input().split())) for _ in range(N)]
query = [tuple(map(int, input().split())) for _ in range(Q)]

for x, y, w in points:
    solver.add_point(x, y, w)
for t, *q in query:
    if t == 0:
        x, y, w = q
        solver.add_point(x, y)
solver.build()
ans = []
for t, *q in query:
    if t == 0:
        x, y, w = q
        solver.add_value(x, y, w)
    else:
        lx, ly, rx, ry = q
        ans.append(solver.rectangle_sum(lx, ly, rx, ry))
print(*ans)
