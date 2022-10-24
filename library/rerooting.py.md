---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/1595.test.py
    title: tests/aoj/1595.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://null-mn.hatenablog.com/entry/2020/04/14/124151
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\nfrom typing import List, Callable, TypeVar\n\nT = TypeVar('T')\n\
    \ninput = sys.stdin.readline\n\n\nclass Rerooting:\n    # reference: https://null-mn.hatenablog.com/entry/2020/04/14/124151\n\
    \    # \u9069\u5F53\u306A\u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\
    \u6728\u306B\u5BFE\u3057\u3066\u8A08\u7B97\u3055\u308C\u308B\u5024dp_v\u304C\u3001\
    v\u306E\u5B50c1, c2, ... ck\u3092\u7528\u3044\u3066\n    # \u4E0B\u8A18\u306E\u3088\
    \u3046\u306B\u8868\u3059\u3053\u3068\u304C\u3067\u304D\u308B\n    # dp_v = g(merge(f(dp_c1,c1),\
    \ f(dp_c2,c2), ..., f(dp_ck,ck)), v)\n    def __init__(self, N: int, E: List[List[int]],\n\
    \                 f: Callable[[T, int], T],\n                 g: Callable[[T,\
    \ int], T],\n                 merge: Callable[[T, T], T], e: T):\n        self.N\
    \ = N\n        self.E = E\n        self.f = f\n        self.g = g\n        self.merge\
    \ = merge\n        self.e = e\n\n        self.dp = [[self.e for _ in range(len(self.E[v]))]\
    \ for v in range(self.N)]\n        self._calculate()\n\n    # def _dfs1(self,\
    \ v, p):\n    #     # \u3042\u308B\u9802\u70B9\u306E\u6839\u4ED8\u304D\u6728\u3068\
    \u3057\u3066\u3001\u305E\u308C\u305E\u306E\u9802\u70B9\u306E\u5024\u3092\u6C42\
    \u3081\u308B\n    #     acc = self.e\n    #     for i, d in enumerate(self.E[v]):\n\
    \    #         if d == p:\n    #             continue\n    #         self.dp[v][i]\
    \ = self._dfs1(d, v)\n    #         acc = self.merge(acc, self.f(self.dp[v][i],\
    \ d))\n    #     return self.g(acc, v)\n\n    def _dfs1(self, root):\n       \
    \ stack = [(root, -1)]\n        ret = [self.e] * self.N\n        while stack:\n\
    \            v, p = stack.pop()\n            if v < 0:\n                v = ~v\n\
    \                acc = self.e\n                for i, d in enumerate(self.E[v]):\n\
    \                    if d == p:\n                        continue\n          \
    \          self.dp[v][i] = ret[d]\n                    acc = self.merge(acc, self.f(ret[d],\
    \ d))\n                ret[v] = self.g(acc, v)\n                continue\n\n \
    \           stack.append((~v, p))\n            for i, d in enumerate(self.E[v]):\n\
    \                if d == p:\n                    continue\n                stack.append((d,\
    \ v))\n\n    # def _dfs2(self, v, p, from_par):\n    #     # \u305D\u308C\u305E\
    \u308C\u306E\u9802\u70B9\u3092\u6839\u3068\u3057\u3066\u307F\u305F\u6642\u306E\
    \u5024\u3092\u6C42\u3081\u308B\n    #     for i, d in enumerate(self.E[v]):\n\
    \    #         if d == p:\n    #             self.dp[v][i] = from_par\n    # \
    \            break\n    #     c = len(self.E[v])\n    #     # \u5B50\u3092\u53F3\
    \u304B\u3089\u306A\u3081\u305F\u5834\u5408\u306E\u7D2F\u7A4D\u5024\n    #    \
    \ Sr = [self.e] * (c + 1)\n    #     for i in range(c, 0, -1):\n    #        \
    \ Sr[i - 1] = self.merge(Sr[i], self.f(self.dp[v][i - 1], self.E[v][i - 1]))\n\
    \    #     Sl = self.e\n    #     for i, d in enumerate(self.E[v]):\n    #   \
    \      if d != p:\n    #             val = self.merge(Sl, Sr[i + 1])\n    #  \
    \           self._dfs2(d, v, self.g(val, v))\n    #         Sl = self.merge(Sl,\
    \ self.f(self.dp[v][i], d))\n\n    def _dfs2(self, root):\n        stack = [(root,\
    \ -1, self.e)]\n        while stack:\n            v, p, from_par = stack.pop()\n\
    \            for i, d in enumerate(self.E[v]):\n                if d == p:\n \
    \                   self.dp[v][i] = from_par\n                    break\n    \
    \        c = len(self.E[v])\n            Sr = [self.e] * (c + 1)\n           \
    \ for i in range(c, 0, -1):\n                Sr[i - 1] = self.merge(Sr[i], self.f(self.dp[v][i\
    \ - 1], self.E[v][i - 1]))\n            Sl = self.e\n            for i, d in enumerate(self.E[v]):\n\
    \                if d != p:\n                    val = self.merge(Sl, Sr[i + 1])\n\
    \                    stack.append((d, v, self.g(val, v)))\n                Sl\
    \ = self.merge(Sl, self.f(self.dp[v][i], d))\n\n    def _calculate(self, root=0):\n\
    \        self._dfs1(root)\n        self._dfs2(root)\n\n    def solve(self, v):\n\
    \        ans = self.e\n        for i, d in enumerate(self.E[v]):\n           \
    \ ans = self.merge(ans, self.f(self.dp[v][i], d))\n        return self.g(ans,\
    \ v)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/rerooting.py
  requiredBy: []
  timestamp: '2022-10-25 01:31:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/1595.test.py
documentation_of: library/rerooting.py
layout: document
redirect_from:
- /library/library/rerooting.py
- /library/library/rerooting.py.html
title: library/rerooting.py
---
