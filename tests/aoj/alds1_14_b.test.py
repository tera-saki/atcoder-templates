# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_14_B
import sys
import random
from library.rolling_hash import RollingHash

input = sys.stdin.readline

T = input()[:-1]
P = input()[:-1]

RT = RollingHash(T)
RP = RollingHash(P, base=RT.base)

target = RP.get(0, len(P))
for i in range(len(T)):
    if i + len(P) > len(T):
        break
    h = RT.get(i, i + len(P))
    if h == target:
        print(i)
