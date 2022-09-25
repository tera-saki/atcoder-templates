# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat
import sys
from library.two_sat import TwoSat

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

p, cnf, N, M = input().split()
N, M = int(N), int(M)
solver = TwoSat(N)
for _ in range(M):
    s, t, _ = map(int, input().split())
    if s > 0:
        s -= 1
    if t > 0:
        t -= 1
    solver.add_clause(s, t)

ans = solver.solve()
if ans is None:
    print('s UNSATISFIABLE')
    exit()
A = []
for i in range(N):
    if ans[i] > 0:
        A.append(i + 1)
    else:
        A.append(-(i + 1))
print('s SATISFIABLE')
print(f"v {' '.join([str(a) for a in A])} 0")
