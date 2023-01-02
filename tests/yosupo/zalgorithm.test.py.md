---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/string.py
    title: library/string.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/zalgorithm
    links:
    - https://judge.yosupo.jp/problem/zalgorithm
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm

    import sys

    from library.string import Z_Algorhthm


    input = sys.stdin.readline


    S = input()[:-1]

    print(*Z_Algorhthm(S).Z)

    '
  dependsOn:
  - library/string.py
  isVerificationFile: true
  path: tests/yosupo/zalgorithm.test.py
  requiredBy: []
  timestamp: '2023-01-02 14:29:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/zalgorithm.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/zalgorithm.test.py
- /verify/tests/yosupo/zalgorithm.test.py.html
title: tests/yosupo/zalgorithm.test.py
---
