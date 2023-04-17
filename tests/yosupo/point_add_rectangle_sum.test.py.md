---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/point_add_rectangle_sum.py
    title: library/point_add_rectangle_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum\n\
    import sys\nfrom library.point_add_rectangle_sum import WaveletMatrixPointAddRectangleSum\n\
    \ninput = sys.stdin.readline\n\nN, Q = map(int, input().split())\nsolver = WaveletMatrixPointAddRectangleSum()\n\
    points = [tuple(map(int, input().split())) for _ in range(N)]\nquery = [tuple(map(int,\
    \ input().split())) for _ in range(Q)]\n\nfor x, y, w in points:\n    solver.add_point(x,\
    \ y, w)\nfor t, *q in query:\n    if t == 0:\n        x, y, w = q\n        solver.add_point(x,\
    \ y)\nsolver.build()\nans = []\nfor t, *q in query:\n    if t == 0:\n        x,\
    \ y, w = q\n        solver.add_value(x, y, w)\n    else:\n        lx, ly, rx,\
    \ ry = q\n        ans.append(solver.rectangle_sum(lx, ly, rx, ry))\nprint(*ans)\n"
  dependsOn:
  - library/point_add_rectangle_sum.py
  isVerificationFile: true
  path: tests/yosupo/point_add_rectangle_sum.test.py
  requiredBy: []
  timestamp: '2023-04-17 16:54:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/point_add_rectangle_sum.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/point_add_rectangle_sum.test.py
- /verify/tests/yosupo/point_add_rectangle_sum.test.py.html
title: tests/yosupo/point_add_rectangle_sum.test.py
---
