# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_14_B
import sys
import random
from lib.rolling_hash import RollingHash

input = sys.stdin.readline

T = input()[:-1]
P = input()[:-1]

mod = (1 << 61) - 1
base = random.randint(100, mod - 1)
RT = RollingHash(T, mod=mod, base=base)
RP = RollingHash(P, mod=mod, base=base)

target = RP.get(0, len(P))
for i in range(len(T)):
    if i + len(P) > len(T):
        break
    h = RT.get(i, i + len(P))
    if h == target:
        print(i)
