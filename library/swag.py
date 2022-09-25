class SWAG:
    # reference: https://scrapbox.io/data-structures/Sliding_Window_Aggregation
    def __init__(self, op):
        self.op = op
        self.front = []
        self.back = []

    def push(self, a):
        if not self.back:
            self.back.append((a, a))
        else:
            _, acc = self.back[-1]
            self.back.append((a, self.op(a, acc)))

    def pop(self):
        assert self.front or self.back
        if not self.front:
            a, _ = self.back.pop()
            self.front.append((a, a))
            while self.back:
                a, _ = self.back.pop()
                _, acc = self.front[-1]
                self.front.append((a, self.op(a, acc)))
        self.front.pop()

    def fold(self):
        assert self.front or self.back
        if not self.front:
            return self.back[-1][1]
        if not self.back:
            return self.front[-1][1]
        return self.op(self.front[-1][1], self.back[-1][1])
