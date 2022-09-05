# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_D
from lib.lis import LIS

input = sys.stdin.readline


N = int(input())
A = [int(input()) for _ in range(N)]
print(LIS(A).solve())
