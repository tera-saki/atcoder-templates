---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/dual_segment_tree.py
    title: library/dual_segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D\n\
    import sys\nfrom library.dual_segment_tree import DualSegTree\n\ninput = sys.stdin.readline\n\
    \nN, Q = map(int, input().split())\ndst = DualSegTree(N, lambda a, b: max(a, b),\
    \ (-1, (1 << 31) - 1))\nfor i in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        a, b, x = q\n        dst.query(a, b + 1, (i, x))\n  \
    \  else:\n        i, = q\n        print(dst.get(i)[1])\n"
  dependsOn:
  - library/dual_segment_tree.py
  isVerificationFile: true
  path: tests/aoj/dsl_2_d.test.py
  requiredBy: []
  timestamp: '2023-01-05 19:39:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/dsl_2_d.test.py
layout: document
redirect_from:
- /verify/tests/aoj/dsl_2_d.test.py
- /verify/tests/aoj/dsl_2_d.test.py.html
title: tests/aoj/dsl_2_d.test.py
---
