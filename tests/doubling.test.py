# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/2320
import sys
from lib.doubling import Doubling

input = sys.stdin.readline

D = ['N', 'E', 'S', 'W']
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(H, W, L):
    def h(i, j, d):
        return (i * W + j) * 4 + d

    def move(i, j, d):
        di, dj = direct[d]
        return (i + di, j + dj)

    S = [input()[:-1] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#' or S[i][j] == '.':
                continue
            si = i
            sj = j
            for idx, c in enumerate(D):
                if S[i][j] == c:
                    sd = idx

    nex = [i for i in range(H * W * 4)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            for d in range(4):
                flag = False
                for k in range(4):
                    if flag is True:
                        break
                    nd = (d + k) % 4
                    ai, aj = move(i, j, nd)
                    if ai < 0 or ai > H - 1 or aj < 0 or aj > W - 1:
                        continue
                    if S[ai][aj] == '#':
                        continue
                    nex[h(i, j, d)] = h(ai, aj, nd)
                    flag = True
    solver = Doubling(nex)
    res = solver.solve(h(si, sj, sd), L)
    a, d = divmod(res, 4)
    i, j = divmod(a, W)
    print(i + 1, j + 1, D[d])


while True:
    H, W, L = map(int, input().split())
    if H == 0 and W == 0 and L == 0:
        break
    solve(H, W, L)
