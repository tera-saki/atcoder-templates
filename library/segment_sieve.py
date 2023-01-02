from typing import List
import math


class SegmentSieve:
    def __init__(self, N: int):
        self.square_n = math.ceil(math.sqrt(N))
        is_prime = [True] * (self.square_n + 1)
        is_prime[0] = False
        is_prime[1] = False

        for p in range(2, self.square_n + 1):
            if not is_prime[p]:
                continue
            for j in range(2, self.square_n + 1):
                if p * j > self.square_n:
                    break
                is_prime[p * j] = False

        # primes smaller than √N
        self.prime_sqn = [p for p in range(2, self.square_n + 1) if is_prime[p]]

    def get_primes(self, l: int, r: int) -> List[int]:
        """return list of primes (l <= p <= r)"""
        l = max(l, 2)
        if l > r:
            return []
        factors = self._do_sieve(l, r)
        return [p for p in range(l, r + 1) if not factors[p - l]]

    def get_factors(self, l: int, r: int) -> List[List[int]]:
        """return list of factors of n (l <= n <= r)"""
        l = max(l, 2)
        if l > r:
            return []
        factors = self._do_sieve(l, r)
        ret = [[] for _ in range(r - l + 1)]
        for i, n in enumerate(range(l, r + 1)):
            for f in factors[i]:
                if n == 1:
                    break
                while n % f == 0:
                    ret[i].append(f)
                    n //= f
            if n > 1:
                ret[i].append(n)
        return ret

    def _do_sieve(self, l: int, r: int) -> List[int]:
        is_prime = [True] * (r - l + 1)
        factors = [[] for _ in range(l, r + 1)]
        for p in self.prime_sqn:
            start = l + (-l) % p
            if start == p:
                start *= 2
            for i in range(start, r + 1, p):
                factors[i - l].append(p)
        return factors
