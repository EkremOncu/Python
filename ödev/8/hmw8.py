# Solution 
import sys
import itertools
g = {'A': {'B': 5, 'C': 7, 'D': 10},
     'B': {'A': 5, 'D': 4, 'E': 17, 'G': 20}, 
     'C': {'A': 7, 'D': 6, 'F':9}, 
     'D': {'A': 10, 'B': 4, 'C':6, 'F':12, 'E': 3},
     'E': {'B': 17, 'D':3, 'F': 14, 'G': 6 },
     'F': {'C': 9, 'D': 12, 'E': 14}, 
     'G': {'B': 20, 'E': 6, 'F': 10}    
     }

def get_length(tour):
     tlen = 0
     for i in range(len(tour) - 1):
          ddcit = g.get(tour[i])
          if ddcit is None:
               return None
          nlen = ddcit.get(tour[i+1])
          if nlen is None:
               return None
          tlen += nlen

     return tlen

result = get_length(['A', 'B', 'E', 'G'])

print(result)
print('-----')

cities = ['B','C','D','E','F','G']

min_len = sys.float_info.max  #  bir float türünün alabileceği en büyük pozitif sayı
min_tour = []
for t in itertools.permutations(cities, len(cities)):
     tour = ('A',) + t + ('A',)
     if (tlen := get_length(tour)) is None:
          continue
     if tlen < min_len:
          min_len = tlen
          min_tour = tour

print(f'min tour: {min_tour}, min tour length: {min_len}')