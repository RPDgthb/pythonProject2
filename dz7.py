class IterableGenerator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.start, self.stop):
            yield i


iterable_obj = IterableGenerator(1, 5)

for value in iterable_obj:
    print(value)
