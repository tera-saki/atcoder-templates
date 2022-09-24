---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/doubling.py
    title: library/doubling.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/2320
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/2320
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/2320\n\
    import sys\nfrom library.doubling import Doubling\n\ninput = sys.stdin.readline\n\
    \nD = ['N', 'E', 'S', 'W']\ndirect = [(-1, 0), (0, 1), (1, 0), (0, -1)]\n\n\n\
    def solve(H, W, L):\n    def h(i, j, d):\n        return (i * W + j) * 4 + d\n\
    \n    def move(i, j, d):\n        di, dj = direct[d]\n        return (i + di,\
    \ j + dj)\n\n    S = [input()[:-1] for _ in range(H)]\n    for i in range(H):\n\
    \        for j in range(W):\n            if S[i][j] == '#' or S[i][j] == '.':\n\
    \                continue\n            si = i\n            sj = j\n          \
    \  for idx, c in enumerate(D):\n                if S[i][j] == c:\n           \
    \         sd = idx\n\n    nex = [i for i in range(H * W * 4)]\n    for i in range(H):\n\
    \        for j in range(W):\n            if S[i][j] == '#':\n                continue\n\
    \            for d in range(4):\n                flag = False\n              \
    \  for k in range(4):\n                    if flag is True:\n                \
    \        break\n                    nd = (d + k) % 4\n                    ai,\
    \ aj = move(i, j, nd)\n                    if ai < 0 or ai > H - 1 or aj < 0 or\
    \ aj > W - 1:\n                        continue\n                    if S[ai][aj]\
    \ == '#':\n                        continue\n                    nex[h(i, j, d)]\
    \ = h(ai, aj, nd)\n                    flag = True\n    solver = Doubling(nex)\n\
    \    res = solver.solve(h(si, sj, sd), L)\n    a, d = divmod(res, 4)\n    i, j\
    \ = divmod(a, W)\n    print(i + 1, j + 1, D[d])\n\n\nwhile True:\n    H, W, L\
    \ = map(int, input().split())\n    if H == 0 and W == 0 and L == 0:\n        break\n\
    \    solve(H, W, L)\n"
  dependsOn:
  - library/doubling.py
  isVerificationFile: true
  path: tests/doubling.test.py
  requiredBy: []
  timestamp: '2022-09-24 15:55:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/doubling.test.py
layout: document
redirect_from:
- /verify/tests/doubling.test.py
- /verify/tests/doubling.test.py.html
title: tests/doubling.test.py
---
