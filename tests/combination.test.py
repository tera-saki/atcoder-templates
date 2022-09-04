# verification-helper: PROBLEM https://yukicoder.me/problems/no/117
import sys
from lib.combination import Combination

input = sys.stdin.readline

T = int(input())
mod = 10 ** 9 + 7
comb = Combination(2 * 10 ** 6, mod)

for _ in range(T):
    query = input()[:-1]
    t = query[0]
    n, k = map(int, query[2:-1].split(','))
    if t == 'C':
        print(comb.C(n, k))
    elif t == 'P':
        print(comb.P(n, k))
    else:
        print(comb.H(n, k))
