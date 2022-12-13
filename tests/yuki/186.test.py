# verification-helper: PROBLEM https://yukicoder.me/problems/no/186
import sys
from library.math import crt

input = sys.stdin.readline

P = [tuple(map(int, input().split())) for _ in range(3)]
ans, lcm = crt(P)
print(ans if ans > 0 else lcm)
