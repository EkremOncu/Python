# Solution 1
"""
class mycount:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        return self.start - self.step


iterator = mycount(10, 2)

for index, x in enumerate(iterator):
    if index == 10:
        break
    print(x, end=' ')
print()

def mycount(start=0, step=1):
    while True:
        start += step
        yield start - step


iterator = mycount(10,2)

for index, x in enumerate(iterator):
    if index == 10:
        break
    print(x, end=' ')
"""

# Solution 2
"""
class mycycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = self.iterable.__iter__()
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.iterator.__next__()
        except StopIteration:
            self.iterator = self.iterable.__iter__()    # Yeni iterator
            return self.iterator.__next__()

a = ['A', 'B', 'C']
for index, x in enumerate(mycycle(a)):
    if index == 10:
        break
    print(x, end=' ')
print()

def mycycle(iterable):
    while True:
        for i in iterable:
            yield i

a = ['A', 'B', 'C']
for index, x in enumerate(mycycle(a)):
    if index == 10:
        break
    print(x, end=' ')
"""

# Solution 3   ???????????????????????
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
            if self.stop > self.i:
                self.i += self.step
                return self.iterator.__next__()
            else:
                raise StopIteration

        else:
            if self.stop > self.start:
                self.start += self.step
                return self.iterator.__next__()
            else:
                raise StopIteration

import itertools
for c in Myislice(itertools.cycle('ABC'), 5):
    print(c,end=' ')
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
            return self.val

        elif self.i < self.times:
            self.i += 1
            return self.val
        else:
            raise StopIteration

g = Myrepeat(10,30)
for x in g:
    print(x, end=' ')
print()


def Myrepeat(val, times= None):
    if times == None:
        while True:
            yield val
    else:
        for i in range(times):
            yield val

g = Myrepeat(10,30)
for x in g:
    print(x, end=' ')
print()
"""