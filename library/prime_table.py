class PrimeTable:
    def __init__(self, N):
        self.is_prime = [True] * (N + 1)

        self.is_prime[0] = False
        self.is_prime[1] = False
        for i in range(2, N + 1):
            if i * i > N:
                break
            if self.is_prime[i] is False:
                continue
            for j in range(2, N + 1):
                if i * j > N:
                    break
                self.is_prime[i * j] = False

        self.primes = [n for n in range(2, N + 1) if self.is_prime[n]]
