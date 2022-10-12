---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/scc.py
    title: library/scc.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/two_sat.test.py
    title: tests/yosupo/two_sat.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yuki/1955.test.py
    title: tests/yuki/1955.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List\n\nfrom library.scc import SCC\n\n\nclass TwoSat:\n\
    \    def __init__(self, N: int):\n        self.N = N\n        self.E = [[] for\
    \ _ in range(2 * N)]\n\n    def vid(self, n):\n        return 2 * (~n) + 1 if\
    \ n < 0 else 2 * n\n\n    def add_clause(self, s: int, t: int) -> None:\n    \
    \    sid, tid = self.vid(s), self.vid(t)\n        # ~s -> t\n        self.E[sid\
    \ ^ 1].append(tid)\n        # ~t -> s\n        self.E[tid ^ 1].append(sid)\n\n\
    \    def if_then(self, s: int, t: int) -> None:\n        sid, tid = self.vid(s),\
    \ self.vid(t)\n        self.add_clause(~s, t)\n\n    def solve(self) -> List[bool]:\n\
    \        cid = SCC(2 * self.N, self.E).cid\n        for i in range(self.N):\n\
    \            if cid[2 * i] == cid[2 * i + 1]:\n                return None\n \
    \       # if cid[2 * a] > cid[2 * a + 1], possibly ~a -> a\n        ans = [cid[2\
    \ * i] > cid[2 * i + 1] for i in range(self.N)]\n        return ans\n"
  dependsOn:
  - library/scc.py
  isVerificationFile: false
  path: library/two_sat.py
  requiredBy: []
  timestamp: '2022-10-13 00:59:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yuki/1955.test.py
  - tests/yosupo/two_sat.test.py
documentation_of: library/two_sat.py
layout: document
redirect_from:
- /library/library/two_sat.py
- /library/library/two_sat.py.html
title: library/two_sat.py
---
