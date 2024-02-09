# Solution 1
"""
x= 'bugün hava çok güzeldi.'

print({name for name in x if name in 'aeuüo'})
"""

# Solution 2
"""
a = [1, 2, 3, 4, 5]

print([(eleman, 'çift') if eleman % 2 == 0 else (eleman, 'tek') for eleman in a])
"""

# Solution 3
"""
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print ([list(sayi) for sayi in list (zip(*[ sayi for sayi in a] ))])


# Klasik Çözümü

l = [ [],[],[] ]

for s in range(len(a)):
    for i in range(len(a)):
        l[s].append(a[i][s])
print(l)       
"""

# Solution 4   ??????????    
"""
a = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

result= [[x[i] for x in a if len(x)>i] for i in range(max([len(row) for row in a]))]

print(result)
print('-------------')

# Klasik Çözümü

maxcol = 0
for row in a:
    if len(row) > maxcol:
        maxcol = len(row)
print(maxcol)        
print()

result = []
for i in range(len(a)):
    row = []
    
    for x in a:
        if len(x) > i:    
            row.append(x[i])
    result.append(row)    
print(result)        
"""


# Solution 5
"""
import itertools, statistics

a = [1, 2, 3, 4, 5]
print(statistics.mean([statistics.mean(x) for x in itertools.combinations(a,2)]))
"""

# Solution 6 ???????????????
"""
s = 'bugün hava çok güzel'

result= ' '.join([ ''.join([c for c in w if c not in 'aeıiuüoö']) for w in s.split()])
print(result)
""".
    
    
        








