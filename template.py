import sys
import pypyjit
import itertools
import heapq
import math
from collections import deque, defaultdict
import bisect

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
pypyjit.set_param('max_unroll_recursion=-1')


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
