---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/bipartite_matching.test.py
    title: tests/yosupo/bipartite_matching.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://snuke.hatenablog.com/entry/2019/05/07/013609
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple\nfrom collections import deque\n\n\nclass\
    \ BipartiteMatching:\n    # reference: https://snuke.hatenablog.com/entry/2019/05/07/013609\n\
    \    def __init__(self, L: int, R: int):\n        self.L = L\n        self.R =\
    \ R\n\n        self.N = L + R\n        self.G = [[] for _ in range(self.N)]\n\
    \        self.pair_l = [None] * self.L\n        self.pair_r = [None] * self.R\n\
    \n    def add_edge(self, a: int, b: int) -> None:\n        \"\"\"add edges\n\n\
    \        Args:\n            a (int): left vertex index (0 <= a < L)\n        \
    \    b (int): right vertex index (0 <= b < R)\n        \"\"\"\n        assert\
    \ 0 <= a < self.L\n        assert 0 <= b < self.R\n        self.G[a].append(b)\n\
    \n    def solve(self) -> int:\n        ret = 0\n        while True:\n        \
    \    pre = [None] * self.L\n            root = [None] * self.L\n            update\
    \ = False\n\n            dq = deque()\n            for i in range(self.L):\n \
    \               if self.pair_l[i] is None:\n                    root[i] = i\n\
    \                    dq.append(i)\n            while dq:\n                v =\
    \ dq.popleft()\n                if self.pair_l[root[v]] is not None:\n       \
    \             continue\n                for d in self.G[v]:\n                \
    \    if self.pair_r[d] is None:\n                        while d is not None:\n\
    \                            self.pair_r[d] = v\n                            self.pair_l[v],\
    \ d = d, self.pair_l[v]\n                            v = pre[v]\n            \
    \            update = True\n                        ret += 1\n               \
    \         break\n                    d = self.pair_r[d]\n                    if\
    \ pre[d] is not None:\n                        continue\n                    pre[d]\
    \ = v\n                    root[d] = root[v]\n                    dq.append(d)\n\
    \            if not update:\n                break\n        return ret\n\n   \
    \ def pairs(self) -> List[Tuple[int, int]]:\n        p = []\n        for i in\
    \ range(self.L):\n            pair = self.pair_l[i]\n            if pair is None:\n\
    \                continue\n            p.append((i, pair))\n        return p\n"
  dependsOn: []
  isVerificationFile: false
  path: library/bipartite_matching.py
  requiredBy: []
  timestamp: '2023-01-02 17:52:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/bipartite_matching.test.py
documentation_of: library/bipartite_matching.py
layout: document
redirect_from:
- /library/library/bipartite_matching.py
- /library/library/bipartite_matching.py.html
title: library/bipartite_matching.py
---
