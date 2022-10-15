# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
import sys
from library.math import extgcd

input = sys.stdin.readline

a, b = map(int, input().split())
_, x, y = extgcd(a, b)
print(x, y)
