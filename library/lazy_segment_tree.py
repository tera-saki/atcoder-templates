from typing import List, Callable, TypeVar
S = TypeVar('S')
F = TypeVar('F')


class LazySegTree:
    # reference: https://github.com/shakayami/ACL-for-python
    # reference: https://maspypy.com/segment-tree-%E3%81%AE%E3%81%8A%E5%8B%89%E5%BC%B72
    # reference: https://betrue12.hateblo.jp/entry/2020/09/22/194541
    def __init__(self, N: int, op: Callable[[S, S], S], e: S,
                 mapping: Callable[[F, S], S],
                 composition: Callable[[F, F], F], id: F):
        """ 遅延セグメント木

        Args:
            N (int): 配列の長さ
            op (Callable[[S, S], S]): 区間取得に用いる演算
            e (S): 全てのaに対して op(a, e) = a が成り立つ単位元
            mapping (Callable[[F, S], S]): dataに作用させる関数
            composition (Callable[[F, F], F]): lazyに作用させる関数 f(g(x))
            id (F): 全てのaに対して mapping(id, a) = a が成り立つ恒等写像
        """
        self.N = N
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id

        self.K = (self.N - 1).bit_length()
        self.size = 1 << (self.K)

        self.data = [e] * (self.size << 1)
        self.lazy = [id] * (self.size)

    def build(self, A: List[S]) -> None:
        for i in range(self.N):
            self.data[self.size + i] = A[i]
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(self.data[i << 1], self.data[i << 1 | 1])

    def _eval_at(self, i: int, f: F) -> None:
        self.data[i] = self.mapping(f, self.data[i])
        if i < self.size:
            self.lazy[i] = self.composition(f, self.lazy[i])

    def _propagate_at(self, i: int) -> None:
        self._eval_at(i << 1, self.lazy[i])
        self._eval_at(i << 1 | 1, self.lazy[i])
        self.lazy[i] = self.id

    def _propagate_above(self, i: int) -> None:
        H = i.bit_length() - 1
        for h in range(H, 0, -1):
            self._propagate_at(i >> h)

    def _recalc_at(self, i: int) -> None:
        self.data[i] = self.op(self.data[i << 1], self.data[i << 1 | 1])

    def _recalc_above(self, i: int) -> None:
        while i > 1:
            i >>= 1
            self._recalc_at(i)

    def set(self, i: int, x: S) -> None:
        i += self.size
        self._propagate_above(i)
        self.data[i] = x
        self._recalc_above(i)

    def get(self, i) -> S:
        i += self.size
        self._propagate_above(i)
        return self.data[i]

    def prod(self, L: int, R: int) -> S:
        assert 0 <= L and L <= R and R <= self.N
        if L == R:
            return self.e
        L += self.size
        R += self.size
        self._propagate_above(L // (L & -L))
        self._propagate_above(R // (R & -R) - 1)
        vl = self.e
        vr = self.e
        while L < R:
            if L & 1:
                vl = self.op(vl, self.data[L])
                L += 1
            if R & 1:
                R -= 1
                vr = self.op(self.data[R], vr)
            L >>= 1
            R >>= 1
        return self.op(vl, vr)

    def all_prod(self) -> S:
        return self.data[1]

    def apply(self, L: int, R: int, f: F) -> None:
        assert 0 <= L and L <= R and R <= self.N
        if L == R:
            return
        L += self.size
        R += self.size
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_above(L0)
        self._propagate_above(R0)
        while L < R:
            if L & 1:
                self._eval_at(L, f)
                L += 1
            if R & 1:
                R -= 1
                self._eval_at(R, f)
            L >>= 1
            R >>= 1
        self._recalc_above(L0)
        self._recalc_above(R0)
