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
    - https://atcoder.jp/contests/abc106/tasks/abc106_d
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 97, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\ninput = sys.stdin.readline\n\n\nclass CumulativeSum2D:\n    def\
    \ __init__(self, A):\n        self.A = A\n        self.H = len(A)\n        self.W\
    \ = len(A[0])\n        self.S = [[0 for _ in range(self.W + 1)] for _ in range(self.H\
    \ + 1)]\n\n        for i in range(self.H):\n            for j in range(self.W):\n\
    \                self.S[i + 1][j + 1] = self.S[i + 1][j] + self.S[i][j + 1] -\
    \ self.S[i][j] + self.A[i][j]\n\n    def sum(self, lx, ly, rx, ry):\n        return\
    \ self.S[rx + 1][ry + 1] - self.S[lx][ry + 1] - self.S[rx + 1][ly] + self.S[lx][ly]\n\
    \n\n# https://atcoder.jp/contests/abc106/tasks/abc106_d\nN, M, Q = map(int, input().split())\n\
    A = [[0 for _ in range(N)] for _ in range(N)]\nfor _ in range(M):\n    l, r =\
    \ map(int, input().split())\n    l -= 1\n    r -= 1\n    A[l][r] += 1\n\nS = CumulativeSum2D(A)\n\
    for _ in range(Q):\n    p, q = map(int, input().split())\n    p -= 1\n    q -=\
    \ 1\n    print(S.sum(p, p, q, q))\n"
  dependsOn: []
  isVerificationFile: false
  path: library/cumulative_sum.py
  requiredBy: []
  timestamp: '2022-09-18 13:43:26+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/cumulative_sum.py
layout: document
redirect_from:
- /library/library/cumulative_sum.py
- /library/library/cumulative_sum.py.html
title: library/cumulative_sum.py
---
