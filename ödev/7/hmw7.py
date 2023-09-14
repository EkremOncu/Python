# Solution 1   
"""
x= 'bugün hava çok güzeldi.'

print({name for name in x if ("a" or "e" or "o" or "u" or "ü") in name})

"""
# Solution 2

def sing(r):
    for t in r:
        if t%2 == 0:
            print((t, "çift"))
        else:
            print((t, "tek"))


a = [1, 2, 3, 4, 5]
result = sing(a)

# print([sayi for sayi in a if ])
    