---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
    PROBLEM: https://atcoder.jp/contests/abc242/tasks/abc242_g
    links:
    - https://atcoder.jp/contests/abc242/tasks/abc242_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 97, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc242/tasks/abc242_g\n\
    # verification-helper: IGNORE\nimport sys\nfrom library.mo import Mo\n\n\nclass\
    \ MoSolver(Mo):\n    def __init__(self, N, Q, A, query):\n        super().__init__(N,\
    \ Q, A, query)\n\n    def extend(self, i):\n        if clothes[A[i]] & 1:\n  \
    \          self.cnt += 1\n        clothes[A[i]] += 1\n\n    def shrink(self, i):\n\
    \        clothes[A[i]] -= 1\n        if clothes[A[i]] & 1:\n            self.cnt\
    \ -= 1\n\n    def extend_left(self, i):\n        self.extend(i)\n\n    def extend_right(self,\
    \ i):\n        self.extend(i)\n\n    def shrink_left(self, i):\n        self.shrink(i)\n\
    \n    def shrink_right(self, i):\n        self.shrink(i)\n\n\nN = int(input())\n\
    A = list(map(lambda x: int(x) - 1, input().split()))\nQ = int(input())\nquery\
    \ = []\nfor _ in range(Q):\n    l, r = map(int, input().split())\n    l -= 1\n\
    \    query.append((l, r))\n\nclothes = [0] * N\n\nM = max(A) + 1\nsolver = MoSolver(N,\
    \ Q, A, query)\nans = solver.solve()\nprint(*ans, sep='\\n')\n"
  dependsOn: []
  isVerificationFile: true
  path: tests/mo.test.py
  requiredBy: []
  timestamp: '2022-09-18 13:43:26+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: tests/mo.test.py
layout: document
redirect_from:
- /verify/tests/mo.test.py
- /verify/tests/mo.test.py.html
title: tests/mo.test.py
---
