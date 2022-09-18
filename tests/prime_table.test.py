# verification-helper: https://onlinejudge.u-aizu.ac.jp/problems/0009
import sys
from library.prime_table import PrimeTable

input = sys.stdin.readline

primes = PrimeTable(10 ** 6).primes
for n in map(int, sys.stdin.read().split()):
    l = -1
    r = len(primes)
    while r - l > 1:
        c = (l + r) // 2
        if primes[c] == n:
            l = c
            break
        if primes[c] < n:
            l = c
        else:
            r = c
    print(l + 1)
