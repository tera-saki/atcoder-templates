import sys
input = sys.stdin.readline


class RLE:
    @classmethod
    def encode(self, S):
        A = [[S[0], 1]]
        for i in range(1, len(S)):
            if S[i] != S[i - 1]:
                A.append([S[i], 1])
            else:
                A[-1][1] += 1
        return [tuple(p) for p in A]


# https://atcoder.jp/contests/abc259/tasks/abc259_c
S = input()[:-1]
T = input()[:-1]

Se = RLE.encode(S)
Te = RLE.encode(T)

if len(Se) != len(Te):
    print('No')
    exit()

for (s, n), (t, m) in zip(Se, Te):
    if s != t or n > m:
        print('No')
        exit()
    if n == 1 and m > 1:
        print('No')
        exit()
print('Yes')
