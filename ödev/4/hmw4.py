# Solution 1  WWRRONG
"""
while True:
    print("")
    w = input("Bir sayi giriniz:")
    word = w.strip()
    for i in word:
        s = ord (f"{i}") - ord("0")
        print(s, end="")
"""       
 
# Solution 3 ?
"""
n = int (input("Bir sayi gir: "))
l = [[0] * n for _ in range(n)]

for i in range(len(l)):
    l[i][i] = 1

for i in range(n):
    print(l[i])
"""

# Solution 4   WWRRONG
"""      
y = input("Bir yazi gir: ")

p = y.split()
p.remove("–")
p.remove("-")
print(p)
"""

# Solution 5 
"""
n = int(input("Bir sayi gir: "))

for i in range(n+1):
    if i % 2 == 0:
        print(i)

"""
# Solution 6
"""   
a = input("Bir yazi gir: ")
count_lower = 0
count_upper = 0
for i in a:
    if i.isalpha() == True:
        if i.islower() == True:
            count_lower += 1
        else:
            count_upper += 1
print(f" {count_lower} tane küçük harf vardır")                
print(f" {count_upper} tane küçük harf vardır")     
"""
# Solution 7
"""
b = input("Bir yazi gir: ")
a = []  

for i in range(len(b)):
    c = b.count(b[i])
    a.append([b[i],c])

d = dict(a)
print(d)
"""    
# Solution 8
"""
a = [12, 56, 89, 32, 19, 99, 43]

for i in range(len(a)):
    a[i] = a[i] // 10 + (a[i] % 10) *10
print(a)
"""
# Solution 9
"""
width = int(input("genişlik gir: "))
height = int(input("yükseklik gir: "))

for i in range(height):
    print("|" + i*" " + '*' + (height - i) *" " + '|')
for i in range(height):
    print("|" + (height - i)*" " + '*' +  i*" " + '|')
for i in range(height):
    print("|" + i*" " + '*' + (height - i) *" " + '|')
"""
# Solution 10
n = int(input("n sayisi gir: "))
t = 1
for _ in range(n):
    m = t * '*'
    k = m.center(n*2 -1)
    print(k)
    t +=2
t-=2    
for _ in range(n):
    m = t * '*'
    k = m.center(n*2 -1)
    print(k)
    t -=2









 

