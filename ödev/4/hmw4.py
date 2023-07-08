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
 
# Solution 3
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



























 

