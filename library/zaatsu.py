class Zaatsu:
    def __init__(self, A):
        self.A = sorted(set(A))
        self.N = len(self.A)
        self.D = {a: i for i, a in enumerate(self.A)}

    def id(self, a):
        return self.D[a]

    def value(self, i):
        return self.A[i]
