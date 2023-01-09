---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/wavelet_matrix.py
    title: library/wavelet_matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum\n\
    import sys\nimport bisect\nfrom library.wavelet_matrix import WaveletMatrix\n\n\
    input = sys.stdin.readline\n\nN, Q = map(int, input().split())\nP = [tuple(map(int,\
    \ input().split())) for _ in range(N)]\nP.sort(key=lambda x: x[0])\nX = []\nA\
    \ = []\nW = []\nfor x, y, w in P:\n    X.append(x)\n    A.append(y)\n    W.append(w)\n\
    \nWM = WaveletMatrix(A, W)\nfor _ in range(Q):\n    lx, ly, rx, ry = map(int,\
    \ input().split())\n    l, r = bisect.bisect_left(X, lx), bisect.bisect_left(X,\
    \ rx)\n    print(WM.range_sum(l, r, ly, ry))\n"
  dependsOn:
  - library/wavelet_matrix.py
  isVerificationFile: true
  path: tests/yosupo/rectangle_sum.test.py
  requiredBy: []
  timestamp: '2023-01-09 18:15:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/rectangle_sum.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/rectangle_sum.test.py
- /verify/tests/yosupo/rectangle_sum.test.py.html
title: tests/yosupo/rectangle_sum.test.py
---
