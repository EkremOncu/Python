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
       
disp_last_lines('teste.txt', 2)
"""

# Solution 3
"""
def get_count(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)
        print()
        asa = f.tell()
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

    wcount= len(a)  # or  asa - len(res) + 1

    return lcount,wcount,ccount,


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
def copy_file(source_path, dest_path):
    
    q = open(dest_path, 'w+')

    with open(source_path, 'r') as f:
        while True:
                s = f.read(1024)
                q.write(s)
                if s == '':
                    break
                print(s, end='')

    print()
    print("----------------")

    q.seek(0)
    po = q.read()
    print(po)

    q.close()

copy_file ('teste.txt', 'testecopy.txt')
"""
# Solution 6   # eksik

def read_csv(path, sep=',', skiprows=0, converter={}):
    with open(path,'r') as f:
        s= f.read()

        les = s.split(sep)

        s= s.replace('\n', sep)
        res = s.split(sep)

        flag = False
        s = 0
        for i in les:
            flag = '\n' in i
            s += 1
            if flag:
                break

        matris = [[] for _ in range(len(res) // s)]

        q = 0
        for i in range(len(matris)):
            for _ in range(s):
                matris[i].append(res[q])
                q += 1

        del matris[0:skiprows]

    return matris


result = read_csv("FB.csv", ';', 1)

print(result)
print()
for satir in result:
    print(satir)

