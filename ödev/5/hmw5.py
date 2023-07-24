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



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
