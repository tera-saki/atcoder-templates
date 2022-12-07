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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_G
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_G
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_G\n\
    # RSQ and RAQ\nimport sys\nfrom library.lazy_segment_tree import LazySegTree\n\
    \ninput = sys.stdin.readline\n\ne = (0, 0)\nid = 0\n\n\ndef op(a, b):\n    return\
    \ (a[0] + b[0], a[1] + b[1])\n\n\ndef mapping(f, x):\n    return (x[0] + f * x[1],\
    \ x[1])\n\n\ndef composition(f, g):\n    return f + g\n\n\nN, Q = map(int, input().split())\n\
    lst = LazySegTree(N, op, e, mapping, composition, id)\nA = [(0, 1) for _ in range(N)]\n\
    lst.build(A)\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n    if\
    \ t == 0:\n        s, t, x = q\n        s -= 1\n        lst.apply(s, t, x)\n \
    \   else:\n        s, t = q\n        s -= 1\n        print(lst.prod(s, t)[0])\n"
  dependsOn:
  - library/lazy_segment_tree.py
  isVerificationFile: true
  path: tests/aoj/dsl_2_g.test.py
  requiredBy: []
  timestamp: '2022-12-07 19:04:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/dsl_2_g.test.py
layout: document
redirect_from:
- /verify/tests/aoj/dsl_2_g.test.py
- /verify/tests/aoj/dsl_2_g.test.py.html
title: tests/aoj/dsl_2_g.test.py
---
