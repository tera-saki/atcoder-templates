---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
    - https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\ninput = sys.stdin.readline\n\n# reference: https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e\n\
    \n\nclass LazySegTree_RUQ:\n    def __init__(self, N, func, e):\n        self.N\
    \ = N\n        self.func = func\n        self.X = [e] * (N << 1)\n        self.lazy\
    \ = [None] * (N << 1)\n        self.e = e\n\n    def build(self, seq):\n     \
    \   for i in range(self.N):\n            self.X[self.N + i] = seq[i]\n       \
    \ for i in range(self.N)[::-1]:\n            self.X[i] = self.func(self.X[i <<\
    \ 1], self.X[i << 1 | 1])\n\n    def gindex(self, l, r):\n        l += self.N\n\
    \        r += self.N\n        lm = l >> (l & -l).bit_length()\n        rm = r\
    \ >> (r & -r).bit_length()\n        while r > l:\n            if l <= lm:\n  \
    \              yield l\n            if r <= rm:\n                yield r\n   \
    \         r >>= 1\n            l >>= 1\n        while l:\n            yield l\n\
    \            l >>= 1\n\n    def propagates(self, *ids):\n        for i in ids[::-1]:\n\
    \            v = self.lazy[i]\n            if v is None:\n                continue\n\
    \            self.lazy[i << 1] = v\n            self.lazy[i << 1 | 1] = v\n  \
    \          self.X[i << 1] = v\n            self.X[i << 1 | 1] = v\n          \
    \  self.lazy[i] = None\n\n    def update(self, L, R, x):\n        *ids, = self.gindex(L,\
    \ R)\n        self.propagates(*ids)\n        L += self.N\n        R += self.N\n\
    \        while L < R:\n            if L & 1:\n                self.lazy[L] = x\n\
    \                self.X[L] = x\n                L += 1\n            if R & 1:\n\
    \                R -= 1\n                self.lazy[R] = x\n                self.X[R]\
    \ = x\n            L >>= 1\n            R >>= 1\n        for i in ids:\n     \
    \       self.X[i] = self.func(self.X[i << 1], self.X[i << 1 | 1])\n\n    def query(self,\
    \ L, R):\n        *ids, = self.gindex(L, R)\n        self.propagates(*ids)\n \
    \       L += self.N\n        R += self.N\n        vL = self.e\n        vR = self.e\n\
    \        while L < R:\n            if L & 1:\n                vL = self.func(vL,\
    \ self.X[L])\n                L += 1\n            if R & 1:\n                R\
    \ -= 1\n                vR = self.func(self.X[R], vR)\n            L >>= 1\n \
    \           R >>= 1\n        return self.func(vL, vR)\n\n\n# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H\n\
    N, Q = map(int, input().split())\nlazy_segtree = LazySegTree_RUQ(N, min, 1 <<\
    \ 40)\nlazy_segtree.build([(1 << 31) - 1 for _ in range(N)])\nfor _ in range(Q):\n\
    \    t, *q = map(int, input().split())\n    if t == 0:\n        s, t, x = q\n\
    \        lazy_segtree.update(s, t + 1, x)\n    else:\n        s, t = q\n     \
    \   print(lazy_segtree.query(s, t + 1))\n"
  dependsOn: []
  isVerificationFile: false
  path: library/lazy_seg_tree_update.py
  requiredBy: []
  timestamp: '2022-09-19 01:08:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/lazy_seg_tree_update.py
layout: document
redirect_from:
- /library/library/lazy_seg_tree_update.py
- /library/library/lazy_seg_tree_update.py.html
title: library/lazy_seg_tree_update.py
---
