---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/segment_tree.py
    title: library/segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import sys\nfrom library.segment_tree import SegTree\n\ninput = sys.stdin.readline\n\
    \nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\n\nst\
    \ = SegTree(N, lambda a, b: a + b, 0)\nst.build(A)\n\nfor _ in range(Q):\n   \
    \ t, x, y = map(int, input().split())\n    if t == 0:\n        st.add(x, y)\n\
    \    else:\n        print(st.query(x, y))\n"
  dependsOn:
  - library/segment_tree.py
  isVerificationFile: true
  path: tests/yosupo/point_add_range_sum.test.py
  requiredBy: []
  timestamp: '2023-01-14 13:08:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/point_add_range_sum.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/point_add_range_sum.test.py
- /verify/tests/yosupo/point_add_range_sum.test.py.html
title: tests/yosupo/point_add_range_sum.test.py
---
