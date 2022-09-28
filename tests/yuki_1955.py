# verification-helper: PROBLEM https://yukicoder.me/problems/no/1955
import sys
from library.prime_table import PrimeTable
from library.two_sat import TwoSat

input = sys.stdin.readline

N = int(input())
is_prime = PrimeTable(10 ** 6).is_prime
A = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    A.append(b)

solver = TwoSat(2 * N)
for i in range(N):
    solver.add_clause(2 * i, 2 * i + 1)
    solver.add_clause(~(2 * i), ~(2 * i + 1))
for i in range(2 * N):
    for j in range(2 * N):
        if i == j:
            continue
        n = int(str(A[i]) + str(A[j]))
        if is_prime[n]:
            solver.if_then(i, j)
print('Yes' if solver.solve() is not None else 'No')
