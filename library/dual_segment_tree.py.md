---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/dsl_2_d.test.py
    title: tests/aoj/dsl_2_d.test.py
  - icon: ':heavy_check_mark:'
    path: tests/aoj/dsl_2_e.test.py
    title: tests/aoj/dsl_2_e.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://hackmd.io/@tatyam-prime/DualSegmentTree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, TypeVar, Callable\n\n\nT = TypeVar('T')\n\n\nclass\
    \ DualSegTree:\n    # reference: https://hackmd.io/@tatyam-prime/DualSegmentTree\n\
    \    def __init__(self, N: int, f: Callable[[T, T], T], e: T):\n        \"\"\"\
    \u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728\n\n        Args:\n          \
    \  N (int): \u914D\u5217\u306E\u9577\u3055\n            f (Callable[[T, T], T]):\
    \ \u4F5C\u7528\u3055\u305B\u308B\u95A2\u6570\n            e (T): \u5358\u4F4D\u5143\
    \n\n        Note:\n            \u5024\u306B\u4F5C\u7528\u3092\u9069\u5FDC\u3055\
    \u305B\u308B\u64CD\u4F5C\uFF08\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728\
    \u306Emapping\u306B\u76F8\u5F53\uFF09\u3068\u3001\n            \u4F5C\u7528\u3092\
    \u5408\u6210\u3059\u308B\u64CD\u4F5C\uFF08\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\
    \u30C8\u6728\u306Ecomposition\u306B\u76F8\u5F53)\u304C\u3001\n            \u540C\
    \u4E00\u306E\u64CD\u4F5C\u3068\u3057\u3066\u8A18\u8FF0\u3067\u304D\u308B\u3053\
    \u3068\u304C\u5FC5\u8981\n            \u4F8B\uFF09 \u533A\u9593\u52A0\u7B97\u30FB\
    \u533A\u9593\u4EE3\u5165\u30FB\u533A\u9593chmin\u7B49\n        \"\"\"\n      \
    \  self.N = N\n        self.f = f\n        self.e = e\n\n        self.K = (self.N\
    \ - 1).bit_length()\n        self.size = 1 << self.K\n\n        self.lazy = [e]\
    \ * (self.size << 1)\n\n    def build(self, A: List[T]) -> None:\n        for\
    \ i in range(self.N):\n            self.lazy[self.size + i] = A[i]\n\n    def\
    \ _propagate_at(self, i: int) -> None:\n        if self.lazy[i] == self.e:\n \
    \           return\n        self.lazy[i << 1] = self.f(self.lazy[i << 1], self.lazy[i])\n\
    \        self.lazy[i << 1 | 1] = self.f(self.lazy[i << 1 | 1], self.lazy[i])\n\
    \        self.lazy[i] = self.e\n\n    def _propagate_above(self, i: int) -> None:\n\
    \        H = i.bit_length() - 1\n        for h in range(H, 0, -1):\n         \
    \   self._propagate_at(i >> h)\n\n    def get(self, i: int) -> T:\n        i +=\
    \ self.size\n        self._propagate_above(i)\n        return self.lazy[i]\n\n\
    \    def set(self, i: int, a: T) -> None:\n        i += self.size\n        self._propagate_above(i)\n\
    \        self.lazy[i] = a\n\n    def query(self, l: int, r: int, a: T) -> None:\n\
    \        assert 0 <= l and l <= r and r <= self.N\n        l += self.size\n  \
    \      r += self.size\n        self._propagate_above(l // (l & -l))\n        self._propagate_above(r\
    \ // (r & -r) - 1)\n        while l < r:\n            if l & 1:\n            \
    \    self.lazy[l] = self.f(self.lazy[l], a)\n                l += 1\n        \
    \    if r & 1:\n                r -= 1\n                self.lazy[r] = self.f(self.lazy[r],\
    \ a)\n            l >>= 1\n            r >>= 1\n"
  dependsOn: []
  isVerificationFile: false
  path: library/dual_segment_tree.py
  requiredBy: []
  timestamp: '2023-04-17 16:54:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/dsl_2_e.test.py
  - tests/aoj/dsl_2_d.test.py
documentation_of: library/dual_segment_tree.py
layout: document
redirect_from:
- /library/library/dual_segment_tree.py
- /library/library/dual_segment_tree.py.html
title: library/dual_segment_tree.py
---
