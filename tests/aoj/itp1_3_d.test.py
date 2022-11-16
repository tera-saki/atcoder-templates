# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_D
import sys
from library.math import divisors

input = sys.stdin.readline

a, b, c = map(int, input().split())
divs = divisors(c)
ans = 0
for d in divs:
    if a <= d <= b:
        ans += 1
print(ans)
