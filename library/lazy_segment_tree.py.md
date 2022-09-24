---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/lazy_segment_tree.test.py
    title: tests/lazy_segment_tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Callable, TypeVar\nS = TypeVar('S')\nF = TypeVar('F')\n\
    \n\nclass LazySegTree:\n    def __init__(self, N: int, op: Callable[[S, S], S],\
    \ e: S,\n                 mapping: Callable[[F, S], S],\n                 composition:\
    \ Callable[[F, F], F], id: F):\n        \"\"\" \u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\
    \u30C8\u6728\n\n        Args:\n            N (int): \u914D\u5217\u306E\u9577\u3055\
    \n            op (Callable[[S, S], S]): \u533A\u9593\u53D6\u5F97\u306B\u7528\u3044\
    \u308B\u6F14\u7B97\n            e (S): \u5168\u3066\u306Ea\u306B\u5BFE\u3057\u3066\
    \ op(a, e) = a \u304C\u6210\u308A\u7ACB\u3064\u5358\u4F4D\u5143\n            mapping\
    \ (Callable[[F, S], S]): data\u306B\u4F5C\u7528\u3055\u305B\u308B\u95A2\u6570\n\
    \            composition (Callable[[F, F], F]): lazy\u306B\u4F5C\u7528\u3055\u305B\
    \u308B\u95A2\u6570 f(g(x))\n            id (F): \u5168\u3066\u306Ea\u306B\u5BFE\
    \u3057\u3066 mapping(id, a) = a \u304C\u6210\u308A\u7ACB\u3064\u6052\u7B49\u5199\
    \u50CF\n        \"\"\"\n        self.N = N\n        self.op = op\n        self.e\
    \ = e\n        self.mapping = mapping\n        self.composition = composition\n\
    \        self.id = id\n\n        self.K = (self.N - 1).bit_length()\n        self.size\
    \ = 1 << (self.K)\n\n        self.data = [e] * (self.size << 1)\n        self.lazy\
    \ = [id] * (self.size)\n\n    def build(self, A: List[S]) -> None:\n        for\
    \ i in range(self.N):\n            self.data[self.size + i] = A[i]\n        for\
    \ i in range(self.size - 1, 0, -1):\n            self.data[i] = self.op(self.data[i\
    \ << 1], self.data[i << 1 | 1])\n\n    def _eval_at(self, i: int, f: F) -> None:\n\
    \        self.data[i] = self.mapping(f, self.data[i])\n        if i < self.size:\n\
    \            self.lazy[i] = self.composition(f, self.lazy[i])\n\n    def _propagate_at(self,\
    \ i: int) -> None:\n        self._eval_at(i << 1, self.lazy[i])\n        self._eval_at(i\
    \ << 1 | 1, self.lazy[i])\n        self.lazy[i] = self.id\n\n    def _propagate_above(self,\
    \ i: int) -> None:\n        H = i.bit_length() - 1\n        for h in range(H,\
    \ 0, -1):\n            self._propagate_at(i >> h)\n\n    def _recalc_at(self,\
    \ i: int) -> None:\n        self.data[i] = self.op(self.data[i << 1], self.data[i\
    \ << 1 | 1])\n\n    def _recalc_above(self, i: int) -> None:\n        while i\
    \ > 1:\n            i >>= 1\n            self._recalc_at(i)\n\n    def set(self,\
    \ i: int, x: S) -> None:\n        i += self.size\n        self._propagate_above(i)\n\
    \        self.data[i] = x\n        self._recalc_above(i)\n\n    def get(self,\
    \ i) -> S:\n        i += self.size\n        self._propagate_above(i)\n       \
    \ return self.data[i]\n\n    def prod(self, L: int, R: int) -> S:\n        assert\
    \ 0 <= L and L <= R and R <= self.N\n        if L == R:\n            return self.e\n\
    \        L += self.size\n        R += self.size\n        self._propagate_above(L\
    \ // (L & -L))\n        self._propagate_above(R // (R & -R) - 1)\n        vl =\
    \ self.e\n        vr = self.e\n        while L < R:\n            if L & 1:\n \
    \               vl = self.op(vl, self.data[L])\n                L += 1\n     \
    \       if R & 1:\n                R -= 1\n                vr = self.op(self.data[R],\
    \ vr)\n            L >>= 1\n            R >>= 1\n        return self.op(vl, vr)\n\
    \n    def all_prod(self) -> S:\n        return self.data[1]\n\n    def apply(self,\
    \ L: int, R: int, f: F) -> None:\n        assert 0 <= L and L <= R and R <= self.N\n\
    \        if L == R:\n            return\n        L += self.size\n        R +=\
    \ self.size\n        L0 = L // (L & -L)\n        R0 = R // (R & -R) - 1\n    \
    \    self._propagate_above(L0)\n        self._propagate_above(R0)\n        while\
    \ L < R:\n            if L & 1:\n                self._eval_at(L, f)\n       \
    \         L += 1\n            if R & 1:\n                R -= 1\n            \
    \    self._eval_at(R, f)\n            L >>= 1\n            R >>= 1\n        self._recalc_above(L0)\n\
    \        self._recalc_above(R0)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/lazy_segment_tree.py
  requiredBy: []
  timestamp: '2022-09-24 15:48:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/lazy_segment_tree.test.py
documentation_of: library/lazy_segment_tree.py
layout: document
redirect_from:
- /library/library/lazy_segment_tree.py
- /library/library/lazy_segment_tree.py.html
title: library/lazy_segment_tree.py
---
