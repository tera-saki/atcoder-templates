---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 97, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\nfrom typing import List, Optional\nfrom collections import deque\n\
    input = sys.stdin.readline\n\n\nclass TopologicalSort():\n    def __init__(self,\
    \ N: int, E: List[List[int]]) -> None:\n        self.N = N\n        self.E = E\n\
    \        self.D = [0] * N\n        for s in range(self.N):\n            for t\
    \ in self.E[s]:\n                self.D[t] += 1\n\n    def sort(self) -> Optional[List[int]]:\n\
    \        \"\"\"return sorted list if sortable othereise None\"\"\"\n        dq\
    \ = deque([])\n        for i in range(self.N):\n            if self.D[i] == 0:\n\
    \                dq.append(i)\n\n        ret = []\n        while dq:\n       \
    \     v = dq.popleft()\n            ret.append(v)\n            for dest in self.E[v]:\n\
    \                self.D[dest] -= 1\n                if self.D[dest] == 0:\n  \
    \                  dq.append(dest)\n\n        for i in range(self.N):\n      \
    \      if not self.D[i] == 0:\n                return None\n        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: library/topological_sort.py
  requiredBy: []
  timestamp: '2022-09-18 13:43:26+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/topological_sort.py
layout: document
redirect_from:
- /library/library/topological_sort.py
- /library/library/topological_sort.py.html
title: library/topological_sort.py
---
