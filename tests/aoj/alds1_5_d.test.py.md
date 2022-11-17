---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/binary_indexed_tree.py
    title: library/binary_indexed_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_D\n\
    import sys\nfrom library.binary_indexed_tree import BIT\n\ninput = sys.stdin.readline\n\
    \nN = int(input())\nA = list(map(int, input().split()))\n\nidx = {}\nfor i, a\
    \ in enumerate(sorted(A)):\n    idx[a] = i\n\nans = 0\nbit = BIT(N)\nfor i, a\
    \ in enumerate(A):\n    ans += bit.range_sum(idx[a] + 1, N)\n    bit.add(idx[a],\
    \ 1)\nprint(ans)\n"
  dependsOn:
  - library/binary_indexed_tree.py
  isVerificationFile: true
  path: tests/aoj/alds1_5_d.test.py
  requiredBy: []
  timestamp: '2022-11-17 21:56:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/alds1_5_d.test.py
layout: document
redirect_from:
- /verify/tests/aoj/alds1_5_d.test.py
- /verify/tests/aoj/alds1_5_d.test.py.html
title: tests/aoj/alds1_5_d.test.py
---
