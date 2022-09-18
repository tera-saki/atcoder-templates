# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/0053
# verification-helper: IGNORE
import sys
from library.prime_table import PrimeTable

input = sys.stdin.readline

primes = PrimeTable(10 ** 6).primes
S = [0]
for p in primes:
    S.append(S[-1] + p)
while True:
    n = int(input())
    if n == 0:
        break
    print(S[n])
