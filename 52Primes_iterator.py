class Primes:
    def __init__(self, first, last=None):
        self.curr = None

        if last is None:
            self.first = 2
            self.last = first
        else:
            self.first = first
            self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr is None:
            self.curr = 2
            return self.curr

        while self.curr < self.last:
            self.curr += 1
            if Primes.__prime(self.curr):
                return self.curr
        raise StopIteration()

    def __prime(n):
        for d in range(2, n):
            if n % d == 0:
                return False
        return True


for p in Primes(100):
    print(p)
