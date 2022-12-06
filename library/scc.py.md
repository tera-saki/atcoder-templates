---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: library/two_sat.py
    title: library/two_sat.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/0366.test.py
    title: tests/aoj/0366.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/scc.test.py
    title: tests/yosupo/scc.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SCC:\n    def __init__(self, N, E):\n        self.N = N\n        self.E\
    \ = E\n        self.I = [[] for _ in range(N)]\n        for s in range(N):\n \
    \           for t in E[s]:\n                self.I[t].append(s)\n\n        self.V\
    \ = []\n        self.cid = [None] * N\n        self.c_num = 0\n        self._traverse()\n\
    \        self._traverse2()\n\n        self.C = [[] for _ in range(self.c_num)]\n\
    \        for i in range(self.N):\n            c = self.cid[i]\n            self.C[c].append(i)\n\
    \n    def to_dag(self):\n        NE = [set() for _ in range(self.c_num)]\n   \
    \     for i in range(self.N):\n            ci = self.cid[i]\n            for j\
    \ in self.E[i]:\n                cj = self.cid[j]\n                if ci == cj:\n\
    \                    continue\n                NE[ci].add(cj)\n        return\
    \ self.C, [list(ne) for ne in NE]\n\n    def _traverse(self):\n        flag =\
    \ [False] * self.N\n        for i in range(self.N):\n            if flag[i] is\
    \ False:\n                self._dfs(i, flag)\n        self.V.reverse()\n\n   \
    \ def _traverse2(self):\n        flag = [False] * self.N\n        cid = 0\n  \
    \      for v in self.V:\n            if flag[v] is False:\n                self._dfs2(v,\
    \ flag)\n                self.c_num += 1\n\n    def _dfs(self, v, flag):\n   \
    \     stack = [~v, v]\n        while stack:\n            v = stack.pop()\n   \
    \         if v < 0:\n                self.V.append(~v)\n                continue\n\
    \n            if flag[v] is True:\n                stack.pop()\n             \
    \   continue\n            flag[v] = True\n            for dest in self.E[v]:\n\
    \                if flag[dest] is False:\n                    stack.append(~dest)\n\
    \                    stack.append(dest)\n\n    def _dfs2(self, v, flag):\n   \
    \     stack = [v]\n        while stack:\n            v = stack.pop()\n       \
    \     if flag[v] is True:\n                continue\n            flag[v] = True\n\
    \            self.cid[v] = self.c_num\n            for dest in self.I[v]:\n  \
    \              if flag[dest] is False:\n                    stack.append(dest)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/scc.py
  requiredBy:
  - library/two_sat.py
  timestamp: '2022-12-06 18:26:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/scc.test.py
  - tests/aoj/0366.test.py
documentation_of: library/scc.py
layout: document
redirect_from:
- /library/library/scc.py
- /library/library/scc.py.html
title: library/scc.py
---
