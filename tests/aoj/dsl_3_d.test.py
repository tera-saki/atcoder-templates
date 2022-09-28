# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
import sys
from library.swag import SWAG

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

ans = []
swag = SWAG(min)
for i in range(L):
    swag.push(A[i])
ans.append(swag.fold())

for i in range(L, N):
    swag.pop()
    swag.push(A[i])
    ans.append(swag.fold())

print(*ans)
