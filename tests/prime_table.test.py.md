---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: library/prime_table.py
    title: library/prime_table.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/0053
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/0053
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/0053\n\
    # verification-helper: IGNORE\nimport sys\nfrom library.prime_table import PrimeTable\n\
    \ninput = sys.stdin.readline\n\nprimes = PrimeTable(10 ** 6).primes\nS = [0]\n\
    for p in primes:\n    S.append(S[-1] + p)\nwhile True:\n    n = int(input())\n\
    \    if n == 0:\n        break\n    print(S[n])\n"
  dependsOn:
  - library/prime_table.py
  isVerificationFile: true
  path: tests/prime_table.test.py
  requiredBy: []
  timestamp: '2022-09-18 07:47:05+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: tests/prime_table.test.py
layout: document
redirect_from:
- /verify/tests/prime_table.test.py
- /verify/tests/prime_table.test.py.html
title: tests/prime_table.test.py
---
