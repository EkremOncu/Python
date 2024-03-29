# Solution 1   
"""
def increasing_numbers(s):
    vals = []
    prev_val = int(s[0])
    vals.append(prev_val)
    beg_index = 1
    
    for i in range(1,len(s)):
        val = int(s[beg_index : i+1])
        
        if val > prev_val:
            vals.append(val)
            prev_val = val
            beg_index = i + 1
            
    return vals

s = input('sayısal karakterlerden oluşan yazı giriniz:')
result = increasing_numbers(s)
print(result)
"""
# Solution 2
"""
def consecutive_total(a, n):
    b = []
    match n:
        case 2:
            for i in range(len(a) - 1):
                b.append(a[i]+a[i+1])

            maxValue = max(b)
            maxValue_index = b.index(maxValue)
            print((maxValue,maxValue_index))
        case 3:
            for i in range(len(a) - 2):
                b.append(a[i] + a[i + 1] + a[i + 2])

            maxValue = max(b)
            maxValue_index = b.index(maxValue)
            print((maxValue, maxValue_index))
            print(b)
        case 4:
            for i in range(len(a) - 3):
                b.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])

            maxValue = max(b)
            maxValue_index = b.index(maxValue)
            print((maxValue, maxValue_index))
            print(b)

        case 5:
            for i in range(len(a) - 4):
                b.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4])

            maxValue = max(b)
            maxValue_index = b.index(maxValue)
            print((maxValue, maxValue_index))
            print(b)

a = [3, 8, 6, 9, 4, 7, 5, 5, 98]
consecutive_total(a, 3)
"""
"""
# Solution 3

def move_machine(s):
    
    result = s.replace(" ", "").lower().split(";")
    x = 0; y = 0
    
    for i in range(len(result)):
        if 'up' in result[i]:
            val = int(result[i][2])
            x += val
        if 'down' in result[i]:
            val = int(result[i][4])
            x -= val
    
        if 'left' in result[i]:
            val = int(result[i][4])
            y -= val
    
        if 'right' in result[i]:
            val = int(result[i][5])
            y += val
    
    return x,y

s = 'Up     4    ; DowN 2 ; Down 3;     Left 4; Up 2; right 3'

x, y = move_machine(s)
print(x,y)
"""

# Solution 4
"""
import random

a = []
hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(5000):
    column = random.sample(range(1, 10000), 5) # iadesiz cekim
    x = (column[0] + column[1] + column[2] + column[3] + column[4]) / 5 
    a.append(x)
    
for i in range(len(a)):
    if 0 <= a[i] < 1000:
        hist[0] += 1

    if 1000 <= a[i] < 2000:
        hist[1] += 1
    
    if 2000 <= a[i] < 3000:
        hist[2] += 1        

    if 3000 <= a[i] < 4000:
        hist[3] += 1

    if 4000 <= a[i] < 5000:
        hist[4] += 1
        
    if 5000 <= a[i] < 6000:
        hist[5] += 1

    if 6000 <= a[i] < 7000:
        hist[6] += 1

    if 7000 <= a[i] < 8000:
        hist[7] += 1

    if 8000 <= a[i] < 9000:
        hist[8] += 1
        
    if 9000 <= a[i] < 10000:
        hist[9] += 1

print(hist)        

print(hist[0] * 'X')
print(hist[1] // 18 * 'X')
print(hist[2] // 18 * 'X')
print(hist[3] // 18 * 'X')
print(hist[4] // 18 * 'X')
print(hist[5] // 18 * 'X')
print(hist[6] // 18 * 'X')
print(hist[7] // 18 * 'X')
print(hist[8] // 18 * 'X')
print(hist[9] // 18 * 'X')     
"""

# Solution 5
"""
import random

a = []
hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(5000):
    column = random.sample(range(1, 10000), 5) # iadesiz cekim
    x = (column[0] + column[1] + column[2] + column[3] + column[4]) / 5 
    a.append(x)
    
for i in range(len(a)):
    if 0 <= a[i] < 1000:
        hist[0] += 1

    if 1000 <= a[i] < 2000:
        hist[1] += 1
    
    if 2000 <= a[i] < 3000:
        hist[2] += 1        

    if 3000 <= a[i] < 4000:
        hist[3] += 1

    if 4000 <= a[i] < 5000:
        hist[4] += 1
        
    if 5000 <= a[i] < 6000:
        hist[5] += 1

    if 6000 <= a[i] < 7000:
        hist[6] += 1

    if 7000 <= a[i] < 8000:
        hist[7] += 1

    if 8000 <= a[i] < 9000:
        hist[8] += 1
        
    if 9000 <= a[i] < 10000:
        hist[9] += 1

print(hist) 


import matplotlib.pyplot as plt

plt.hist(a, 10)
plt.show()
"""

# Solution 6
"""
import matplotlib.pyplot as plt

def gauss(x):
    import math
    return math.exp((-1/2) * (x**2)) * 1 / (math.sqrt(2 * math.pi))

a = -10
x = []
y = []
while a < 10:
    x.append(a)
    a += 0.1

for i in range(len(x)):
    val = gauss(x[i])
    y.append(val)

plt.plot(x, y)
plt.show()
"""
















