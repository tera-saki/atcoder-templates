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
    PROBLEM: https://judge.yosupo.jp/problem/range_kth_smallest
    links:
    - https://judge.yosupo.jp/problem/range_kth_smallest
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest\n\
    import sys\nfrom library.wavelet_matrix import WaveletMatrix\n\ninput = sys.stdin.readline\n\
    \nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\nWM =\
    \ WaveletMatrix(A)\nfor _ in range(Q):\n    l, r, k = map(int, input().split())\n\
    \    print(WM.quantile(l, r, k))\n"
  dependsOn:
  - library/wavelet_matrix.py
  isVerificationFile: true
  path: tests/yosupo/range_kth_smallest.test.py
  requiredBy: []
  timestamp: '2023-01-14 13:08:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/range_kth_smallest.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/range_kth_smallest.test.py
- /verify/tests/yosupo/range_kth_smallest.test.py.html
title: tests/yosupo/range_kth_smallest.test.py
---
