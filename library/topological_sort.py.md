---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_4_a.test.py
    title: tests/aoj/grl_4_a.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\nfrom typing import List, Optional\nfrom collections import deque\n\
    \n\nclass TopologicalSort():\n    def __init__(self, N: int, E: List[List[int]])\
    \ -> None:\n        self.N = N\n        self.E = E\n        self.D = [0] * N\n\
    \        for s in range(self.N):\n            for t in self.E[s]:\n          \
    \      self.D[t] += 1\n\n    def sort(self) -> Optional[List[int]]:\n        \"\
    \"\"return sorted list if sortable otherwise None\"\"\"\n        dq = deque([])\n\
    \        for i in range(self.N):\n            if self.D[i] == 0:\n           \
    \     dq.append(i)\n\n        ret = []\n        while dq:\n            v = dq.popleft()\n\
    \            ret.append(v)\n            for dest in self.E[v]:\n             \
    \   self.D[dest] -= 1\n                if self.D[dest] == 0:\n               \
    \     dq.append(dest)\n\n        for i in range(self.N):\n            if not self.D[i]\
    \ == 0:\n                return None\n        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: library/topological_sort.py
  requiredBy: []
  timestamp: '2023-01-14 16:20:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_4_a.test.py
documentation_of: library/topological_sort.py
layout: document
redirect_from:
- /library/library/topological_sort.py
- /library/library/topological_sort.py.html
title: library/topological_sort.py
---
