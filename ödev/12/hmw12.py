# Solution 1
"""
class Mycount:
    def __init__(self, start, step=1):
        self.start = start
        self.step = step
        self.i = self.start

    def __iter__(self):
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
"""
???????????????????????????????????????????????????????????????????????????????
class Myislice:
    def __init__(self, iterable, start, stop=None, step=1):
        self.iterable = iterable
        self.iterator = self.iterable.__iter__()
        self.step = step
        self.stop = stop
        self.i = 0

        if self.stop == None:
            self.stop = start
            self.start = 0
        else:
            self.start = start
            self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 0:
            for _ in self.iterator:
                self.i += 1
            self.stop = self.i

            if self.start == self.stop:
                raise StopIteration()
            self.start += self.step
            return self.start - self.step

        else:
            if self.start == self.stop:
                raise StopIteration()

            self.start += self.step
            return self.start - self.step

import itertools
for c in Myislice('12aas',20):
    print(c,end=' ')

???????????????????????????????????????????????????????????????????????????????
"""

# Solution 4
"""
class Myrepeat:
    def __init__(self, val, times= None):
        self.val = val
        self.times = times
        self.i = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.times == None:
            while True:
                return self.val

        elif self.i < self.times:
                self.i +=1
                return self.val
        else:
            raise StopIteration

g = Myrepeat(10,5)
for x in g:
    print(x, end=' ')
print()


def myrepeat(val, times=None):
    if not times is None:
        for i in range(times):
            yield val
    else:
        while True:
           yield val

g = myrepeat(10,5)
for x in g:
    print(x, end=' ')

"""


class Myislice:
    def __init__(self, iterable, start, stop=None, step=1):
        self.iterable = iterable
        self.iterator = self.iterable.__iter__()
        self.step = step
        self.stop = stop
        self.i = 0

        if self.stop == None:
            self.stop = start
            self.start = 0
        else:
            self.start = start
            self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 0:
            for _ in self.iterator:
                self.i += 1
            self.stop = self.i

            if self.start == self.stop:
                raise StopIteration()
            self.start += self.step
            return self.start - self.step

        else:
            if self.start == self.stop:
                raise StopIteration()

            self.start += self.step
            return self.start - self.step

import itertools
for c in Myislice(itertools.cycle('ABC'),20):
    print(c,end=' ')


