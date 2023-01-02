# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/2858
import sys
from library.segment_sieve import SegmentSieve

input = sys.stdin.readline

l, r = map(int, input().split())
sieve = SegmentSieve(10 ** 9)
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
is_prime = [i in primes for i in range(30)]
ans = 0
for factors in SegmentSieve(10 ** 9).get_factors(l, r):
    if is_prime[len(factors)]:
        ans += 1
print(ans)
