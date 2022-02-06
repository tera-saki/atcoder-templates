class Modpow:
    def __init__(self, p):
        self.p = p
        self.inv = {}
    
    def pow(self, n, m):
        if m == 0:
            return 1
        if m > 0:
            return pow(n, m, self.p)
        if m < 0:
            if self.inv.get(n) is None:
                self.inv[n] = pow(n, self.p - 2, self.p)
            return pow(self.inv[n], -m, self.p)