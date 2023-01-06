---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/math.py
    title: library/math.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/discrete_logarithm_mod
    links:
    - https://judge.yosupo.jp/problem/discrete_logarithm_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod\n\
    import sys\nfrom library.math import solve_discrete_logarithm\n\ninput = sys.stdin.readline\n\
    \nT = int(input())\nfor _ in range(T):\n    x, y, m = map(int, input().split())\n\
    \    ans = solve_discrete_logarithm(x, y, m)\n    print(ans if ans is not None\
    \ else -1)\n"
  dependsOn:
  - library/math.py
  isVerificationFile: true
  path: tests/yosupo/discrete_logarithm_mod.test.py
  requiredBy: []
  timestamp: '2023-01-06 21:27:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/discrete_logarithm_mod.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/discrete_logarithm_mod.test.py
- /verify/tests/yosupo/discrete_logarithm_mod.test.py.html
title: tests/yosupo/discrete_logarithm_mod.test.py
---
