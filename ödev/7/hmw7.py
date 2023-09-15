# Solution 1   
"""
x= 'bugün hava çok güzeldi.'

print({name for name in x if ("a" or "e" or "o" or "u" or "ü") in name})

"""
# Solution 2
"""
a = [1, 2, 3, 4, 5]

print([(eleman, 'çift') if eleman % 2 == 0 else (eleman, 'tek') for eleman in a])
"""

# Solution 3
# print([(sayi, tç) for sayi in a for  ])

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print( [ list (zip(sayi)) for sayi in a ] )    