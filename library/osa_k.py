class Osa_k:
    # N以下の整数を素因数分解 O(NlogN)
    def __init__(self, N):
        self.min_factor = [i for i in range(N + 1)]
        for i in range(2, N + 1):
            if i * i > N:
                break
            if self.min_factor[i] == i:
                for j in range(2, N + 1):
                    if i * j > N:
                        break
                    if self.min_factor[i * j] > i:
                        self.min_factor[i * j] = i

    def factors(self, n):
        f = []
        while n > 1:
            f.append(self.min_factor[n])
            n //= self.min_factor[n]
        return f
