# -------- Solution 1 --------
"""
class CommandPrompt:
    def __init__(self,prompt):
        self.prompt = prompt

    def run(self):
        while True:
            prompt = input('write: ')
            print(prompt[::-1])

            if prompt == 'quit':
                return False

cp = CommandPrompt('CSD')
cp.run()
"""

# -------- Solution 2 --------

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def isinside(self, x, y):
        if self.x1 <= x and x <= self.x2 and self.y1 <= y  and y <= self.y2:
            return True
        else:
            return False

    def intersect(self, rect):
        pass

    def disp(self):
        print(f'x1 = {self.x1}, y1 = {self.y1}, x2 = {self.x2}, y2 = {self.y2}')

# a
r1 = Rectangle(10, 10, 20, 20)
r1.disp()
a = r1.isinside(12, 14)
print(a)
print('İçinde' if r1.isinside(12, 14) else 'İçinde Değil')

# b ?????????????????????

r2 = Rectangle(15, 15, 30, 30)
#r3 = r1.intersect(r2)
#r3.disp()


# -------- Solution 3 --------










