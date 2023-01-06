---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/lazy_segment_tree.py
    title: library/lazy_segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_H
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_H
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_H\n\
    # RMQ and RAQ\nimport sys\nfrom library.lazy_segment_tree import LazySegTree\n\
    \ninput = sys.stdin.readline\n\nINF = 1 << 30\ne = INF\nid = 0\n\n\ndef op(a,\
    \ b):\n    return min(a, b)\n\n\ndef mapping(f, x):\n    return f + x\n\n\ndef\
    \ composition(f, g):\n    return f + g\n\n\nN, Q = map(int, input().split())\n\
    lst = LazySegTree(N, op, e, mapping, composition, id)\nlst.build([0] * N)\nfor\
    \ _ in range(Q):\n    t, *q = map(int, input().split())\n    if t == 0:\n    \
    \    s, t, x = q\n        lst.apply(s, t + 1, x)\n    else:\n        s, t = q\n\
    \        print(lst.prod(s, t + 1))\n"
  dependsOn:
  - library/lazy_segment_tree.py
  isVerificationFile: true
  path: tests/aoj/dsl_2_h.test.py
  requiredBy: []
  timestamp: '2023-01-07 00:50:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/dsl_2_h.test.py
layout: document
redirect_from:
- /verify/tests/aoj/dsl_2_h.test.py
- /verify/tests/aoj/dsl_2_h.test.py.html
title: tests/aoj/dsl_2_h.test.py
---
