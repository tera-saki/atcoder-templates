# https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/0053/judge/6971267/Python3
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
