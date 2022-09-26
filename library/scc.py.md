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
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SCC:\n    def __init__(self, N, E):\n        self.N = N\n        self.E\
    \ = E\n        self.I = [[] for _ in range(N)]\n        for s in range(N):\n \
    \           for t in E[s]:\n                self.I[t].append(s)\n\n        self.V\
    \ = []\n        self.cid = [None] * N\n        self.c_num = 0\n        self.traverse()\n\
    \        self.traverse2()\n\n        self.C = [[] for _ in range(self.c_num)]\n\
    \        for i in range(self.N):\n            c = self.cid[i]\n            self.C[c].append(i)\n\
    \n    def traverse(self):\n        flag = [False] * self.N\n        for i in range(self.N):\n\
    \            if flag[i] is False:\n                self.dfs(i, flag)\n       \
    \ self.V.reverse()\n\n    def traverse2(self):\n        flag = [False] * self.N\n\
    \        cid = 0\n        for v in self.V:\n            if flag[v] is False:\n\
    \                self.dfs2(v, flag)\n                self.c_num += 1\n\n    def\
    \ dfs(self, v, flag):\n        stack = [~v, v]\n        while stack:\n       \
    \     v = stack.pop()\n            if v < 0:\n                self.V.append(~v)\n\
    \                continue\n\n            if flag[v] is True:\n               \
    \ stack.pop()\n                continue\n            flag[v] = True\n        \
    \    for dest in self.E[v]:\n                if flag[dest] is False:\n       \
    \             stack.append(~dest)\n                    stack.append(dest)\n\n\
    \    def dfs2(self, v, flag):\n        stack = [v]\n        while stack:\n   \
    \         v = stack.pop()\n            flag[v] = True\n            self.cid[v]\
    \ = self.c_num\n            for dest in self.I[v]:\n                if flag[dest]\
    \ is False:\n                    stack.append(dest)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/scc.py
  requiredBy: []
  timestamp: '2022-09-26 23:57:29+09:00'
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