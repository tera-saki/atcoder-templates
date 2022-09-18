# verification-helper: PROBLEM https://atcoder.jp/contests/abc242/tasks/abc242_g
# verification-helper: IGNORE
import sys
from library.mo import Mo


class MoSolver(Mo):
    def __init__(self, N, Q, A, query):
        super().__init__(N, Q, A, query)

    def extend(self, i):
        if clothes[A[i]] & 1:
            self.cnt += 1
        clothes[A[i]] += 1

    def shrink(self, i):
        clothes[A[i]] -= 1
        if clothes[A[i]] & 1:
            self.cnt -= 1

    def extend_left(self, i):
        self.extend(i)

    def extend_right(self, i):
        self.extend(i)

    def shrink_left(self, i):
        self.shrink(i)

    def shrink_right(self, i):
        self.shrink(i)


N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
Q = int(input())
query = []
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    query.append((l, r))

clothes = [0] * N

M = max(A) + 1
solver = MoSolver(N, Q, A, query)
ans = solver.solve()
print(*ans, sep='\n')
