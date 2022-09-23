class CumulativeSum:
    def __init__(self, A):
        self.S = [0]
        acc = 0
        for a in A:
            acc += a
            self.S.append(acc)

    def get(self, l, r):
        """return sum(A[l:r]), i.e. sum of A[x] (l <= x < r) """
        return self.S[r] - self.S[l]
