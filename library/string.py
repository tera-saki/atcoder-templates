class Z_Algorhthm:
    """calculate Z[i] := longest common prefix of S and S[i:]
    reference: https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05
    """

    def __init__(self, S):
        self.Z = [None] * len(S)

        self.Z[0] = len(S)
        i, j = 1, 0
        while i < len(S):
            while i + j < len(S) and S[j] == S[i + j]:
                j += 1
            self.Z[i] = j

            if j == 0:
                i += 1
                continue

            k = 1
            while k < j and k + self.Z[k] < j:
                self.Z[i + k] = self.Z[k]
                k += 1
            i += k
            j -= k
