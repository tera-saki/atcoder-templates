# verification-helper: PROBLEM https://yukicoder.me/problems/no/1006
import sys
from collections import defaultdict
from library.osa_k import Osa_k

input = sys.stdin.readline

X = int(input())
osa_k = Osa_k(X)
f = [0] * X
for i in range(1, X):
    factors = osa_k.factors(i)
    D = defaultdict(int)
    for factor in factors:
        D[factor] += 1
    d = 1
    for v in D.values():
        d *= (v + 1)
    f[i] = i - d
v = [1 << 30] * X
for i in range(1, X):
    v[i] = abs(f[i] - f[X - i])
minv = min(v)
for i in range(1, X):
    if v[i] == minv:
        print(i, X - i)
