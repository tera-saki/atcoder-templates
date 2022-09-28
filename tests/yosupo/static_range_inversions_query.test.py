# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query
import sys

from library.mo import Mo
from library.binary_indexed_tree import BIT


input = sys.stdin.readline


class MoSolver(Mo):
    def __init__(self, N, Q, A, query):
        super().__init__(N, Q, A, query)

    def extend_left(self, i):
        self.acc += bit.sum(A[i])
        self.cnt += 1
        bit.add(A[i], 1)

    def extend_right(self, i):
        self.acc += self.cnt - bit.sum(A[i] + 1)
        self.cnt += 1
        bit.add(A[i], 1)

    def shrink_left(self, i):
        bit.add(A[i], -1)
        self.cnt -= 1
        self.acc -= bit.sum(A[i])

    def shrink_right(self, i):
        bit.add(A[i], -1)
        self.cnt -= 1
        self.acc -= self.cnt - bit.sum(A[i] + 1)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [tuple(map(int, input().split())) for _ in range(Q)]

idx = {}
for i, a in enumerate(sorted(set(A))):
    idx[a] = i
A = [idx[a] for a in A]
K = len(A)
bit = BIT(K)
ans = MoSolver(N, Q, A, query).solve()
print(*ans, sep='\n')
