# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_A
import sys
from library.math import factorize

input = sys.stdin.readline

N = int(input())
ans = ' '.join([str(f) for f in factorize(N)])
print(f"{N}: {ans}")
