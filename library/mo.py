import sys
import math
input = sys.stdin.readline


class Mo:
    # refer to following tatyam-san's submission:
    # https://atcoder.jp/contests/abc242/submissions/29862680
    def __init__(self, N, Q, A, query):
        # divide queries into √Q buckets
        # thus the size of each bucket is N/√Q
        self.N = N
        self.Q = Q
        self.A = A
        self.query = query
        self.b_num = int(math.ceil(math.sqrt(Q)))
        self.buckets = [[] for _ in range(self.b_num)]

        self.cnt = 0
        self.ans = [None] * Q

        # decide which bucket the query is placed to by left-end value
        for i in range(Q):
            # [l:r)
            l, r = query[i]
            self.buckets[l * self.b_num // N].append((l, r, i))

        # sort queries in the bucket by right-end value
        # in asc order if bucket's index is even otherwise in desc order
        # (the constant factor will be smaller)
        for i in range(self.b_num):
            if i & 1:
                self.buckets[i].sort(key=lambda x: -x[1])
            else:
                self.buckets[i].sort(key=lambda x: x[1])

    def solve(self):
        L = 0
        R = 0
        for b in range(self.b_num):
            for l, r, i in self.buckets[b]:
                # extend left-end
                # decrement at first since current A[L] is already included ([L:R))
                while l < L:
                    L -= 1
                    self.extend_left(L)
                # extend right-end
                # increment at last since current A[R] is not included yet ([L:R))
                while R < r:
                    self.extend_right(R)
                    R += 1
                # shrink left-end
                # increment at last since current A[L] is included ([L:R))
                while L < l:
                    self.shrink_left(L)
                    L += 1
                # shrink right-end
                # decrement at first since current A[R] is not included ([L:R))
                while r < R:
                    R -= 1
                    self.shrink_right(R)
                self.ans[i] = self.cnt
        return self.ans

    def extend_left(self, i):
        raise NotImplementedError()

    def extend_right(self, i):
        raise NotImplementedError()

    def shrink_left(self, i):
        raise NotImplementedError()

    def shrink_right(self, i):
        raise NotImplementedError()
