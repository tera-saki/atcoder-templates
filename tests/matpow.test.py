# verification-helper: PROBLEM https://yukicoder.me/problems/no/1073
import sys
from library.matpow import Matpow

input = sys.stdin.readline

N = int(input())
mod = 10 ** 9 + 7

pinv = pow(6, mod - 2, mod)
A = [[0 for _ in range(6)] for _ in range(6)]
for j in range(6):
    A[0][j] = pinv
for i in range(1, 6):
    A[i][i - 1] = 1

An = Matpow(A, mod).pow(N)
print(An[0][0])
