from typing import List, TypeVar, Callable


T = TypeVar('T')


class DualSegTree:
    # reference: https://hackmd.io/@tatyam-prime/DualSegmentTree
    def __init__(self, N: int, f: Callable[[T, T], T], e: T):
        """双対セグメント木

        Args:
            N (int): 配列の長さ
            f (Callable[[T, T], T]): 作用させる関数
            e (T): 単位元

        Note:
            値に作用を適応させる操作（遅延セグメント木のmappingに相当）と、
            作用を合成する操作（遅延セグメント木のcompositionに相当)が、
            同一の操作として記述できることが必要
            例） 区間加算・区間代入・区間chmin等
        """
        self.N = N
        self.f = f
        self.e = e

        self.K = (self.N - 1).bit_length()
        self.size = 1 << self.K

        self.lazy = [e] * (self.size << 1)

    def build(self, A: List[T]) -> None:
        for i in range(self.N):
            self.lazy[self.size + i] = A[i]

    def _propagate_at(self, i: int) -> None:
        if self.lazy[i] == self.e:
            return
        self.lazy[i << 1] = self.f(self.lazy[i << 1], self.lazy[i])
        self.lazy[i << 1 | 1] = self.f(self.lazy[i << 1 | 1], self.lazy[i])
        self.lazy[i] = self.e

    def _propagate_above(self, i: int) -> None:
        H = i.bit_length() - 1
        for h in range(H, 0, -1):
            self._propagate_at(i >> h)

    def get(self, i: int) -> T:
        i += self.size
        self._propagate_above(i)
        return self.lazy[i]

    def set(self, i: int, a: T) -> None:
        i += self.size
        self._propagate_above(i)
        self.lazy[i] = a

    def query(self, l: int, r: int, a: T) -> None:
        assert 0 <= l and l <= r and r <= self.N
        l += self.size
        r += self.size
        self._propagate_above(l // (l & -l))
        self._propagate_above(r // (r & -r) - 1)
        while l < r:
            if l & 1:
                self.lazy[l] = self.f(self.lazy[l], a)
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.f(self.lazy[r], a)
            l >>= 1
            r >>= 1
