---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/scc.test.py
    title: tests/scc.test.py
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
    \           for t in E[s]:\n                self.I[t].append(s)\n        \n  \
    \      self.V = []\n        self.C = []\n        self.traverse()\n        self.traverse2()\n\
    \n    def toDAG(self):\n        cidx = [None] * self.N\n        for i in range(len(self.C)):\n\
    \            for v in self.C[i]:\n                cidx[v] = i\n        edge =\
    \ [set() for _ in range(len(self.C))]\n        for v in range(self.N):\n     \
    \       cv = cidx[v]\n            for dest in self.E[v]:\n                cdest\
    \ = cidx[dest]\n                if cv == cdest:\n                    continue\n\
    \                edge[cv].add(cdest)\n        edge = [list(s) for s in edge]\n\
    \        return self.C, edge\n\n    def traverse(self):\n        flag = [False]\
    \ * self.N\n        for i in range(self.N):\n            if flag[i] is False:\n\
    \                self.dfs(i, flag)\n        self.V.reverse()\n\n    def traverse2(self):\n\
    \        flag = [False] * self.N\n        for v in self.V:\n            if flag[v]\
    \ is False:\n                idx = len(self.C)\n                self.C.append([])\n\
    \                self.dfs2(idx, v, flag)\n\n    def dfs(self, v, flag):\n    \
    \    flag[v] = True\n        for dest in self.E[v]:\n            if flag[dest]\
    \ is False:\n                self.dfs(dest, flag)\n        self.V.append(v)\n\n\
    \    def dfs2(self, idx, v, flag):\n        flag[v] = True\n        self.C[idx].append(v)\n\
    \        for dest in self.I[v]:\n            if flag[dest] is False:\n       \
    \         self.dfs2(idx, dest, flag)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/scc.py
  requiredBy: []
  timestamp: '2022-09-18 07:47:05+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/scc.test.py
documentation_of: library/scc.py
layout: document
redirect_from:
- /library/library/scc.py
- /library/library/scc.py.html
title: library/scc.py
---
