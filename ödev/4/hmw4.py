# Solution 1 
"""
while True:
    print("")
    w = input("Bir sayi giriniz:")
    word = w.strip()
    n = len(word)-1 
    s = 0
    for i in word:
        s += (ord (f"{i}") - ord("0")) * (10**n)
        n -=1
    print(s*2)
"""
# Solution 2
"""
a = int(input('int bir değer giriniz:'))

while a:
    val = a % 10
    s = chr (val + ord('0')) 
    print(s, end="")
    a //= 10
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

# Solution 4  ?????????????????  WRONG
     
y = "Bugün hava çok güzel. Ali (bizim Ali) – Veli - ve Selami parka gittiler."
#input("Bir yazi gir: ")
for i in y:
    if i.isalpha() == True:
        print(i, end=" ")




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
"""
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
"""
# Solution 11
"""
while True:
    cmd = input("CSD> ")
    
    if 'length' in cmd:
        index = cmd.find('"')
        r_index = cmd.rfind('"')
        a = cmd[index+1 : r_index]
        print(len(a))
    
    if 'upper ' in cmd:
        index = cmd.find('"')
        r_index = cmd.rfind('"')
        a = cmd[index+1 : r_index]
        print(a.upper())
    
    if 'lower ' in cmd:
        index = cmd.find('"')
        r_index = cmd.rfind('"')
        a = cmd[index+1 : r_index]
        print(a.lower())    
    
    if 'reverse' in cmd:
        index = cmd.find('"')
        r_index = cmd.rfind('"')
        a = cmd[index+1 : r_index]
        print(a[::-1])
    
    if 'repitition ' in cmd:
        index = cmd.find('"')
        r_index = cmd.rfind('"')
        a = cmd[index+1 : r_index]
        sayi = int(cmd[r_index+1:])
        print(a*sayi)
        
    if 'count ' in cmd:
        index = cmd.find('"')
        r_index = cmd.rfind('"')
        a = cmd[index+1 : r_index]        
        l = []  
        for i in range(len(a)):
            c = a.count(a[i])
            l.append([a[i],c])
        d = dict(l)
        for char, c in d.items():
            print(char, "=>", c)            
        
    if 'concat' in cmd:
          index = cmd.find('"')
          r_index = cmd.rfind('"')
          a = cmd[index+1 : r_index]
          an = a.replace('"', '')
          an = an.replace(' ', '')
          print(an)
         
    if 'quit' in cmd:
        break
"""    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
