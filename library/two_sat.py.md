---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/two_sat.test.py
    title: tests/two_sat.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from library.scc import SCC\n\n\nclass TwoSat:\n    def __init__(self, N):\n\
    \        self.N = N\n        self.E = [[] for _ in range(2 * N)]\n\n    def add_clause(self,\
    \ s, t):\n        def vid(n):\n            return 2 * (~n) + 1 if n < 0 else 2\
    \ * n\n\n        def oppose(id):\n            return id - 1 if id & 1 else id\
    \ + 1\n\n        sid, tid = vid(s), vid(t)\n        # ~s -> t\n        self.E[oppose(sid)].append(tid)\n\
    \        # ~t -> s\n        self.E[oppose(tid)].append(sid)\n\n    def solve(self):\n\
    \        cid = SCC(2 * self.N, self.E).cid\n        for i in range(self.N):\n\
    \            if cid[2 * i] == cid[2 * i + 1]:\n                return None\n\n\
    \        ans = []\n        for i in range(self.N):\n            # possibly ~x\
    \ -> x\n            if cid[2 * i] > cid[2 * i + 1]:\n                ans.append(1)\n\
    \            else:\n                ans.append(-1)\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: library/two_sat.py
  requiredBy: []
  timestamp: '2022-09-25 12:09:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/two_sat.test.py
documentation_of: library/two_sat.py
layout: document
redirect_from:
- /library/library/two_sat.py
- /library/library/two_sat.py.html
title: library/two_sat.py
---
