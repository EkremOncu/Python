with open('teste.txt', 'w+', encoding='utf-8') as pe:
    pe.write("LeBron James(goat)\nGabe Vincent(Heat culture and injured)\nAustin Reeves(I'm him)\nRui Hachimura(Japanese)\nAnthony Davis Defensive player of the year")    
print()

# Solution 1
"""
def mygrep(path,text):
    
    with open(path, 'r', encoding='utf-8') as f:
        s= f.read()
        print(s)
        print()
        
    res= s.split('\n')
    found= [index for index, item in enumerate(res) if text in item]
    
    if found:
        for i in range(len(found)):
            print(f"<{found[i]}>: {res[found[i]]}")

mygrep('teste.txt','him')
"""
# Solution 2
"""
def disp_last_lines(path,n):
    
    with open(path, 'r', encoding='utf-8') as f:
        s= f.read()
        print(s)
        print()
        
    res= s.split('\n')
    found= [index for index,item in enumerate(res)]
    
    for i in range(len(found)-1,len(found)-n-1,-1):
        print(f'{res[i]}')    
       
disp_last_lines('teste.txt', 3)
"""
# Solution 3
"""
def get_count(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)
        print()

    res= s.split('\n')
    lcount= len(res)


    ccount= 0
    for i in range(len(res)):
        ccount += len(res[i])
    ccount += len(res)-1


    a= s.replace('\n', '')
    a= a.replace('(', ' ')
    a= a.replace(')', ' ')
    a= a.replace("'", ' ')
    a= a.split(' ')
    wcount= len(a)

    return lcount,wcount,ccount


lcount,wcount,ccount= get_count('teste.txt')
print(lcount,wcount,ccount)
"""

# Solution 4
"""
def get_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)
        print()
        f.seek(0, 2)
        size = f.tell()
        print(size)

get_file('teste.txt')
"""
# Solution 5
"""
????????????????????????????
q = open('testecopy.txt', 'w+b')
with open('teste.txt', 'rb') as f:
    while True:
            s= f.read(1024)
            t= q.write('s')
            if s == '':
                break
            print(t, end='')
????????????????????????????
"""            
 # Solution 6           









