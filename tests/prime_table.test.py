# verification-helper: PROBLEM https://yukicoder.me/problems/no/1140
import sys
from library.prime_table import PrimeTable

input = sys.stdin.readline

L = 5 * 10 ** 6
is_prime = PrimeTable(L).is_prime

T = int(input())
for _ in range(T):
    a, p = map(int, input().split())
    if is_prime[p]:
        print(0 if a % p == 0 else 1)
    else:
        print(-1)
