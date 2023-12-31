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

def mycount(start, step=1):
    while True:
        yield start
        start = start + step

iterator = Mycount(10,2)

for index, x in enumerate(iterator):
    if index == 100:
        break
    print(x, end=' ')
print()

iterator = mycount(10,2)

for index, x in enumerate(iterator):
    if index == 100:
        break
    print(x, end=' ')
"""

# Solution 2