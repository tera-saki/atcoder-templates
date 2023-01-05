from typing import List, Tuple


class LiChaoTree:
    # reference: https://smijake3.hatenablog.com/entry/2018/06/16/144548
    def __init__(self, X: List[int], inf: int = int(1e20)):
        self.N = len(X)
        self.K = (self.N - 1).bit_length()
        self.size = 1 << self.K
        self.data = [None] * (self.size << 1)

        for i in range(self.N - 1):
            assert X[i] <= X[i + 1]

        self.X = X
        self.inf = inf
        for i in range(self.N, self.size):
            self.X.append(self.inf)

    def add_line(self, line: Tuple[int, int]) -> None:
        """add line"""
        self._add(line, 1, 0, self.size)

    def add_line_segment(self, line: Tuple[int, int], l: int, r: int) -> None:
        """add line segment to [l, r) range"""
        l0, r0 = l, r
        l += self.size
        r += self.size
        sz = 1
        while l < r:
            if r & 1:
                r -= 1
                r0 -= sz
                self._add(line, r, r0, r0 + sz)
            if l & 1:
                self._add(line, l, l0, l0 + sz)
                l += 1
                l0 += sz
            l >>= 1
            r >>= 1
            sz <<= 1

    def query(self, i: int) -> int:
        x = self.X[i]
        i += self.size
        ret = self.inf
        while i:
            if self.data[i]:
                a, b = self.data[i]
                ret = min(ret, a * x + b)
            i >>= 1
        return ret

    def _add(self, line: Tuple[int, int], k: int, l: int, r: int) -> None:
        while r - l:
            if self.data[k] is None:
                self.data[k] = line
                return
            c = (l + r) >> 1
            a, b = line
            p, q = self.data[k]
            xl, xc, xr = self.X[l], self.X[c], self.X[r - 1]
            left = a * xl + b < p * xl + q
            center = a * xc + b < p * xc + q
            right = a * xr + b < p * xr + q

            # update whole area with added line
            if left and right:
                self.data[k] = line
                return
            # no need to update
            if not left and not right:
                return
            # if more than half of segment is to be updated,
            # swap newly added line and existing line.
            if center:
                self.data[k], line = line, self.data[k]
            # search [l, c)
            if left != center:
                r = c
                k = k << 1
            # search [c, r)
            else:
                l = c
                k = k << 1 | 1
