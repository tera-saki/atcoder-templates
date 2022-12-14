# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm
import sys
from library.string import Z_Algorhthm

input = sys.stdin.readline

S = input()[:-1]
print(*Z_Algorhthm(S).Z)
