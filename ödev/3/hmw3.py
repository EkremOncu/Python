# Solution 1

a = [10, 'ali', 'veli', 20, 'selami']
b = ['selami', 20, 'veli', 'ali', 10]

k = a == b[::-1]

print (k)

# Solution 2

ilkyazi = set(input("ilk yazıyı giriniz: "))
ikinciyazi = set(input("ikinci yazıyı giriniz: "))


print(ilkyazi == ikinciyazi)