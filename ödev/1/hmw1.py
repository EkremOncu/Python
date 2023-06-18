"""a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a1 = a [:5]
a2 = a [5:100]
print(a2 + a1)"""
# Solution
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

mid = len(a) // 2
temp = a[:mid]
print(a[:mid])
a[:mid] = a[mid + len(a) % 2:]
a[mid + len(a) % 2: ] = temp
print(a)

# soru 2
n = int(input("Tek basamaklı bir sayı gir: "))
b = n * (1 + 11 + 111 + 1111 + 11111)
print(b)