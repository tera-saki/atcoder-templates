---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/rolling_hash.py
    title: library/rolling_hash.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_14_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_14_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_14_B\n\
    import sys\nimport random\nfrom library.rolling_hash import RollingHash\n\ninput\
    \ = sys.stdin.readline\n\nT = input()[:-1]\nP = input()[:-1]\n\nmod = (1 << 61)\
    \ - 1\nbase = random.randint(100, mod - 1)\nRT = RollingHash(T, mod=mod, base=base)\n\
    RP = RollingHash(P, mod=mod, base=base)\n\ntarget = RP.get(0, len(P))\nfor i in\
    \ range(len(T)):\n    if i + len(P) > len(T):\n        break\n    h = RT.get(i,\
    \ i + len(P))\n    if h == target:\n        print(i)\n"
  dependsOn:
  - library/rolling_hash.py
  isVerificationFile: true
  path: tests/aoj/alds1_14_b.test.py
  requiredBy: []
  timestamp: '2022-11-16 21:30:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/alds1_14_b.test.py
layout: document
redirect_from:
- /verify/tests/aoj/alds1_14_b.test.py
- /verify/tests/aoj/alds1_14_b.test.py.html
title: tests/aoj/alds1_14_b.test.py
---
