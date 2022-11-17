import bisect


def index_lt(a, x):
    'return largest index s.t. A[i] < x or -1 if it does not exist'
    return bisect.bisect_left(a, x) - 1


def index_le(a, x):
    'return largest index s.t. A[i] <= x or -1 if it does not exist'
    return bisect.bisect_right(a, x) - 1


def index_gt(a, x):
    'return smallest index s.t. A[i] > x or len(a) if it does not exist'
    return bisect.bisect_right(a, x)


def index_ge(a, x):
    'return smallest index s.t. A[i] >= x or len(a) if it does not exist'
    return bisect.bisect_left(a, x)


def popcount(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c
