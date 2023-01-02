---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import bisect\n\n\ndef index_lt(a, x):\n    'return largest index s.t. A[i]\
    \ < x or -1 if it does not exist'\n    return bisect.bisect_left(a, x) - 1\n\n\
    \ndef index_le(a, x):\n    'return largest index s.t. A[i] <= x or -1 if it does\
    \ not exist'\n    return bisect.bisect_right(a, x) - 1\n\n\ndef index_gt(a, x):\n\
    \    'return smallest index s.t. A[i] > x or len(a) if it does not exist'\n  \
    \  return bisect.bisect_right(a, x)\n\n\ndef index_ge(a, x):\n    'return smallest\
    \ index s.t. A[i] >= x or len(a) if it does not exist'\n    return bisect.bisect_left(a,\
    \ x)\n\n\ndef popcount(n):\n    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)\n\
    \    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)\n    c = (c\
    \ & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)\n    c = (c & 0x00ff00ff00ff00ff)\
    \ + ((c >> 8) & 0x00ff00ff00ff00ff)\n    c = (c & 0x0000ffff0000ffff) + ((c >>\
    \ 16) & 0x0000ffff0000ffff)\n    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)\n\
    \    return c\n"
  dependsOn: []
  isVerificationFile: false
  path: library/utils.py
  requiredBy: []
  timestamp: '2023-01-02 17:52:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/utils.py
layout: document
redirect_from:
- /library/library/utils.py
- /library/library/utils.py.html
title: library/utils.py
---
