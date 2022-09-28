---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/prime_table.py
    title: library/prime_table.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1140
    links:
    - https://yukicoder.me/problems/no/1140
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1140\nimport\
    \ sys\nfrom library.prime_table import PrimeTable\n\ninput = sys.stdin.readline\n\
    \nL = 5 * 10 ** 6\nis_prime = PrimeTable(L).is_prime\n\nT = int(input())\nfor\
    \ _ in range(T):\n    a, p = map(int, input().split())\n    if is_prime[p]:\n\
    \        print(0 if a % p == 0 else 1)\n    else:\n        print(-1)\n"
  dependsOn:
  - library/prime_table.py
  isVerificationFile: true
  path: tests/prime_table.test.py
  requiredBy: []
  timestamp: '2022-09-29 01:07:36+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/prime_table.test.py
layout: document
redirect_from:
- /verify/tests/prime_table.test.py
- /verify/tests/prime_table.test.py.html
title: tests/prime_table.test.py
---
