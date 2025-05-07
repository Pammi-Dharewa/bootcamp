class Counter:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)  # 1, 2, 3
