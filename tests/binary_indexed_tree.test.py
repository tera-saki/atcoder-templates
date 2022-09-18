# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_D
import sys
from library.binary_indexed_tree import BIT

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

idx = {}
for i, a in enumerate(sorted(A)):
    idx[a] = i

ans = 0
bit = BIT(N)
for i, a in enumerate(A):
    ans += bit.range_sum(idx[a] + 1, N)
    bit.add(idx[a], 1)
print(ans)
