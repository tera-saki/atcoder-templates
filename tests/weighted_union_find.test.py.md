---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/weighted_union_find.py
    title: library/weighted_union_find.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_B\n\
    import sys\nfrom library.weighted_union_find import WeightedUnionFind\n\ninput\
    \ = sys.stdin.readline\n\nN, Q = map(int, input().split())\nuf = WeightedUnionFind(N)\n\
    for _ in range(Q):\n    t, *q = map(int, input().split())\n    if t == 0:\n  \
    \      x, y, z = q\n        uf.merge(x, y, z)\n    else:\n        x, y = q\n \
    \       res = uf.diff(x, y)\n        print(res if res is not None else '?')\n"
  dependsOn:
  - library/weighted_union_find.py
  isVerificationFile: true
  path: tests/weighted_union_find.test.py
  requiredBy: []
  timestamp: '2022-09-23 12:31:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/weighted_union_find.test.py
layout: document
redirect_from:
- /verify/tests/weighted_union_find.test.py
- /verify/tests/weighted_union_find.test.py.html
title: tests/weighted_union_find.test.py
---
