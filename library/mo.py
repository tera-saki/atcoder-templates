class Mo:
    def __init__(self, N, Q, A, query):
        # divide queries into √Q buckets
        # thus the size of each bucket is N/√Q
        self.N = N
        self.Q = Q
        self.A = A
        self.query = query
        self.b_num = int(Q ** .5)

        self.ans = [None] * Q
        self.acc = 0
        self.cnt = 0
        self.L = 0
        self.R = 0

        # decide which bucket the query is placed to by left-end value
        # sort queries by bucket number, and sort queries in a bucket by right-end value
        # in asc order if bucket's index is even otherwise in desc order
        # (the constant factor will be smaller)

        def cmp(i):
            l, r = self.query[i]
            b = l * self.b_num // N
            return (b << 32) + (~r if b & 1 else r)

        C = [cmp(i) for i in range(Q)]
        self.order = sorted(range(Q), key=lambda i: C[i])

    def solve(self):
        for i in self.order:
            l, r = self.query[i]
            # extend left-end
            # decrement at first since current A[L] is already included ([L:R))
            while l < self.L:
                self.L -= 1
                self.extend_left(self.L)
            # extend right-end
            # increment at last since current A[R] is not included yet ([L:R))
            while self.R < r:
                self.extend_right(self.R)
                self.R += 1
            # shrink left-end
            # increment at last since current A[L] is included ([L:R))
            while self.L < l:
                self.shrink_left(self.L)
                self.L += 1
            # shrink right-end
            # decrement at first since current A[R] is not included ([L:R))
            while r < self.R:
                self.R -= 1
                self.shrink_right(self.R)
            self.ans[i] = self.acc
        return self.ans

    def extend_left(self, i):
        raise NotImplementedError()

    def extend_right(self, i):
        raise NotImplementedError()

    def shrink_left(self, i):
        raise NotImplementedError()

    def shrink_right(self, i):
        raise NotImplementedError()
