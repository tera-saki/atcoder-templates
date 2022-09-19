# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/challenges/sources/JOI/Final/0560
import sys
from library.cumulative_sum import CumulativeSum2D

input = sys.stdin.readline

H, W = map(int, input().split())
Q = int(input())
C = [input()[:-1] for _ in range(H)]

J = [[0 for _ in range(W)] for _ in range(H)]
O = [[0 for _ in range(W)] for _ in range(H)]
I = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j] == 'J':
            J[i][j] += 1
        elif C[i][j] == 'O':
            O[i][j] += 1
        else:
            I[i][j] += 1
Sj = CumulativeSum2D(J)
So = CumulativeSum2D(O)
Si = CumulativeSum2D(I)

for _ in range(Q):
    lx, ly, rx, ry = map(lambda x: int(x) - 1, input().split())
    aj = Sj.sum(lx, ly, rx, ry)
    ao = So.sum(lx, ly, rx, ry)
    ai = Si.sum(lx, ly, rx, ry)
    print(aj, ao, ai)
