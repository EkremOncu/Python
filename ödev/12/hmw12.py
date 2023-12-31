# Solution 1
"""
class Mycount:
    def __init__(self, start, step=1):
        self.start = start
        self.step = step

    def __iter__(self):
        self.i = self.start
        return self
    def __next__(self):
        self.i += self.step
        return self.i - self.step

iterator1 = Mycount(10,2)

for index, x in enumerate(iterator1):
    if index == 100:
        break
    print(x, end=' ')
print()


def mycount(start, step=1):
    while True:
        yield start
        start = start + step

iterator = mycount(10,2)

for index, x in enumerate(iterator):
    if index == 100:
        break
    print(x, end=' ')
"""

# Solution 2
"""
class Mycycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = self.iterable.__iter__()
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.iterator.__next__()
        except StopIteration:
            self.iterator = self.iterable.__iter__()  # Yeni iterator
            return self.iterator.__next__()

a = ['A', 'B', 'C']

for index, x in enumerate(Mycycle(a)):
    if index == 100:
        break
    print(x, end=' ')
print()


def mycycle(iterable):
    while True:
        for i in iterable:
            yield i

a = ['A', 'B', 'C']

for index, x in enumerate(mycycle(a)):
    if index == 100:
        break
    print(x, end=' ')
"""

# Solution 3
