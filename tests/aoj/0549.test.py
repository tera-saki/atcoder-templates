# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/challenges/sources/JOI/Final/0549
import sys
from library.cumulative_sum import CumulativeSum

input = sys.stdin.readline

n, m = map(int, input().split())
A = [int(input()) for _ in range(n - 1)]
cumsum = CumulativeSum(A)

ans = 0
cur = 0
for _ in range(m):
    d = int(input())
    ans += cumsum.get(min(cur, cur + d), max(cur, cur + d))
    cur += d
print(ans % 100000)
