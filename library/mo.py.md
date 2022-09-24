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
    - https://atcoder.jp/contests/abc242/submissions/29862680
    - https://atcoder.jp/contests/abc242/submissions/34629582
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://atcoder.jp/contests/abc242/submissions/34629582\nimport sys\nimport\
    \ math\ninput = sys.stdin.readline\n\n\nclass Mo:\n    # refer to following tatyam-san's\
    \ submission:\n    # https://atcoder.jp/contests/abc242/submissions/29862680\n\
    \    def __init__(self, N, Q, A, query):\n        # divide queries into \u221A\
    Q buckets\n        # thus the size of each bucket is N/\u221AQ\n        self.N\
    \ = N\n        self.Q = Q\n        self.A = A\n        self.query = query\n  \
    \      self.b_num = int(math.ceil(math.sqrt(Q)))\n        self.buckets = [[] for\
    \ _ in range(self.b_num)]\n\n        self.cnt = 0\n        self.ans = [None] *\
    \ Q\n\n        # decide which bucket the query is placed to by left-end value\n\
    \        for i in range(Q):\n            # [l:r)\n            l, r = query[i]\n\
    \            self.buckets[l * self.b_num // N].append((l, r, i))\n\n        #\
    \ sort queries in the bucket by right-end value\n        # in asc order if bucket's\
    \ index is even otherwise in desc order\n        # (the constant factor will be\
    \ smaller)\n        for i in range(self.b_num):\n            if i & 1:\n     \
    \           self.buckets[i].sort(key=lambda x: -x[1])\n            else:\n   \
    \             self.buckets[i].sort(key=lambda x: x[1])\n\n    def solve(self):\n\
    \        L = 0\n        R = 0\n        for b in range(self.b_num):\n         \
    \   for l, r, i in self.buckets[b]:\n                # extend left-end\n     \
    \           # decrement at first since current A[L] is already included ([L:R))\n\
    \                while l < L:\n                    L -= 1\n                  \
    \  self.extend_left(L)\n                # extend right-end\n                #\
    \ increment at last since current A[R] is not included yet ([L:R))\n         \
    \       while R < r:\n                    self.extend_right(R)\n             \
    \       R += 1\n                # shrink left-end\n                # increment\
    \ at last since current A[L] is included ([L:R))\n                while L < l:\n\
    \                    self.shrink_left(L)\n                    L += 1\n       \
    \         # shrink right-end\n                # decrement at first since current\
    \ A[R] is not included ([L:R))\n                while r < R:\n               \
    \     R -= 1\n                    self.shrink_right(R)\n                self.ans[i]\
    \ = self.cnt\n        return self.ans\n\n    def extend_left(self, i):\n     \
    \   raise NotImplementedError()\n\n    def extend_right(self, i):\n        raise\
    \ NotImplementedError()\n\n    def shrink_left(self, i):\n        raise NotImplementedError()\n\
    \n    def shrink_right(self, i):\n        raise NotImplementedError()\n\n\nclass\
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
  isVerificationFile: false
  path: library/mo.py
  requiredBy: []
  timestamp: '2022-09-24 15:48:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/mo.py
layout: document
redirect_from:
- /library/library/mo.py
- /library/library/mo.py.html
title: library/mo.py
---
