# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_4_A
import sys
from library.zaatsu import Zaatsu

input = sys.stdin.readline


N = int(input())
rec = [tuple(map(int, input().split())) for _ in range(N)]

X = [0]
Y = [0]
for x1, y1, x2, y2 in rec:
    X.append(x1)
    X.append(x2)
    Y.append(y1)
    Y.append(y2)

Zx = Zaatsu(X)
Zy = Zaatsu(Y)

A = [[0 for _ in range(Zy.N + 1)] for _ in range(Zx.N + 1)]
for x1, y1, x2, y2 in rec:
    A[Zx.id(x1)][Zy.id(y1)] += 1
    A[Zx.id(x1)][Zy.id(y2)] -= 1
    A[Zx.id(x2)][Zy.id(y1)] -= 1
    A[Zx.id(x2)][Zy.id(y2)] += 1
for i in range(Zx.N):
    for j in range(Zy.N):
        A[i + 1][j] += A[i][j]
for j in range(Zy.N):
    for i in range(Zx.N):
        A[i][j + 1] += A[i][j]
ans = 0
for i, (x1, x2) in enumerate(zip(Zx.A[:-1], Zx.A[1:])):
    for j, (y1, y2) in enumerate(zip(Zy.A[:-1], Zy.A[1:])):
        if A[i][j] == 0:
            continue
        ans += (x2 - x1) * (y2 - y1)
print(ans)
