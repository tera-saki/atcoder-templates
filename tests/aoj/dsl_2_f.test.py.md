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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_F
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_F
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_F\n\
    # RMQ and RUQ\nimport sys\nfrom library.lazy_segment_tree import LazySegTree\n\
    \ninput = sys.stdin.readline\n\ne = 1 << 31\nid = 1 << 31\n\n\ndef op(a, b):\n\
    \    return min(a, b)\n\n\ndef mapping(f, x):\n    if f == id:\n        return\
    \ x\n    return f\n\n\ndef composition(f, g):\n    return g if f == id else f\n\
    \n\nN, Q = map(int, input().split())\nlst = LazySegTree(N, op, e, mapping, composition,\
    \ id)\nA = [(1 << 31) - 1] * N\nlst.build(A)\nfor _ in range(Q):\n    t, *q =\
    \ map(int, input().split())\n    if t == 0:\n        s, t, x = q\n        lst.apply(s,\
    \ t + 1, x)\n    else:\n        s, t = q\n        print(lst.prod(s, t + 1))\n"
  dependsOn:
  - library/lazy_segment_tree.py
  isVerificationFile: true
  path: tests/aoj/dsl_2_f.test.py
  requiredBy: []
  timestamp: '2022-12-18 13:51:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/dsl_2_f.test.py
layout: document
redirect_from:
- /verify/tests/aoj/dsl_2_f.test.py
- /verify/tests/aoj/dsl_2_f.test.py.html
title: tests/aoj/dsl_2_f.test.py
---
