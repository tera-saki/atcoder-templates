---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/alds1_5_d.test.py
    title: tests/aoj/alds1_5_d.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/static_range_inversions_query.test.py
    title: tests/yosupo/static_range_inversions_query.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BIT:\n    def __init__(self, N):\n        self.N = N\n        self.A\
    \ = [0] * (N + 1)\n\n    def add(self, i, x):\n        \"\"\"add x to i-th element\
    \ (0-indexed)\"\"\"\n        assert 0 <= i < self.N\n        i += 1\n        while\
    \ i <= self.N:\n            self.A[i] += x\n            i += i & -i\n\n    def\
    \ sum(self, i):\n        \"\"\"return sum(A[:i])\"\"\"\n        assert 0 <= i\
    \ <= self.N\n        s = 0\n        while i > 0:\n            s += self.A[i]\n\
    \            i -= i & -i\n        return s\n\n    def range_sum(self, l, r):\n\
    \        \"\"\"return sum(A[l:r])\"\"\"\n        return self.sum(r) - self.sum(l)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/binary_indexed_tree.py
  requiredBy: []
  timestamp: '2022-11-03 15:53:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/alds1_5_d.test.py
  - tests/yosupo/static_range_inversions_query.test.py
documentation_of: library/binary_indexed_tree.py
layout: document
redirect_from:
- /library/library/binary_indexed_tree.py
- /library/library/binary_indexed_tree.py.html
title: library/binary_indexed_tree.py
---
