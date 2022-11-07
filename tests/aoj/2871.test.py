# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/2871
import sys
from library.euler_tour import EulerTour
from library.lazy_segment_tree import LazySegTree

input = sys.stdin.readline

N, Q = map(int, input().split())
E = [[] for _ in range(N)]
P = list(map(int, input().split()))
C = input().split()
for i, p in enumerate(P, start=1):
    p -= 1
    E[i].append(p)
    E[p].append(i)

solver = EulerTour(N, E)
A = [None] * (2 * N)
for i in range(N):
    l, r = solver.get_range(i)
    if C[i] == 'G':
        A[l] = (1, 0)
        A[r] = (1, 0)
    else:
        A[l] = (0, 1)
        A[r] = (0, 1)


def op(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mapping(f, x):
    return (x[1], x[0]) if f else x


def composition(f, g):
    return f ^ g


lst = LazySegTree(2 * N, op, (0, 0), mapping, composition, 0)
lst.build(A)
for _ in range(Q):
    v = int(input()) - 1
    l, r = solver.get_range(v)
    lst.apply(l, r + 1, 1)
    g, w = lst.all_prod()
    print('broccoli' if g > w else 'cauliflower')
