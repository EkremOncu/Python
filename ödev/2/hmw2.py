# Solution 1
"""
sayi = input("3 basamakli bir sayi giriniz: ")


a = (ord(sayi[0])- ord("0")) * 100
b = (ord(sayi[1])- ord("0")) * 10
c = (ord(sayi[2])- ord("0")) * 1
toplam = a + b + c

print(toplam)
"""

# Solution 2
"""
tam = input("3 basamakli bir sayi giriniz: ")

soz100 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

a = soz100[tam[0]] * 100
b = soz100[tam[1]] * 10
c = soz100[tam[2]] 

toplam = a + b + c

print(toplam)
"""

# Solution 3
"""
t = int (input(" bir sayi giriniz: "))
s = input("bir yazi giriniz: ")

b = len(s)

c = ((t-b)//2)

d = c + c % 2 

son = ((t-b)//2) * "." + s +  d  * "."

print(son)
"""

# Solution 4

x = int (input(" bir sayi giriniz: "))

c = x * [0]

d = [c] * len(c)

print(d)
















