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
    PROBLEM: https://judge.yosupo.jp/problem/static_range_frequency
    links:
    - https://judge.yosupo.jp/problem/static_range_frequency
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency\n\
    import sys\nfrom library.wavelet_matrix import WaveletMatrix\n\ninput = sys.stdin.readline\n\
    \nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\nWM =\
    \ WaveletMatrix(A)\nfor _ in range(Q):\n    l, r, x = map(int, input().split())\n\
    \    print(WM.rank(l, r, x))\n"
  dependsOn:
  - library/wavelet_matrix.py
  isVerificationFile: true
  path: tests/yosupo/static_range_frequency.test.py
  requiredBy: []
  timestamp: '2023-04-17 16:54:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/static_range_frequency.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/static_range_frequency.test.py
- /verify/tests/yosupo/static_range_frequency.test.py.html
title: tests/yosupo/static_range_frequency.test.py
---
