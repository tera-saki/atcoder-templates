import sys
import math

input = sys.stdin.readline


class Mo:
    # refer to following tatyam-san's submission:
    # https://atcoder.jp/contests/abc242/submissions/29862680
    def __init__(self, N, Q, A, query):
        # divide queries into √Q buckets
        # thus the size of each bucket is N/√Q
        self.A = A
        self.query = query
        self.b_num = int(math.ceil(math.sqrt(Q)))
        self.buckets = [[] for _ in range(self.b_num)]

        # decide which bucket the query is placed to by left-end value
        for i in range(Q):
            # [l:r)
            l, r = query[i]
            l -= 1
            self.buckets[l * self.b_num // N].append((i, l, r))

        # sort queries in the bucket by right-end value
        # in asc order if bucket's index is even otherwise in desc order
        # (the constant factor will be smaller)
        for i in range(self.b_num):
            if i & 1:
                self.buckets[i].sort(key=lambda x: -x[2])
            else:
                self.buckets[i].sort(key=lambda x: x[2])

    def solve(self):
        global pairs
        L = 0
        R = 0
        for b in range(self.b_num):
            for i, l, r in self.buckets[b]:
                # extend left-end
                # decrement at first since current A[L] is already included ([L:R))
                while l < L:
                    L -= 1
                    self.add(L)
                # extend right-end
                # increment at last since current A[R] is not included yet ([L:R))
                while R < r:
                    self.add(R)
                    R += 1
                # shrink left-end
                # increment at last since current A[L] is included ([L:R))
                while L < l:
                    self.sub(L)
                    L += 1
                # shrink right-end
                # decrement at first since current A[R] is not included ([L:R))
                while r < R:
                    R -= 1
                    self.sub(R)
                ans[i] = pairs

    def add(self, i):
        global pairs
        if cnt[A[i]] & 1:
            pairs += 1
        cnt[A[i]] += 1

    def sub(self, i):
        global pairs
        cnt[A[i]] -= 1
        if cnt[A[i]] & 1:
            pairs -= 1

# https://atcoder.jp/contests/abc242/tasks/abc242_g
N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
Q = int(input())
query = [tuple(map(int, input().split())) for _ in range(Q)]

ans = [None] * Q
cnt = [0] * N
pairs = 0
mo = Mo(N, Q, A, query)
mo.solve()
print(*ans, sep='\n')
