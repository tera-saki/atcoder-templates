---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/1595.test.py
    title: tests/aoj/1595.test.py
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_5_a.test.py
    title: tests/aoj/grl_5_a.test.py
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
  code: "import sys\nfrom typing import List, Tuple, Callable, TypeVar\n\nT = TypeVar('T')\n\
    \ninput = sys.stdin.readline\n\n\nclass Rerooting:\n    # reference: https://null-mn.hatenablog.com/entry/2020/04/14/124151\n\
    \    # \u9069\u5F53\u306A\u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\
    \u6728\u306B\u5BFE\u3057\u3066\u8A08\u7B97\u3055\u308C\u308B\u5024dp_v\u304C\u3001\
    v\u306E\u5B50c1, c2, ... ck\u3092\u7528\u3044\u3066\n    # \u4E0B\u8A18\u306E\u3088\
    \u3046\u306B\u8868\u3059\u3053\u3068\u304C\u3067\u304D\u308B\n    # dp_v = g(merge(f(dp_c1,c1),\
    \ f(dp_c2,c2), ..., f(dp_ck,ck)), v)\n    def __init__(self, N: int, E: List[Tuple[int,\
    \ int]],\n                 f: Callable[[T, int, int, int], T],\n             \
    \    g: Callable[[T, int], T],\n                 merge: Callable[[T, T], T], e:\
    \ T):\n        self.N = N\n        self.E = E\n        self.f = f\n        self.g\
    \ = g\n        self.merge = merge\n        self.e = e\n\n        self.dp = [[self.e\
    \ for _ in range(len(self.E[v]))] for v in range(self.N)]\n        self._calculate()\n\
    \n    def _dfs1(self, root):\n        stack = [(root, -1)]\n        ret = [self.e]\
    \ * self.N\n        while stack:\n            v, p = stack.pop()\n           \
    \ if v < 0:\n                v = ~v\n                acc = self.e\n          \
    \      for i, (c, d) in enumerate(self.E[v]):\n                    if d == p:\n\
    \                        continue\n                    self.dp[v][i] = ret[d]\n\
    \                    acc = self.merge(acc, self.f(ret[d], v, d, c))\n        \
    \        ret[v] = self.g(acc, v)\n                continue\n\n            stack.append((~v,\
    \ p))\n            for i, (c, d) in enumerate(self.E[v]):\n                if\
    \ d == p:\n                    continue\n                stack.append((d, v))\n\
    \n    def _dfs2(self, root):\n        stack = [(root, -1, self.e)]\n        while\
    \ stack:\n            v, p, from_par = stack.pop()\n            for i, (c, d)\
    \ in enumerate(self.E[v]):\n                if d == p:\n                    self.dp[v][i]\
    \ = from_par\n                    break\n            ch = len(self.E[v])\n   \
    \         Sr = [self.e] * (ch + 1)\n            for i in range(ch, 0, -1):\n \
    \               c, d = self.E[v][i - 1]\n                Sr[i - 1] = self.merge(Sr[i],\
    \ self.f(self.dp[v][i - 1], v, d, c))\n            Sl = self.e\n            for\
    \ i, (c, d) in enumerate(self.E[v]):\n                if d != p:\n           \
    \         val = self.merge(Sl, Sr[i + 1])\n                    stack.append((d,\
    \ v, self.g(val, v)))\n                Sl = self.merge(Sl, self.f(self.dp[v][i],\
    \ v, d, c))\n\n    def _calculate(self, root=0):\n        self._dfs1(root)\n \
    \       self._dfs2(root)\n\n    def solve(self, v):\n        ans = self.e\n  \
    \      for i, (c, d) in enumerate(self.E[v]):\n            ans = self.merge(ans,\
    \ self.f(self.dp[v][i], v, d, c))\n        return self.g(ans, v)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/rerooting.py
  requiredBy: []
  timestamp: '2022-12-20 01:37:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_5_a.test.py
  - tests/aoj/1595.test.py
documentation_of: library/rerooting.py
layout: document
redirect_from:
- /library/library/rerooting.py
- /library/library/rerooting.py.html
title: library/rerooting.py
---
