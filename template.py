import sys
import pypyjit
import itertools
import heapq
import math
from collections import deque, defaultdict, Counter

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
pypyjit.set_param('max_unroll_recursion=-1')
