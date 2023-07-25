# Solution 1 
"""
def disp_shape(n):
    k = 1
    s = 0 
    for i in range(n):
        print(" " * s, end=" ")
        for i in range(k, n+1):
            print(i, end=" ")

        print("")
        k = k+1
        s = s+1

    t = n - 1
    for i in range(n):
        print(" " * (s-1), end=" ")
        for i in range(n, t, -1):
            print(i, end=" ")

        print("")
        t = t-1
        s = s-1

n = int(input("Bir sayi giriniz: "))
disp_shape(n)
"""


# Solution 2  ???????????????????????
"""
def crown(n):
    t = 0
    s = 0
    for i in range(n):
        print(" " * (2*s-2)  , end=" ")
        for i in range(1, 2+t):
            print(i, end="")
        
        print("")
        t = t+1
        s = s+1
n = 3
crown(n)
"""

# Solution 3
"""
def is_armtrong(a):
    a_ = a
    summ = 0
    while a:
        summ += (a % 10)**3
        a = a // 10
    return summ if a_ == summ else 0

while True:
    a = int(input('Bir sayı giriniz:'))
    is_armtrong(a)
    if a == 0:
        break
    print('Armstrong' if is_armtrong(a) else 'Armstrong değil')
"""

"""
def is_armtrong(a):
    a_ = a
    summ = 0
    num_digits = len(str(a))
    while a:
        summ += (a % 10) ** num_digits
        a = a // 10
    return summ if a_ == summ else 0

def print_armstrongs(n):
    for i in range(n):
        if is_armtrong(i):
            print(i, end=" ")

print_armstrongs(1000000)
"""

# Solution 4  
"""
n = input("Bir yazı giriniz: ").strip()
a = n.split()
print(n)
for i in range(len(a)):
    index = n.find(' ') - 1
    print(n[index::-1],end=" ")
    index += 1
    n = n[index:].strip()
"""

# Solution 5
"""
def digitate(vals):
    b = []
    r = []
    for i in range(len(vals)):
        a = str(vals[i])
        r.append(tuple(b))
        b.clear()
        for k in range(len(a)):
            b.append(int(a[k]))
    r.remove(())
    return r
vals = [23, 4, 765, 34589, 42]
result = digitate(vals)
print(result) # [(2, 3),(4, ), (7, 6, 5), (3, 4, 5, 8, 9), (4, 2)]
"""

# Solution 6
"""   
n = input("Bir yazı giriniz: ").strip()
a = n.split()
print(a)
"""
    
# Solution 7
"""
def print_shape(n):
    k = 0
    n_ = n
    for i in range(n):
        a = n_ * "*"
        b = k * ' '
        c = n_* "*"
        print(a + b + c, end="")
        k +=2
        n_-=1
        print("")

    k = n*2-2
    for i in range(n):
        a = (i+1) * "*"
        b = k * ' '
        c = (i+1) * "*"
        print(a + b + c, end="")
        k -= 2
        print("")
    
print_shape(int(input("bir deger giriniz: ")))
"""
    
# Solution 8
"""
def disp_char_pattern(ch):

    di = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    k = 0
    index = di.index(ch)
    n_ = di[:index+1]

    n = (index * 2 + 1) // 2
    k = 0
    for i in range(len(n_)):
        a = n * ' '
        b = di[i]
        c = k * '  '
        if di[i] == 'A':
            d = ''
        else:
            d = di[i]
        e = n * ' '

        print(a + b + c + d + e, end="")
        k += 1
        n -= 1
        print("")

    n = (index * 2 + 1) // 2
    k = 0
    for i in range(len(n_)):
        a = k * ' '
        b = di[index]
        c = n * '  '
        if di[index] == 'A':
            d = ''
        else:
            d = di[index]
        e = k * ' '
        print(a + b + c + d + e, end="")
        k += 1
        n -= 1
        index -= 1
        print("")
disp_char_pattern('F')
"""
    
# Solution 9
"""
import math
def newton_pi(k):
    pi = 0
    for n in range(k):
        pi += (2**(n+1) * math.factorial(n) ** 2) / math.factorial(2*n+1)
    return pi

result = newton_pi(500)
print(result)
"""
    
# Solution 9-b ????????????????
"""
def somayaji_pi(n):
    pi = 0
    r = 3
    t = 3
    p = 5
    s = 5
    for _ in range(n):
        pi += (4 / (t**3 -r)) - (4 / (p**3 -s))
        t += 2
        r += 2
        p += 2
        s += 2
    pi = pi + 3
    return pi

result = somayaji_pi(1)
print(result)
"""
    
# Solution 9-c
"""
def bailey_borwein_plouffe_pi(k):
    pi = 0
    for n in range(k):
        pi += (1/16)**n * ( (4/(8*n+1)) - (2/(8*n+4)) - (1/(8*n+5)) - (1/(8*n+6)) )
    return pi

result = bailey_borwein_plouffe_pi(5)
print(result)
"""

# Solution 10

def sort_tuple_list(a):









