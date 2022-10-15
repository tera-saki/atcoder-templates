---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/binary_indexed_tree.py
    title: library/binary_indexed_tree.py
  - icon: ':heavy_check_mark:'
    path: library/mo.py
    title: library/mo.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_inversions_query
    links:
    - https://judge.yosupo.jp/problem/static_range_inversions_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query\n\
    import sys\n\nfrom library.mo import Mo\nfrom library.binary_indexed_tree import\
    \ BIT\n\n\ninput = sys.stdin.readline\n\n\nclass MoSolver(Mo):\n    def __init__(self,\
    \ N, Q, A, query):\n        super().__init__(N, Q, A, query)\n\n    def extend_left(self,\
    \ i):\n        self.acc += bit.sum(A[i])\n        self.cnt += 1\n        bit.add(A[i],\
    \ 1)\n\n    def extend_right(self, i):\n        self.acc += self.cnt - bit.sum(A[i]\
    \ + 1)\n        self.cnt += 1\n        bit.add(A[i], 1)\n\n    def shrink_left(self,\
    \ i):\n        bit.add(A[i], -1)\n        self.cnt -= 1\n        self.acc -= bit.sum(A[i])\n\
    \n    def shrink_right(self, i):\n        bit.add(A[i], -1)\n        self.cnt\
    \ -= 1\n        self.acc -= self.cnt - bit.sum(A[i] + 1)\n\n\nN, Q = map(int,\
    \ input().split())\nA = list(map(int, input().split()))\nquery = [tuple(map(int,\
    \ input().split())) for _ in range(Q)]\n\nidx = {}\nfor i, a in enumerate(sorted(set(A))):\n\
    \    idx[a] = i\nA = [idx[a] for a in A]\nK = len(A)\nbit = BIT(K)\nans = MoSolver(N,\
    \ Q, A, query).solve()\nprint(*ans, sep='\\n')\n"
  dependsOn:
  - library/mo.py
  - library/binary_indexed_tree.py
  isVerificationFile: true
  path: tests/yosupo/static_range_inversions_query.test.py
  requiredBy: []
  timestamp: '2022-10-15 16:47:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/static_range_inversions_query.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/static_range_inversions_query.test.py
- /verify/tests/yosupo/static_range_inversions_query.test.py.html
title: tests/yosupo/static_range_inversions_query.test.py
---
