# Solution 1
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

# Solution 2   # eksik

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








