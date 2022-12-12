---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/zaatsu.py
    title: library/zaatsu.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DSL_4_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DSL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_4_A\n\
    import sys\nfrom library.zaatsu import Zaatsu\n\ninput = sys.stdin.readline\n\n\
    \nN = int(input())\nrec = [tuple(map(int, input().split())) for _ in range(N)]\n\
    \nX = [0]\nY = [0]\nfor x1, y1, x2, y2 in rec:\n    X.append(x1)\n    X.append(x2)\n\
    \    Y.append(y1)\n    Y.append(y2)\n\nZx = Zaatsu(X)\nZy = Zaatsu(Y)\n\nA = [[0\
    \ for _ in range(Zy.N + 1)] for _ in range(Zx.N + 1)]\nfor x1, y1, x2, y2 in rec:\n\
    \    A[Zx.id(x1)][Zy.id(y1)] += 1\n    A[Zx.id(x1)][Zy.id(y2)] -= 1\n    A[Zx.id(x2)][Zy.id(y1)]\
    \ -= 1\n    A[Zx.id(x2)][Zy.id(y2)] += 1\nfor i in range(Zx.N):\n    for j in\
    \ range(Zy.N):\n        A[i + 1][j] += A[i][j]\nfor j in range(Zy.N):\n    for\
    \ i in range(Zx.N):\n        A[i][j + 1] += A[i][j]\nans = 0\nfor i, (x1, x2)\
    \ in enumerate(zip(Zx.A[:-1], Zx.A[1:])):\n    for j, (y1, y2) in enumerate(zip(Zy.A[:-1],\
    \ Zy.A[1:])):\n        if A[i][j] == 0:\n            continue\n        ans +=\
    \ (x2 - x1) * (y2 - y1)\nprint(ans)\n"
  dependsOn:
  - library/zaatsu.py
  isVerificationFile: true
  path: tests/aoj/dsl_4_a.test.py
  requiredBy: []
  timestamp: '2022-12-12 21:09:36+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/dsl_4_a.test.py
layout: document
redirect_from:
- /verify/tests/aoj/dsl_4_a.test.py
- /verify/tests/aoj/dsl_4_a.test.py.html
title: tests/aoj/dsl_4_a.test.py
---
