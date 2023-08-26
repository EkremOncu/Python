# Solution 1 
"""
a = "001223332"
b = []

if a[0] == "0":
    b.append(a[0])
    flag = True

    
a = a.lstrip("0")
if a[0] < a[1]:
    b.append(a[0])
    b.append(a[1])
    
for i in range(len(a) - 2):
    i += 1
    if a[i] < a[i+1]:
        b.append(a[i])
    else:
        b.append(a[i+1:i+3])


print("------------")    
print(b)

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
















