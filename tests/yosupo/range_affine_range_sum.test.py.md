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
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum\n\
    import sys\nfrom library.lazy_segment_tree import LazySegTree\n\ninput = sys.stdin.readline\n\
    \n\nN, Q = map(int, input().split())\nA = list(map(int, input().split()))\nmod\
    \ = 998244353\n\n\ndef enc(x):\n    return x >> 32, x % (1 << 32)\n\n\ndef op(a,\
    \ b):\n    a0, a1 = enc(a)\n    b0, b1 = enc(b)\n    return (((a0 + b0) % mod)\
    \ << 32) + a1 + b1\n\n\ndef mapping(f, x):\n    f0, f1 = enc(f)\n    x0, x1 =\
    \ enc(x)\n    return (((f0 * x0 + f1 * x1) % mod) << 32) + x1\n\n\ndef composition(f,\
    \ g):\n    f0, f1 = enc(f)\n    g0, g1 = enc(g)\n    return (((f0 * g0) % mod)\
    \ << 32) + ((g1 * f0 + f1) % mod)\n\n\nlst = LazySegTree(N, op, 0, mapping, composition,\
    \ 1 << 32)\nA = [(a << 32) + 1 for a in A]\nlst.build(A)\nfor _ in range(Q):\n\
    \    t, *q = map(int, input().split())\n    if t == 0:\n        l, r, b, c = q\n\
    \        lst.apply(l, r, (b << 32) + c)\n    else:\n        l, r = q\n       \
    \ print(lst.prod(l, r) >> 32)\n"
  dependsOn:
  - library/lazy_segment_tree.py
  isVerificationFile: true
  path: tests/yosupo/range_affine_range_sum.test.py
  requiredBy: []
  timestamp: '2022-12-07 12:47:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/range_affine_range_sum.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/range_affine_range_sum.test.py
- /verify/tests/yosupo/range_affine_range_sum.test.py.html
title: tests/yosupo/range_affine_range_sum.test.py
---
