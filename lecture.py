"""
s = ' abcd'
a = list(s)
c = [1, 2, 3,]
c.sort(reverse= True)
print(a)
print(c)
c.reverse()
print(c) 
"""
# sorted(iterable, key=None, reverse=False)
"""
numbers = [5, 2, 8, 1, 9]

sorted_numbers = sorted(numbers) # reverse = False
print(sorted_numbers)

fruits = ['apple', 'banana', 'orange', 'kiwi']

sorted_fruits = sorted(fruits, key=len)
print(sorted_fruits)

liste = [('a', 2), ('b', 1), ('d', 23), ('c', 13)]

sorted(liste, key= lambda x:x[1])
"""

"""
a = [10, 20, 30, 40, 50, 60, 70]
print(id(a))
b = a[::-1] # shallow copy
print(b)
print("b id = " ,id(b))
print("a id = " ,id(a))
print("")
print (id(b[0]))
print (id(a[-1])) 
"""

"""
aa = [10, 20, 30, 40, 50, 60, 70]
del aa[2::-1]
print (aa)

d = [1, 2, 3, [4,5]]
sd = 4  in d
print(sd)

a = [10, 20, 30, 40.5, 50, 60, 70, 80, 90, 100]
a[0:5:2] = [1, 2, 3]
print(a)

liste = [1, 2, 3, 4, 5]

liste.insert(1, "yeni")
print(liste)

"""


"""
a = [10, 20, 30, 40.5]
b = 3 * a  # b = a + a + a, anlamına geliyor
print(b)
print ("----")
print (id(a))
print (id(b))
print ("----")
print(id(b[0]))
print(id(b[4]))
print(id(b[8]))
"""

"""
a = [10, 20, 30, 40.5]
print (id(a))
a *= 3    # a *= n ile a.extend(n) eşdeğerdir,  a += n ile a.extend(n) eşdeğerdir
print (a)
print (id(a))
"""

"""
a = [[]] * 3
print(a)
a[0].append(200)
print (a)
c = [1,2]
b = [c,c,c]
print(b)
c.append(200)
c[0] = 100
print(b)
"""

"""
a = (30,)  # geçerli
print(len(a))
print(a)
b = 1, 2, 3, 5.2
print(b)
print(type(b))
"""

"""
t = (1, 2, 3, 'ali')
print(t)
print(hash(t)) # hash degeri elde edilir 

a = [10, 20, 30]
x, y, z = a    # Unpacking islemi
print(x,y,z)
print(type(x))
"""
"""
t = [1, 2, 3, 'ali']
t.extend(["56", 646, True]) # extend metodu sadece iterable elemanlar ekler
# t.extend(646) TypeError: 'int' object is not iterable
print(t)
"""

# -----------------------  KUMELER ----------------------------------------
"""
a = {1, 5, (2,4), 'ali'}
print(a)  
a = {1, 5, (2,4), 'ali', [22,46]} # TypeError: unhashable type: 'list'
# Kümelerde hushable degildir, yani kümenin elemanı küme olamaz.
print(a)

# Kümeler(set) mutable dir.
"""


"""
s = {'ali', 10, 'veli', 'istanbul'}
s.update([30, 'izmir', 'selami'])
print(s)
print("")
s = {'istanbul', 'selami', 'ali', 10, 'izmir', 'veli', 30}
s.update('sakarya')
print(s)
print("")
# s.update(30) TypeError: 'int' object is not iterable
s.add(5646515)
s.add("SAGEGWRRWGWRGWE")
print(s) 
"""

""" 
Kümenin elemanı:
küme olamaz   Çünkü hashable değil
list olamaz   Çünkü hashable değil
tuple olabilir
list ve tuple ın elemanı küme olabilir

#t = {1, (45, 68, [59,57,49] )}
#print(t) TypeError: unhashable type: 'list'
"""

"""
s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
k = s.copy()
print(k) # küme elemanları shallow copy şeklinde kopyalanır
print(s)
"""

"""
s = {'ali', 10, 'veli', 'eskişehir'}
k = {10, 'eskişehir', 'adana', 20}

result = s.intersection(k)
print (result) # result_o = s & k -> s ve k kume(set) olmali

result2 = s.intersection(['ali', 'adana', 'eskişehir'])
print(result2) 
# s -> kume olmali,  sag taraf ise ITERABLE olmali

word1 = input('Bir sözcük giriniz:')
word2 = input('Bir sözcük daha giriniz:')

s = set(word1)

result = s.intersection(word2)
print(result) # type(result) -> set
"""
"""
s = {'ali', 'veli', 'selami', 'ayşe', 'fatma','hüseyin'}
k = ['ali', 'fatma', 'hüseyin', 'ayşe']
m = ['ayşe', 'ali', 'fatma', 'can']

obb = s.intersection(k, m) # 3'nün kesisimini buluyor.
"""

"""
r = s.intersection(b)         # '&' -> kesisim (s n b)
r = s.union(b)                # '|' -> birlesme (s u b)
r = s.difference(b)           # '-' -> iki kumenin farki (s/b) gibi
r = s.symmetric_difference(b) # '^' -> ortak olmayan elemanlar (exor islemi)
r = s.isdisjoint(b)           #      -> ayrik kume  (operator karsiligi yok)
     
 Yukarıda görmüş olduğumuz temel küme işlemlerinin update'li versyonları da vardır. 
 Bunlar aşağıda listelenmiştir:

 a &= b  ya da a.intersection_update(b)
 a |= b  ya da a.update(b)
 a -= b  ya da a.diffrence_update(b)
 a ^= b  ya da a.symmetric_difference_update(b)

 Yukarıdaki işlemlerde sonuç başka bir nesne olarak elde edilmemektedir.
 Sonuç soldaki nesne değiştirilerek elde edilmektedir. 
 Yani bu işlemler sonucunda yeni bir nesne yaratılmamaktadır

a <= b  # superset (ust kume)         -> result = a.issubset(b)
a >= b  # subset (alt kume)           -> result = a.issuperset(b)
a <  b  # proper subset (oz alt kume) -> icin bir metotu yok
a >  b  # proper superset (oz ust kume) -> icin bir metotu yok

"""
"""
fs = frozenset(['ali', 'veli', 'selami', 'ayşe', 'fatma'])
print(fs) # set sinifinin degistirilemez (immutable) bicimi
print(type(fs)) # elemanlari hashable ise frozensette hashable olur
print("")

fss = frozenset('ali')
print(fss)
print(type(fss)) 
print("")


fs = frozenset(['ali', 'veli', 'selami', 'ayşe', 'fatma'])
s = {'ali', 'sacit', 'veli'}

result = fs & s
print(result, type(result))

result_2 = s & fs
print(result_2, type(result_2))
"""

# ---------------------------------  Dict -------------------------------------------
"""
# Sozluklerin anahtarlari hashable olmali, ancak degerler icin bu gecerli değil
# Sozluklerin kendiside hash'lenebilir (hashable) değildir, 
# dict'ler mutable nesnelerdir

a = [('ali', 10), ('veli', 20), ('selami', 30), ('ayşe', 40), ('fatma', 50),"as","fb"]
d = dict(a)
# dict fonksiyonuna biz iki elemanlı dolaşılabilir nesnelerden verebiliriz (sadece 2)
print(d)

val = d.get("asfas")
print(val) # olamayan bir sey girsen de program error vermiyo -> None veriyor
print(d.get("asfas"), "not found")

if val == None:
    print("Anahtar yok")
else:
    print(val)    
# del d['ali'],  d.pop('ali')
"""
"""
d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
print(d)
print("")
d.update([('sacit', 100), ('mehmet', 200), ('sibel', 300)])

va = val = d.pop('ali', "anahtar yok")
print(va)
print("")
val = d.pop('amc', "anahtar yok")
print(val)
print("")
print(d)

keys = list(d)   # ['veli', 'selami', 'ayşe', 'fatma', 'sacit', 'mehmet', 'sibel']
keyss = d.keys() # dict_keys(['veli', 'selami', 'ayşe', 'fatma', 'sacit', 'mehmet', 'sibel'])
type(d.keys())   #  dict_keys
b = list(keyss) # ['veli', 'selami', 'ayşe', 'fatma', 'sacit', 'mehmet', 'sibel']
  
vals = d.values() # dict_values([20, 30, 40, 50, 100, 200, 300])
type(d.values()) #  dict_values
a = list(vals) # [20, 30, 40, 50, 100, 200, 300]
"""
#  View Nesnesi !!!!! onemli dropboxdan bak
"""
d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}

al = d.get(70, 'sacit') # 70'i arıyor yoksa 'sacit' i veriyor
print(d)
print(al) 
print("")

val = d.setdefault(70, 'sacit') # 70'i arıyor yoksa 'sacit' i ekliyor 
print(d)  
print(val)  
print("")

aal = d.setdefault(40, 'sacit')
print(aal)   
"""
# Deyimler bir deger vermezler (del d[10]), operatorler verirler val = (d.pop(10))

# Python'da "padding", bir veri dizisinin veya dizesinin başına veya sonuna eklenen belirli bir karakter veya karakterlerin işlemidir.



# ------------------------------- String Sınıfı ------------------------------------------------------
"""
s = "123456"
s[1] # 2
id(s[0]) # 2384674482800

# String Metotları
ss = 'LeBron James'
ss.capitalize() 
ss.title()
ss.upper()

k = ss.center(20) # 20'lık bir alan icinde k'yı en merkeze koyuyur
print(":" + k + ":")
k1 = ss.center(21,".") # padding
print(k1) 

ord("a") # Python'da bir karakterin Unicode değerini (tam sayı olarak) döndüren yerleşik bir fonksiyon. 
# "ord" kısaltması "ordinal" anlamına gelir. ord'ın icine sadece 1 karakter yazilabilir.

r = "ankara"
val = r.find("k")  # 2 
val1 = r.find("ar")# 3
val2 = r.find("gew2hgrwg")# -1

r.find("k",3,20) # aramanın start oldugu index, stop old index, 3 dahil 20 değil
r.index("k") # find'dan tek farki bulamaz ise ValueError olur.

r.rfind("a",3,20) # reverse find, aramayı sondan basa dogru yapar
r.rindex("a")     # rfind'dan tek farki bulamaz ise ValueError olur.

r.count('a')


path = input("Bir yol ifadesi giriniz: ") # r'c:\windows\system\test.dll' -> r ters bölüler icin(\)
                                          # r kullanmasak  (\\) su sekil yazmam lazimdi 
index = path.rfind('\\')
fname = path[index +1:]

print(fname)        # test.dll


s = '2abc2'
s.isdigit()
s.isupper()
s.islower()
s.isalnum() # alfabetik ve numeric
s.isalpha() # butun karakterler str mi
s.isidentifier() #  bu string'in, değişken olarak kullanilip kullanilamayacagini gosteriyor.
"""
"""

s = ","
result= s.join(['ali', 'v103li', 'selami']) # argümanı iterable nesne olmali, str olmali 
# 'ali, v103li, selami'

result2 = '\n'.join(['ali', 'veli', 'selami'])
print(result2)

sa = 'ali, veli, selami, ayşe, fatma'
result_a = sa.split(', ') # split -> list veriyor,  bosluga dikkat

d = '13/06/2022'
a = d.split('/') # join ve split birbirinin tersi
da = '13/ 06/ 2022' # bosluga dikkat
aa = da.split('/')

bsl = 'sad              fsag      616    \t\t  safsaf \n'
bsl.split() # bosluklari atar


rte = '            LeBron  King           James                                    '
king = rte.strip() # sadece basindaki ve sonundaki bosluklari siler

afs = '.,.,.,.,.,Ali Serçe.,.,.,.,.'
serce = afs.strip(' ., ') # strip() parametrede alabiliyor 

lead = '      Ali Serçe      '
le = lead.lstrip() # sadece leading space'leri atar

tral = '     Ali Serçe......rrrrrrrrr'
re = tral.rstrip(" r. ") # sadece traling space'leri atar

asklm = "MelisaAycaIdil"
ozldm = asklm.partition('Ayca') # ('Melisa', 'Ayca', 'Idil') -> 3'lü TUPLE
asklm.partition('xxx') #  ("MelisaAycaIdil", "" , "")


sdr = 'ali top at, ali ip atla'
kap = sdr.replace('ali', 'veli')


den = '- bu bir denemedir'
startw = den.startswith('-') 
startq = den.startswith('-a')

ass = 'bu bir denemedir...'
rt = ass.endswith('...')
"""

# ---- Leksikografik karsilastirma
  
resal = 'a' > 'B' # True, UNICODE tabloda once buyuk harfler sonra kucuk harfler gelmektedir
#  b > a     -> True

# char() ->  ord fonksiyonunun yaptigi seyin tersi chr fonksiyonuyla yapılabilmektedir. Bizden int bir degeri
#  parametre olarak alır. Onun UNICODE tablodaki karakter karsiligini tek elemanlı bir string olarak verir.

a = 10
b = 20
c = 30
#print(a,b,c, sep='xx')

# -------------------------------- Format Metoduyla Formatli Yazim ----------------------------------------------
"""
s = 'a = {0}, b = {1}, c = {2}'.format(a, b, c) # a = 10, b = 20, c = 30

sd = 'a = {2}, b = {1}, c = {0}'.format(a, b, c) # a = 30, b = 20, c = 10

# Ayrıntılı formatlama işlemi küme parantezi içerisinde ':' sentaksı ile yapılmaktadır. Örneğin:

day = 8
month = 5
year = 2007

date= '{0:02d}/{1:02d}/{2:05d}'.format(day, month, year) # 08/05/02007



# ------------------------------ String Enterpolasyonu ----------------------------------------------------

sas = f'a = {a}, b = {b*b}, c = {c}' # a = 10, b = 400, c = 30

sql = f'{a:<12}{b:>14}'# sola dayali , saga dayali

# Farklı turlerin esittir karsilastirilmasi (==) her zaman FALSE, Farklı turlerin esit degildir karsilastirilmasi (!=) her zaman True


# indent (girinti) -> indentasyon Python'da kodun düzenini ve bloklarını belirlemek için kullanılan bir yapıdır. 
# Girintili bir şekilde yapılandırılmış kod, okunabilirlik ve kodun doğru çalışması açısından önemlidir.    
"""



# ------------------------------------- DEYİM (Statament) ----------------------------------------------------

# Programlar deyimlerin calismasi ile calisir
# Suit -> Python'da bileşik deyimin anahtar sözcüğü ile aynı satıra yazılan birden fazla basit deyime ya da 
#    -> farklı satırlara aynı girinti düzeyiyle yazılan birden fazla deyime "suit" denilmektedir. 


# ------------------------ For --------------------------------

# for <degisken ismi> in <iterable nesne> : <suite>  
"""
d = {'ali': 58, 'veli': 87, 'selami': 59, 'ayşe': 98, 'fatma': 81}

for x in d.values():
    print(x)

print("---------")

a = [(1, "thy"), (3, 4), (5, 6), (7, "Gundo"), (9, 10)]

for t in a:
    x, y = t  # Unpacking
    print(x,y)

print("---------")

d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}

for key in d:
    print(f"{key} -> {d[key]}")

print("")

for key, value in d.items():
        print(key, value)

print("---------")        
        
a = [10, 20, 30, 40, 50]
        
for x in reversed(a):   # for i in range(len(a) - 1, -1, -1):
    print(x)
"""

# ------------------------ Break --------------------------------
# Break basit deyimi mutlaka döngünün içinde olmalıdır


# ----------------------- Match --------------------------------
"""
a = int(input('Bir değer giriniz:'))

match a:
    case 1:
        print('bir')
    case 2:
        print('iki')
    case 3:
        print('üç')
    case 4:
        print('dört')
    case 5:
        print('beş')
    case _:  # under score ozel bir anlam tasır (else anlamı) ve sonda bulunmalidir
        print('Hicbiri')

s = input('Bir şehir giriniz:')

match s:
    case 'ankara':
        print('06')
    case 'eskişehir':
        print('26')
    case 'kocaeli':
        print('41')
    case 'adana':
        print('01')
    case 'izmir':
        print('35')
    case _:
        print('hiçbiri')

# Bir case bölümünde "veya" biçiminde birden fazla kalıp "|" atomu ile oluşturulabilmektedir.
# Bu kalıba "veya kalıbı (or pattern)" denilmektedir

while True:
    cmd = input('CSD>').strip()
    if cmd == '':
        continue
    match cmd:
        case 'copy':
            print('copy executes')
        case 'rename':
            print('rename executes')
        case 'del' | 'erase' | 'remove' as aas_cmd:  # hangisi, kullanici tarafindan girildi anlamak icin
            print(f'{aas_cmd} executes...')
        case 'quit' | 'exit':
            break
        case _:
            print(f'invalid command: {cmd}')

"""
"""
while True:
    cmd = input('CSD>').split() # split() komutu list veriyor
    if cmd =='':
        continue
    match cmd:
        case['rename']:
            print('rename executes')

        case 'copy', source_path, dest_path:
            print(f"copy executes, {source_path} {dest_path}")

        case (['del',file] | ['erase', file] | ["remove", file]) as hop_name:
            print(f'{hop_name[0]} executes, {file}')

        case 'king', *path: # [king, *args] ,  0 ya da daha fazla elemanla uyusum saglar
            # * olunca sinirsiz oluyor,  * sonda olmak zorunda değil
            print(f"rename executes, {path}") # çikti her zaman list olur

        case ['quit']:
            break
        case _:
            print(f'invalid command: {cmd}')
print(file)
"""
"""
a = [10, 20, 30, 40, 50]
match a:
    case 10, _, _, 40, 50:
        print('matched')

print("")

#------------- mapping pattern -------------------
d = {'ali': 10, 'veli': 20, 'selami': 30, 'ayşe': 40, 'fatma': 50}
match d:
    case {'selami': 30, 'fatma': 50, **kwargs}: # ** sadece dict ler icin kullanilir, ** sonda bulunmak zorunda
        print(kwargs)           # {'ali': 10, 'veli': 20, 'ayşe': 40}
"""

# capture pattern
"""
while True:
    a = int(input('Bir değer giriniz:'))
    match a:
        case 10:
            print('on')
        case 20:
            print('yirmi')
        case x:     # capture pattern
            print(f' x = {x}')
"""

# koruma (guard)
"""
a = int(input('Bir sayı giriniz:'))
x = -2

match a:
    case 10 if x > 0:
        print('Ok')
# a'nin 10 olmasinin yani sira ayni zamanda x'in de 0'dan buyuk olmasi gerekmektedir 
    case _:
        print('cannot match...')      
"""

# -------------- Kosul Operatoru (If deyiminden farklı) ------------------
"""
# -> Adından da anlasildigi gibi bir operatordur, degim degil
# <ifade1> if <ifade2> else <ifade3>  ->  b = 100 if a % 2 == 0 else 200
# -> <a % 2 == 0> True ise b'ye 100 atanacak, degilse b'ye 200 atanacak (b=200 olacak)

a = int(input("deger gir: "))
b = 100 if a % 2 == 0 else 200
print(b)

# Koşul operatörü özellikle üç durumda tercih edilmelidir:
#1- Bir karşılaştıma sonucunda elde edilen degerin bir degişkene atandıgı durumlarda. Ornegin:
result = 100 if a % 2 == 0 else 200

#2- Fonksiyon ya da metot çagrımlarında arguman olarak koşul operatoru bazen yazımı kısaltmak icin kullanılabilmektedir. Ornegin:
# val = int(input('Bir sayı giriniz:'))
# print('çift' if val % 2 == 0 else 'tek')

#3- return ifadelerinde de koşul operatörü bazı durumlarda tercih edilmektedir. Ornegin:
# return 100 if a % 2 == 0 else 200


for i in range(100):
        print(i, end='\n' if i % 5 == 4 else ' ')
"""

# -------------------------------- Fonksiyonlar -------------------------------------
# Foksiyonlar hashable degildir -> Bu nedenle set'lerin elemanı olamaz ve dict'lerin anahtari olamazlar.(dict'lerin degeri olabilirler)
"""
def bar():
    print("bar")
def tar():
    print("tar")
def foo():
    print("foo")

a = [bar, tar, foo]
a[0]()
a[1]()
a[2]()
print("")

for f in a:
    f()
print("")


import math
def getroots(a,b,c):

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

result = getroots(3, 5, -7)

if result:
    x1, x2 = result
    print(f'x1 = {x1}, x2 = {x2}')
else:
    print('no real root!')
"""

# Neden Fonksiyon Kullanilir?
"""
Peki biz neden fonksiyon yazmak isteriz? iste fonksiyonlar olusturmanin gerekceleri şunlardir:
1) Fonksiyonlar "yeniden kullanilabilirligi (reusability)" saglarlar.
2) Fonksiyonlar kod tekrarini engellemektedir.
3) Karmasik bir problem parcalarina ayrilarak daha kolay cozulebilir.
4) Fonksiyonlarin isimleri vardir. Bu nedenle yapilmak istenen sey fonksiyon cagrilariyla daha iyi ifade edilebilmektedir.

Iste programlamada bir islemin fonksiyonlara ayrilarak fonksiyonlarin birbirlerine çagirmasi biciminde gerceklestirilmesine 
    "prosedurel programlama modeli (procedural paradigm)" denilmektedir.

def bar():
    return "bar"
def tar():
    print("tar")
def foo():
    print("foo")

d = {1: bar, 2: tar, 3:foo}
print(d[1]())
print(d[2]())
print("")
"""

# Asal Kontrol
"""
def isprime(val):
    for i in range(2, val - 1):
        if val % i == 0:
            return False

    return True


val = int(input('Bir sayı giriniz:'))

print('Asal' if isprime(val) else 'Asal değil')
print("")

# 2' den val'a kadar (val dahil) ki tum asal sayilar
for i in range(2, val+1):
    if isprime(i):
        print(i, end=' ')
"""


# Asal Kontrol algortimasinin daha efektif ve hizli hali
"""
import math

def isprime(a):
    if a % 2 == 0: # Önce, "a" sayısının 2'ye bölümünden kalan kontrol edilir.
# Eğer "a" çift bir sayıysa (2'ye tam bölünüyorsa), fonksiyon yalnızca "a == 2" ifadesini kontrol eder.
# Eğer "a" 2'ye eşitse, yani "2" ise, fonksiyon "True" döndürür, aksi takdirde "False" döndürür.
        return a == 2

    for i in range(3, int(math.sqrt(a)) + 1, 2):
        if a % i == 0:
            return False

    return True

a = int(input('Bir sayı giriniz:'))

print('Asal' if isprime(a) else 'Asal değil')
print("")

for i in range(2, a+1):
    if isprime(i):
        print(i, end=' ')
"""



"""
def disp_range(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0

    for i in range(start, stop, step):
        print(i, end=' ')
    print()
    
disp_range(10)
disp_range(10, 20)
disp_range(10, 20, 2)
"""

# Raise
"""
def banner(s, ch='-'): # isinstance(s, str) -> s nesnesi str ise True, degilse False dondurur
    if not isinstance(s, str):
        raise TypeError('first argument must be string')
    if not isinstance(ch, str) or len(ch) != 1:
        raise TypeError('second argument must be one charater string')
    print(ch * len(s))
    print(s)
    print(ch * len(s))

banner('ankara', 'ali')
"""

"""
#  Parametredeki "*" gerçek bir parametre değildir. Yani asagidaki foo fonksiyonunun 4 parametresi vardir
def foo(a, b, *, c, d=10):
    pass
# '*'ın sagindaki tüm parametreler cagrim sirasinda isimli argumanlarla cagrilmak zorundadir.



def foo(a, b, /, c = 100, d = 200):
        pass # Fonksiyonun parametre listesinde bir parametre yalnızca '/' biciminde girilmişse
# bu durum "onun solundaki tum parametreler argumanlarin pozisyonel olarak girilmesi gerektigi" anlamina gelmektedir.


def foo(a, b, *c):
    print(f"a= {a}, b= {b}, c= {c}")

foo(10, 20, 30,645,23)
print("")
"""

"""
def myprint(*objects, sep=' ', end='\n'):
    i = 0
    while i < len(objects):
        if i != 0:
            print(end=sep)
        print(objects[i], end='')
        i += 1
    print(end=end)


myprint(10, 20, 30)
myprint(10, 20, 30, sep='*')
myprint(10, 20, 30, sep='*', end='/')
"""

"""
def mymax(*args):
    iterable = args[0] if len(args) == 1 else args

    maxval = None
    for x in iterable:
        if maxval == None or x > maxval:
            maxval = x

    return maxval


a = [1, 6, 3, 2, 5]

result = mymax(a)
print(result)  # 6

result = mymax(4, 16, 2, 3)
print(result)  # 16

print("----------------------")

def mymin(*args):
    iterable = args[0] if len(args) == 1 else args

    minval = None
    for x in iterable:
        if minval == None or x < minval:
            minval = x

    return minval


a = [1, 6, 3, 2, 5]

result = mymin(a)
print(result)  # 1

result = mymin(4, 16, 2, 3)
print(result)  # 2
"""

"""
def foo(a, b, *args, **kwargs): # **'lı parametre sonda olmali, * ve ** parametreleri sadece 1 tane olur,
    # *'lı parametre default deger alamazlar ve isimli olarak argüman iceremezler
    print(type(kwargs))
    print(type(args))
    print('a = {}, b = {}, args = {}, kwargs = {}'.format(a, b, args, kwargs))


foo(10, b=20, sad=20, rad=30)
"""

"""
def foo(a, b, **kwargs):
    legal_args = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

    for key in kwargs:
        if key not in legal_args:
            print(f'invalid argument: {key}={kwargs[key]}')
            return

    c = kwargs.get('c', 100)
    d = kwargs.get('d', 200)
    e = kwargs.get('e', 300)
    f = kwargs.get('f', 400)
    g = kwargs.get('g', 500)
    h = kwargs.get('h', 600)
    i = kwargs.get('i', 700)
    j = kwargs.get('j', 800)
    k = kwargs.get('k', 900)
    l = kwargs.get('l', 1000)
    m = kwargs.get('m', 1100)

    print(f'c = {c}, d = {d}, e = {e}, f = {f}, g = {g}, h = {h}, i = {i}, j = {j}, k = {k}, l = {l}, m = {m}')


foo(10, 20, c=10, f=20, i=30,k=40)  # c = 10, d = 200, e = 300, f = 20, g = 500, h = 600, i = 30, j = 800, k = 40, l = 1000, m = 1100
print()
foo(10, 20)
print("-----------------------------------------------------------")


def foo(a, b, **kwargs):
    legal_args = {'c': 100, 'd': 200, 'e': 300, 'f': 400, 'g': 500, 'h': 600, 'i': 700, 'j': 800, 'k': 900, 'l': 1000,
                  'm': 1100}

    for key in kwargs:
        if key not in legal_args:
            print(f'invalid argument: {key}={kwargs[key]}')
            return

    for key, value in kwargs.items():
        legal_args[key] = value

    for key, value in legal_args.items():
        print(f'parameter: {key}, value: {value}')


foo(10, 20, c=10, f=20, i=30, k=40)
print()
foo(10, 20)
"""

"""
# *'li argumanlarin "dolasilabilir (iterable)" nesne belirtmesi gerekir
def foo(a, b, c, d, e):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')

t = 10, 20, 30
foo(1, 2, *t)  # a = 1, b = 2, c = 10, d = 20, e = 30

a = [5, 6, 7, 8, 9, 10]
b = {100, 200, 300}
print(*a, 10, *b)                   # 5 6 7 8 9 10 10 200 100 300
print(*range(20,30))
print()

def bar(a, b, *c):
    print(f'a = {a}, b = {b}, c = {c}')
x = [10, 20, 30, 40, 50, 60]
bar(1, *x)  # a = 1, b = 10, c = (20, 30, 40, 50, 60)
print()

d = {10: 'ali', 20: 'veli', 30: 'selami', 40: 'ayşe', 50: 'fatma'}
print(*d)                   # 10 20 30 40 50
print(*d.values())          # ali veli selami ayşe fatma
"""

# **'lı argumanlar bir sozluk nesnesi olmak zorundadır. Bu argumanlara 
# iliskin sozluk nesnelerinin anahtarlarının str turunden olmasi gerekir.
"""
def foo(a, b, c, d, e, f):
    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}')

d = {'c': 100, 'd': 200, 'e': 300}
foo(10, 20, **d, f=400)  # a=10, b=20, c=100, d=200, e=300, f=400
"""

# Forwarding
"""
def myprint(*args, **kwargs):
    print(*args, **kwargs)  # perfect forwarding
myprint(10, 20, 30, sep=', ', end='*')


"forwarding" bir bir fonksiyonun aldığı parametreleri baska bir fonksiyona 
argüman olarak iletmesi durumuna denilmektedir.Yukarıdaki örnekte myrint 
fonksiyonu kendisi hangi argümanlarla çağrılmışsa print fonksiyonunu da o 
argümanlarla çağırmıştır. 
"""

# **'lı argümanlar bir sözlük nesnesi olmak zorundadır. Bu argümanlara ilişkin sözlük nesnelerinin
# anahtarlarının str türünden olması gerekir. Ancak değerleri herhangi bir türden olabilir.

# Ozyineleme (recursion)
"""
def add(*args):
    total = 0
    for x in args:
        total += x

    return total

result = add(1, 2, 3, 4, 5, *(7, *(8, 9)), *[9, 2, *(3, 5, 6)])
print(result)
"""

# -------------- MODULE ----------------
"""
import math
print(type(math)) # <class 'module'>
print(math.sqrt(10)) # 3.1622776601683795

x = math
print(x.sqrt(10)) # 3.1622776601683795
print(type(x))
"""

# from utility import add   -> Aslında bu işlemin eşdeğeri şöyledir:
"""     import utility
        add = utility.add
        del utility     """

# __init__ -> "dunder init" demekle biz "__init__" demiş olmaktayız.

# if __name__ == '__main__':
# biz yazdığımız programdaki fonksiyonların ve değişkenlerin import edilerek 
# kullanılmasını istiyorsak ve aynı zamanda da onu bağımsız bir program 
# gibi de çalıştırmak istiyorsak kullanilir


# ------------------------------- Rastgele Sayı Uretme ----------------------------------------------

"""
for _ in range(1):
    result = random.random()
    print(result)
print("")
#  Fonksiyonun ilk parametresi ortalamayı, ikinci parametresi standart sapmayı belirtir:
for i in range(3):
    result = random.gauss(100, 15)
    print(result)
"""
"""
import random

result = random.randint(10, 20) # kesikli düzgün (discrete uniform) dagilim
print(result)    # 10 ve 20 dahil
print()

# random.choice( sequence container ya da küme )
a = ['ali', 'veli', 'selami', 'ayşe', 'fatma']
result = random.choice(a)
print(result)
print()

# random.sample( sequence container ya da küme , int) -> Ayni degerleri dondurmez
a = ('ali', 'veli', 'selami', 'ayşe', 'fatma')
result = random.sample(a, 3)
print(result)
print()

column = random.sample(range(1, 50), 6) # iadesiz cekim
print(column)
print()

names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']
result = random.choices(names, k=8)     # iadeli cekim
print(result)
print()

result = random.randrange(0, 10, 2)
print(result) # Burada aslında biz 0, 2, 4, 8 sayıları arasında rastgele bir sayı üretmiş oluruz. 
print()    

a = ['ali', 'veli', 'selami', 'ayşe', 'fatma']
print(a)
random.shuffle(a) # inplace olarak karistiriyor
print(a)
def myshuffle(a):
    for i in range(len(a)):
        k = random.randrange(len(a))
        a[k], a[i] = a[i], a[k]
              
names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']  
myshuffle(names)
print(names)
print()
"""
#  Aşağıdaki örnekte bir oyun kartı destesi oluşturulmuş sonra da bu deste dört oyuncuya dağıtılmıştır. 
# Ancak oyunculara dağıtılan kartlar sıraya da dizilmiştir.
"""
import random

card_vals = {'As': 14, 'Papaz': 13, 'Kız': 12, 'Vale': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
card_types = {'Kupa': 3, 'Maça': 2, 'Karo': 1, 'Sinek': 0}

def build_deck():
    deck = []

    for cval in card_vals:
        for ctype in card_types:
            deck.append((cval, ctype))
        
    return deck

def distribute(deck):
    random.shuffle(deck)

    players = [[], [], [], []]
    
    for i in range(52):
        players[i % 4].append(deck[i])
        
    for player in players:
       player.sort(key=keyfunc, reverse=True)

    return players

def keyfunc(t):
    cval, ctype = t
    return card_vals[cval] * 4 + card_types[ctype]  
   
def disp_players(players):  
    for player in players:
        print(player)
        print('-------')
  
def main():
    deck = build_deck()
    players = distribute(deck)
    disp_players(players)
    
main()  
"""

# ------ Enumerate Fonksiyonu ------

"""-> enumerate isimli built-in fonksiyon bizden dolaşılabilir bir nesne alır, 
bize dolaşılabilir bir nesne verir. iki elemanlı demetler elde edilecektir.
"""

"""
names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

for t in enumerate(names,10):
    print(t)
print()
for index,name in enumerate(names):
    print(index,name)
"""

# ------ Degiskenlerin faaliyet alanı (scope) ------

""" Python'da değişkenler faaliyet alanları bakımından üç gruba ayrılmaktadır:

    1) Yerel Değişkenler (Local Variables)
    2) Global Değişkenler (Global Variables)
    3) Sınıf Değişkenleri (Class Variables)
"""

# ---------------- map Fonksionu -------------------

# map (fonksiyon nesnesi, iterable, *iterable)
"""
-----------------------------------------------------------------------------
Bu fonksiyon bizden bir fonksiyonu ve dolaşılabilir bir nesneyi parametre 
olarak alır. Bize bir dolaşım (iterator) nesnesi verir.
-----------------------------------------------------------------------------
iterator nesnesi bir kez dolasılip biter 

iterator (dolasim) nesne
iterable (dolasilabilir) nesne 


a = [3, 13, 23, 33]
iterable = map(int, a)

for x in iterable:
    print(x, end=" ")

print()

for x in iterable:
    print(x, end=" ")
"""


"""
s = '1 2 3 4 5'

total = 0
for x in map(int, s.split()):
    total += x
    
print(total)
print()
"""

"""
-----------------------------------------------------------------------------
Tabii map fonksiyonunun birinci parametresi bir metot da olabilir. 
Ancak metotlar tek başına kullanılamazlar. Metotlar ancak 
ilişkin oldukları sınıf türünden bir değişkenle '.' operatörü ile 
kullanılabilirler. Bu durumda map fonksiyonunun birinci parametresine 
metot vereceksek metodu isimle değil <değişken>.<metot> biçiminde vermeliyiz
-----------------------------------------------------------------------------
"""

"""
a = [1, 2, 3, 4, 5]
b = ['ali', 'Ja']
c = [100.34, 200, 300.23, 400, 500]

def foo(*x):
    return x

iterable = map(foo, a, b, c)
for x in iterable:
    print(x)

print()
"""


# ----------- iç içe(nested) fonksionlar -----------

"""    
Tabii iç fonksiyonun içerisinde de başka bir fonksiyon tanımlanabilir. 
Bu tür durumlarda iç fonksiyon ismi yerel bir değişken olmaktadır. 
Dolayısıyla iç fonksiyon ancak dıştaki fonksiyonun içerisinden çağrılabilir. 

Aşağıdaki örnekte biz bar fonksiyonunu ancak foo fonksiyonun içerisinde ve 
bar tanımlandıktan sonra çağırabiliriz. bar fonksiyonunu dışarıdan çağıramayız:

def foo():
    print('foo')
    def bar():
        print('bar')
    bar()

foo()    
"""

"""
import math 

def print_primes(n):
    def isprime(val):
        if val % 2 == 0:
            return val == 2
        for i in range(3, int(math.sqrt(val)) + 1, 2):
            if val % i == 0:
                return False
        return True
    
    for x in range(2, n + 1):
        if isprime(x):
            print(x, end=' ')
        
print_primes(100)
"""
# nonlocal
"""
def foo():
    a = 10
    def bar():
        nonlocal a
        a = 20          # buradaki a foo'nun a'sı
        print(a)        # foo'nun a'sı, 20
    bar()
    print(a)            # foo'nun a'sı, 20
    
foo()
"""

# -------------- globals built-in fonksiyonu --------------
"""
----------------------------------------------------------------------------------
Bir sözlük nesnesi biçiminde bize verir. Sözlüğün anahtarları global 
değişkenlerin isimlerinden değerleri ise onların değerlerinden oluşur.
globals fonksiyonu ile global değişkenleri elde ettiğinizde sizin yaratmadığınız 
başka değişkenleri de görürseniz şaşırmayınız. Örneğin biz daha önce __name__ 
isimli global değişkenin yorumlayıcı tarafından oluşturulduğunu görmüştük. 
Benzer biçimde bütün built-in değişkenler __builtins__ isimli bir 
global sözlük nesnesi içerisinde bulunmaktadır. 
-----------------------------------------------------------------------------------
"""
"""
a = 10
name = 'ali'

def foo():
    pass

g = globals()
print(g)
print(list(g)) # ['__name__', '__file__', '__nonzero__', '__builtins__', 'a', 'name', 'foo', 'g']
"""

# -------------- locals built-in fonksiyonu --------------
"""
------------------------------------------------------------------------------------
globals fonksiyonuna benzeyen locals isimli bir built-in fonksiyon daha vardır. 
locals fonksiyonu hangi fonksiyon içerisinde çağrılmışsa o fonksiyonun yerel 
değişkenlerini bir sözlük olarak vermektedir. locals fonksiyonu global 
düzeyde çağrılırsa tamamen globals fonksiyonu çağrılmış gibi etki göstermektedir. 
------------------------------------------------------------------------------------
"""
"""
a = 10

def foo():
    b = 20
    d = locals()
    print(d)            # {'b': 20}
    print(list(d))      # ['b']
    
def bar():
    a = 30
    c = locals()
    print(c)            # {'a': 300}
    print(list(c))      # ['a']
    
foo()
print()
bar()
"""


# -------------------- Comprehensions(içlemler) -------------------------1
"""
1) Liste içlemleri (list comprehensions)
2) Küme içlemleri (set comprehensions)
3) Sözlük içlemleri (dictionary comprehensions)
"""

# Liste içlemleri -> [<ifade> for <değişken> in <dolaşılabilir nesne> if <koşul> ]
"""
a = [i * i for i in range(10)]
print(a)
print()

# Bu işlemin eşdeğeri şöyledir: 

temp = []
for i in range(10):
    temp.append(i * i)
a = temp
print(a)
print()

names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']
print(*[len(name) for name in names])
"""

"""# if kosulu

a = [i for i in range(10) if i % 2 == 0]
print(a)        # [0, 2, 4, 6, 8]
print()

sentences = ['anastas mum satsana', 'izmir', 'ey edip adanada pide ye', 'eskişehir', 'adamla çeneç almada']

palindromes = [sentence for sentence in sentences if sentence == sentence[::-1]]
print(palindromes)
"""


"""
------------------------------------------------------------------------------------
Aslında içlemlerin içerisinde birden fazla for döngüsü de olabilir. 
Yani aşağıdaki gibi içlemler de söz konusu olabilir:
------------------------------------------------------------------------------------
"""
# result = [ifade for x in iterable1 for y in iterable2 if koşul]

"""
------------------------------------------------------------------------------------    
İç içe for döngüleri nasıl çalışıyorsa buradaki çalışma da benzer biçimdedir.
Dıştaki döngünün her bir yinelemesinde içteki döngü baştan sona 
çalıştırılmaktadır. Yukarıdaki içlemin kod karşılığı şöyle ifade edilebilir:
------------------------------------------------------------------------------------
temp = []
for x in iterable1:
    for y in iterable2:
        if koşul:
            temp.append(ifade)    
result = temp
"""

"""
a = [[0, 0, 0, 0, 0] for _ in range(5)]
a[0][0] = 100
print(a)
print()

# alt ve üst aynısı, Comprehension'dan kaynaklı, shallow copy yok ikisinde de

a = [[0, 0, 0, 0, 0] for _ in range(5)]
a[0][0] = 100
print(a)
"""

# Küme içlemleri -> [<ifade> for  <değişken>  in  <dolaşılabilir nesne> if <koşul>]

# Sözlük içlemleri -> { <key: value>  for <değişken> in <iterable> if <koşul>}
"""
a = [1, 2, 3, 4, 5]

d = {x: str(x) for x in a}
print(d)

print()

d = {}
for x in a:
    d[x] = str(x)
    
print(d)
"""

# ---------------- zip built-in fonksionu -------------------
# def zip(*iterables):
"""   
------------------------------------------------------------------------------------
zip fonksiyonu bizden dolaşılabilir nesneleri alır ve bize geri dönüş 
değeri olarak bir dolaşım nesnesi verir. zip fonksiyonun geri 
döndürdüğü dolaşım nesnesini dolaştığımızda demetler elde ederiz.
------------------------------------------------------------------------------------
"""   
    
"""
a = ['ali', 'veli', 'selami']
b = [10, 20, 30, 50, 65, 956, 65, 654, 852, 564, 656, 5123, 26494]
c = [5.2, 3.8, 4.6]

z = zip(a, b, c)

for t in z:
    print(t)
"""

# unzip
"""
a = ['ali', 'veli', 'selami']
b = [10, 20, 30, 50, 65, 956, 65, 654, 852, 564, 656, 5123, 26494]
c = [5.2, 3.8, 4.6]

z = zip(a, b, c)

d,e,f = zip(*z)
print(d)
print(e)
print(f)
"""

"""
a = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

for t in zip(*enumerate(a)):
    print(t)
"""

# ---------------- kombinasyon / permütasyon ----------------
"""
import math

a = math.perm(5, 3) # 60
b = math.comb(5, 3) # 10


------------------------------------------------------------------------------------
itertools modülündeki permutations isimli fonksiyon bizden dolaşılabilir 
bir nesneyi ve bir sayıyı parametre olarak alır ve bize dolaşılabilir 
bir nesne verir. İşte permutations fonksiyonunun bize verdiği 
dolaşılabilir nesneyi dolaştığımızda bizim birinci parametreyle 
verdiğimiz kümenin ikinci parametreyle belirtilen permütasyonlarını 
demetler halinde elde ederiz.Örneğin:
------------------------------------------------------------------------------------
"""
"""
import itertools

names = ['ali', 'veli', 'selami', 'ayşe', 'fatma']

for t in itertools.permutations(names, 2):
    print(t)

print()

for t in itertools.combinations(names, 3):
    print(t)
"""


# ---------------- bytes nesneleri ----------------
"""
# amaç -> en yalın bellek birimi olan byte'ı temsil eden bir tür oluşturmak
#  Byte kavramı [0, 255] arasında bir sayı belirtir, immutable'dır
# bytearray -> set-frozenset gibi, mutable'dır

b = b'alebron'
type(b) # <class 'bytes'>
b[0] #  97


a = [3, 5, 65, 32, 254]
c = bytes(a)
print(c)
"""  
"""
s = 'ağrı dağı'
b = bytes(s, 'utf-8')
print(b)

print()

s = 'ağrı dağı'
sd = s.encode('utf-8')  # decode() ->  encode()'nin tersi
                        # yani bytes'dan str türüne dönüstürür
print(sd)
"""

# ----------------------------------- Pythonda Nesne Yönelimi -------------------------------------
"""
# Sınıflar mutable türlerdir

class Sample:
    pass

s = Sample() # s -> instance

s.a = 10 # -> instance attribute, s'in a isimli bir instance attribute'unu oluşturuldu

print(s.a)          # 10
print(id(s))        # 1256763753232
print(id(s.a))      # 140717322703944

"""
#  ------------------ Metot(Method) ------------------
"""
-----------------------------------------------------------------------------
Sınıfların  içerisindeki fonksiyonlara "metot (method)" denilmektedir. 
Eğer bir fonksiyon sınıfların dışındaysa ona "fonksiyon (function)"
Python'da metotların en azından bir parametresi olur. Metotların ilk 
parametreleri özel bir anlama sahiptir. Programcılar genel olarak
metotların bu ilk parametrelerini "self" biçiminde isimlendirirler. 
Ancak bu ilk parametrenin "self" biçiminde isimlendirilmesi 
zorunlu değildir.
-----------------------------------------------------------------------------

class Sample:
   def foo(self):
       print('foo')

   def bar(self, a):
       print(f'bar: {a}')

   def tar(self, a, b):
       print(f'tar: {a}, {b}')

def zar():
    pass

-----------------------------------------------------------------------------
Bir metodun çağrılması için o metodun içinde bulunduğu sınıf türünden bir 
değişkenin olması gerekir. Metot çağırma işleminin genel biçimi şöyledir:

    <değişken_ismi>.<metot_ismi>([argüman listesi])
-----------------------------------------------------------------------------

s = Sample()

s.foo()
s.bar(10)
s.tar(10, 20)
-----------------------------------------------------------------------------
Metot bu biçimde çağrılırken birinci self parametresi için argüman girilmez. 
Metoda girilen argümanlar self parametresinden sonraki parametrelere ilişkindir.
-----------------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------------
Metotlar ilgili sınıf türünden bir değişkenle çağrıldığına göre o değişkenin 
atanacağı metotta bir self parametresinin bulunması gerekmektedir. Aşağıdaki 
örnekte self parametresi ile s aynı nesneyi gösteriyor durumdadır.
Dolayısıyla nesnenin a özniteliğine self parametresiyle de erişilebilmiştir:
-----------------------------------------------------------------------------
class Sam:
    def foo(self):
        print(self.a, self.b)       # 10
            
s = Sam()
s.a = 10
s.b = 11

s.foo()

----------------------------------------------------------------------------------
Yukarıdaki, işlemin tersini de yapabiliriz. Yani metodun içerisinde nesenin 
öznitelikleri yaratılabilir. Yaratılan bu öznitelikler daha sonra kullanılabilir:
----------------------------------------------------------------------------------       
class Sample:
    def foo(self):
        self.a = 10
        self.b = 20
           
s = Sample()
s.foo()

print(s.a, s.b)         # 10 20
""" 

# ----- __init__ metodu -------

"""
----------------------------------------------------------------------------------
Python'da sınıfların __init__ isimli özel bir metotları vardır. Bu metotlara 
"initializer" ya da bazen "constructor" da denilmektedir. __init__ metodu 
bir sınıf türünden nesne yaratıldığında otomatik olarak çağrılan bir metottur.
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
Burada Sample nesnesi Sample() ifadesi ile yaratılmak istendiğinde Python 
yorumlayıcısı önce nesneyi yaratır. Sonra yaratılan nesnenin adresini 
self parametresine geçirerek __init__ metodunu çağırır, ondan sonra s 
değişkenine atama yapılır. Yani önce __init__ metodu çağrılıp sonra nesnenin 
adresi s değişkenine atanmaktadır.

Aşağıdaki örnekte Sample sınıfı türünden her nesne yaratıldığında yorumlayıcı 
tarafından sınıfın __init__ metodu otomatik bir biçimde çağrılacaktır.
----------------------------------------------------------------------------------

class Sample:
    def __init__(self):
        print('__init__ called')
        
s = Sample()
print('Ok')
k = Sample()

"""

"""
----------------------------------------------------------------------------------
Yukarıda de belirtitğimiz gibi bir sınıf türünden nesne yaratıldığında önce 
nesne yaratılır. Sonra sınıfın __init__ metodu çağrılır. 
Ondan sonra nesnenin adresi değişkene atanır. Örneğin:
----------------------------------------------------------------------------------

s = Sample()
----------------------------------------------------------------------------------
Burada __init__ çağrıldıktan sonra s'e atama yapılacaktır. __init__ metodunun 
self parametresi henüz (yani yeni) yaratılmış olan nesneyi belirtmektedir. 
İşte programcı tipik olarak oluşturduğu nesnenin nesnenin özniteliklerini 
__init__ metodu  içerisinde yaratmaktadır. Böylece yaratılan her nesne aynı 
elemanlara yani özniteliklere sahip olur. Örneğin:
----------------------------------------------------------------------------------
class Sample:
    def __init__(self):
        self.a = 10
        self.b = 20
        
s = Sample()
print(s.a, s.b)

k = Sample()
print(k.a, k.b)

----------------------------------------------------------------------------------
Burada s ve k değişkenlerinin gösteridği yerdeki nesnelerin öznitelikleri 
__init__ tarafından yaratılmıştır.
----------------------------------------------------------------------------------
"""

"""
class Sample:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def disp(self):
        print(self.a, self.b)


s = Sample(10, 20)
k = Sample(30, 40)

s.disp()  # 10 20
k.disp()  # 30 40
----------------------------------------------------------------------------------
Tabii biz nesnenin örnek özniteliklerini başka bir metotta da yaratabiliriz.
__init__ metodunun diğer metotlardan tek farkı yorumlayıcı tarafından otomatik 
çağrılmasıdır. Aşağıdaki örnekte nesnenin a ve öznitelikleri __init__ metodunda 
değil foo metodunda yaratılmıştır.
----------------------------------------------------------------------------------

class Sample:
    def foo(self, a, b):
        self.a = a
        self.b = b

    def disp(self):
        print(self.a, self.b)


s = Sample()
k = Sample()

s.foo(10, 20)
k.foo(30, 40)

s.disp()
k.disp()
"""

"""
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def disp(self):
        print(f'{self.real}+{self.imag}i')
        
    def add(self, z):
        real = self.real + z.real
        imag = self.imag + z.imag
        
        result = Complex(real, imag)
        
        return result
    
    def sub(self, z):
        real = self.real - z.real
        imag = self.imag - z.imag
        
        result = Complex(real, imag)
        
        return result   
        
x = Complex(6, 5)
y = Complex(2, 3)

z = x.add(y)
z.disp()

z = x.sub(y)
z.disp()
"""
"""
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def disp(self):
        print(f'{self.real}', end='')
        if self.imag != 0:
            print(f' + {self.imag}i')
        else:
            print()


x = Complex(6, 5)
y = Complex(6)
z = Complex()

x.disp()  # 6+5i
y.disp()  # 6
z.disp()  # 0
"""
"""
----------------------------------------------------------------------------------
Sınıfların metotları alternatif biçimde sınıf ismi ile de çağrılabilmektedir. 
Ancak bu çağrı biçiminde self parametresini açıkça argüman olarak geçirmek 
gerekir. Örneğin:
----------------------------------------------------------------------------------
class Sample:
    def foo(self):
        print('foo')
        
    def bar(self, a):
        print(f'bar: {a}')
                    
s = Sample()

s.foo()
s.bar(10)
print("--------")
Sample.foo(s)
Sample.bar(s, 10)
----------------------------------------------------------------------------------
Burada örneğin s.foo() çağrısı ile Sample.foo(s) çağrısı tamamen eşdeğerdir. 
Ancak birinci çağrı yani s.foo() çağrısı tercih edilmelidir. 
----------------------------------------------------------------------------------
"""

"""
class Sample:
    print('one')

    def foo(self):
        pass

    print('two')

    def bar(self):
        pass
    
    print('three')
"""
"""
class Sammmple:
       pass

print(type(Sammmple))     # <class 'type'>

s = Sammmple()
print(type(s))          # <class '__main__.Sammmple'>
"""


"""
-------------------------------------------------------------------------------
NYPT'de sınıflar arasındaki ilişkiler dört başlıkta ele alınmaktadır:

    1) İçerme İlişkisi (Composition)
    2) Birleşme İlişkisi (Aggregation)
    3) Türetme İlişkisi (Inheritance)
    4) Çağrışım İlişkisi (Association)

Tabii iki sınıf arasında hiçbir ilişki de olmayabilir. Eğer ilişki olmamasını 
da bir ilişki biçimi olarak ele alırsak o zaman beşinci maddeyi 
"ilişki yok" biçiminde de oluşturabiliriz. 
-------------------------------------------------------------------------------
"""

#  ---------------- İçerme İlişkisi (Composition) ----------------
"""
-------------------------------------------------------------------------------
Örneğin "insan" ile "karaciğer" sınıfları arasında, "araba" ile "motor" sınıfları 
arasında bu biçimde içerme ilişkisi vardır. İki sınıf arasında içerme ilişkisi 
olması için aşağıdaki iki özelliğin ikisinin de sağlanması gerekir:

    1) İçeren nesneyle içerilen nesnenin ömürleri aynı olmalıdır. 
    2) İçerilen nesne tek bir nesne tarafından içerilmelidir. 
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Bu durumda örneğin "hastane" sınıfı ile "doktor" sınıfı arasında içerme ilişkisi 
yoktur. Çünkü bunların ömürleri aynı değildir. Ayrıca bir doktor aynı anda 
birden fazla hastanede de çalışabilmektedir. Ancak insan ile karaciğer arasında, 
arabayla motor arasında, "saat" ile "akrep" arasında, "dünya" ile "kıtalar" 
arasında, "cep telefonu" ile "işlemcisi" arasında içerme ilişkisi vardır. "Oda"
ile "duvar" arasında içerme ilişkisi yoktur. Her ne kadar oda ile duvar aynı 
ömre sahipse de duvar aynı zamanda yan odanın da duvarıdır
-------------------------------------------------------------------------------
"""
"""

-------------------------------------------------------------------------------
Python'da içerme ilişkisi içeren sınıfın __init__ metodunda içerilen nesnenin 
yaratılarak içeren sınıfın örnek özniteliğinde tutulması yoluyla sağlanabilir.
-------------------------------------------------------------------------------
class Araba:
    def __init__(self):
        self.motor = Motor()
                        
class Motor:
    pass

a = Araba()
-------------------------------------------------------------------------------
Burada Araba sınıfı türünden nesne yaratıldığında Araba sınıfının __init__ metodu 
çağrılacak ve Motor nesnesi de yaratılacaktır. Böylece araba nesnesi motor 
nesnesine sahip olmaktadır (has a ilişkisi). Henüz görmemiş olsak da 
"çöp toplayıcı (garvage collector)" mekanizma Araba nesnesini yok ettiğinde motor
nesnesi de yok olacaktır.
-------------------------------------------------------------------------------
"""

#  ---------------- Birleşme İlişkisi (Aggregation) ----------------
"""
----------------------------------------------------------------------------------
Birleşme ilişkisinde (aggregation) bir sınıf türünden nesne başka bir sınıf 
türünden nesneyi bünyesine katarak kullanmaktadır. Ancak kullanılan nesne tek 
bir nesne tarafından kullanılmak zorunda değildir. Kullanan nesneyle kullanılan
nesnenin ömürleri de aynı olmak zorunda değildir. İşte bu durumda bu nesnelerin 
sınıfları arasında "birleşme" ilişkisi vardır.Aslında çoğu zaman "içerme" 
ilişkisine benzeyen ancak içerme ilişkisi olmayan iişkiler "birleşme" ilişkisidir.
Örneğin "hastane" ile "doktor" sınıfları arasında, "bilgisayar" ile "fare" 
sınıfları arasında "oda" ile "duvar" sınıfları arasında içerme ilişkisi yoktur, 
birleşme ilişkisi vardır.
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Python'da birleşme ilişkisi kullanan sınıfta kullanılan nesneyi geçici olarak 
tutma yoluyla sağlanabilir. Yani birleşme ilişkisinde kullanılacak nesnenin
kullanan nesneye dahil edilmesi ve çıkartılması gibi işlemler söz konusu olmaktadır. 
----------------------------------------------------------------------------------

class Doctor:
        def __init__(self, name, specialty):
            self.name = name
            self.specialty = specialty

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        
    def remove_doctor(self, name):
        self.doctors.remove(name)
                
    def another_metods(self):
        print('self.doctors is using...')
            
hospital1 = Hospital('Yaşam')

doctor1 = Doctor('Ali Serçe', 'Kalp Damar')
hospital1.add_doctor(doctor1)

doctor2 = Doctor('Mehmet güneş', 'Kulak Burun Boğaz')
hospital1.add_doctor(doctor2)

hospital2 = Hospital('Gelecek')
hospital2.add_doctor(doctor1)

----------------------------------------------------------------------------------
Burada bir Hospital nesnesi birden fazla Doctor nesnesini kullanabildiği gibi
bir Doctor nesnesi de birden fazla Hospital nesnesi tarafından kullanılabilmektedir.
Hospital nesnesinin ve Doctor nesnelerinin ömürlerinin farklı olabildiğine 
dikkat ediniz. 
----------------------------------------------------------------------------------
"""


#  ---------------- Association İlişkisi (Çağrışım) -----------------
"""
----------------------------------------------------------------------------------
Sınıflararası ucuncu ilişki biçimine "çağrışım ilişkisi (association)" denilmektedir. 
Çağrışım ilişkisinde bir sınıf nesnesi başka bir nesneyi kullanır. Ancak bu 
kullanma yüzeyseldir. Bünyesine katarak bir kullanma değildir. Örneğin Taksi sınıfı 
Müşteri sınıfını kullanır. Ancak Taksi ile Şoför arasındaki ilişki birleşme 
ilişkisiyken Taksi ile Müşteri arasındaki ilişki çağrışım ilişkisidir. Çağrışım 
ilişkisi yüzeysel bir ilişkidir. Örneğin bir sınıf diğer sınıfı yalnızca bir 
metodunda kullanıyorsa,bünyesine katarak kullanmıyorsa burada bir çağrışım 
ilişkisinden bahsedilebilir. Örneğin Hastane sınıfı reklam yapılacağı zaman
Reklam Şirketi sınıfını kullanıyor olabilir.

Çağrışım ilişkisi UML sınıf diyagramlarında kullanan sınıftan kullanılan 
sınıfa çekilen ince bir ok ile temsil edilmektedir.
----------------------------------------------------------------------------------
"""

#  ---------------- Inheritance İlişkisi (Türetme ) -----------------
"""
----------------------------------------------------------------------------------
Sınıflar arasındaki diğer bir ilişki biçimi de "türetme" ilişkisidir. Türetme 
ilişkisine İngilizce  "inheritance" yani "kalıtım" da denilmektedir. Türetme 
mevcut bir sınıfa dokunmadan onu genişletme anlamına gelir. Burada asıl sınıfa 
"taban sınıf (base class)", genişletilmiş olan sınıfa da "türemiş sınıf (derived class)"
denilmektedir. Türetmede türemiş sınıf tamamen taban sınıf gibi de işlem görür 
ancak fazlalıkları da vardır. UML sınıf diyagramlarında türetme ilişkisi 
türemiş sınıftan taban sınıfa doğru çekilen içi boş bir okla gösterilmektedir.
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
Örneğin:

    A
    B

Burada B sınıfı A sınıfından türetilmiştir. Yani B sınıfı türünden bir nesne 
ile hem B sınıfının elemanlarını hem de A sınıfının elemanlarını kullanabiliriz. 

Türemiş sınıftan yeniden türetme yapılabilir. Böylece bir dizi türetme söz 
konusu olabilir. Örneğin:

    A
    B
    C
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Bir türetme şemasında yukarıya çıktıkça genelleşme, aşağıya indikçe özelleşme
olur. Yani yukarıdaki sınıflar diğer sınıflarda olan ortak özellikleri barındırır. 
NYPT'de türetme ilişkisine İngilizce "is a" ilişkisi de denilmektedir. Örneğin 
"işçi bir çalışandır". O zaman İşçi sınıfı Çalışan sınıfından türetilebilir. 
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
Bir sınıfın birden fazla sınıfa taban sınıflık yapması tamamen normal bir durumdur. 
Örneğin:
    
          A
    B           C

Burada A hem B'nin hem de C'nin taban sınıfı durumundadır. Ancak bir sınıfın 
birden fazla taban sınıfa sahip olması durumu özel bir durumdur. Buna NYPT'de 
"çoklu türetme (multiple inheritance)" denilmektedir. Doğada çoklu türetme az
olmasına karşın karşılaşılmaktadır. Örneğin:

    A       B
        C
----------------------------------------------------------------------------------


----------------------------------------------------------------------------------
İçerme ilişkisi, birleşme ilişkisi ve çağrışım ilişkisi şimdiye kadar görmüş 
olduğumuz bilgilerle oluşturulabilmektedir. Ancak türetme ilişkisi ayrı bir 
sentaks ile oluşturulmaktadır. Biz de şimdi Python'da türetme ilişkisinin 
oluşturulması ve kullanılması üzerinde duracağız.

Python'da türetme sentaksının genel biçimi şöyledir:

    
class <türemiş sınıf ismi>(<taban sınıf listesi>):
    pass

Örneğin:

class A:
    pass

class B(A):
    pass
----------------------------------------------------------------------------------
"""

"""
class A:
    def foo(self):
        print('A.foo')
    
    def bar(self):
        print('A.bar')
        
class B(A):
    def tar(self):
        print('B.tar')
        
b = B()

b.foo()
b.bar()
b.tar()

------------------------------------------------------------------------------------
Türetme ilişkisinde türemiş sınıf taban sınıfı kullanmaktadır. Taban sınıf 
türemiş sınıfı kullanmamaktadır. Aşağıdaki örnekte B ve C sınıflarının ortak 
elemanları A taban sınıfında toplanmış ve kod tekrarı bu sayede elimine edilmiştir.
------------------------------------------------------------------------------------

class A:
    def foo(self):
        print('foo')
    
    def bar(self):
        print('bar')

class B(A):
    def tar(self):
        print('tar')
        
class C(A):
    def zar(self):
        print('zar')
        
b = B()
b.foo()
b.bar()
b.tar()

c = C()
c.foo()
c.bar()
c.zar()
"""



"""
------------------------------------------------------------------------------------
Anımsanacağı gibi nesnelerin öznitelikleri tipik olarak __init__ metotlarında 
yaratılmaktadır. Türemiş sınıf türünden bir nesne yaratıldığında eğer türemiş 
sınıfın __init__ metodu yazılmışsa türemiş sınıfın __init__ metodu otomatik çağrılır.
Ancak türemiş sınıfın __init__ metodu yazılmamışsa bu durumda taban sınıfın
__init__ metodu çağrılmaktadır. 

Türemiş sınıfın __init__ metodunun türetmeyi yapan programcı tarafından yazılmış 
olduğunu varsayalım. Bu durumda türemiş sınıf türünden bir nesne yaratıldığında 
türemiş sınıfın __init__ metodu çağrılacaktır.Taban sınıfın __init__ metodu 
çağrılmayacaktır. Oysa taban sınıfın __init__ metodunun içerisinde taban sınıf 
gereken birtakım şeyler yapılmış olabilmektedir. Türemiş sınıf türünden nesne 
yaratıldığında türemiş sınıfın __init__ metodunun çağrılması ancak taban sınıfın
 __init__ netodunun çağrılmaması önemli sorunlara yol açabilmektedir. Örneğin:
------------------------------------------------------------------------------------

class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
    
class B(A):
    def __init__(self):
        self.y = 20
    
    def dispB(self):
        print(self.y)
            

a = A()
a.dispA()           # sorun yok! nesnenin a özniteliği yaratılmış durumda

b = B()
b.dispA()           # dikkat! nesnenin bir a örnek özniteliği yaratılmamış!
b.dispB()

------------------------------------------------------------------------------------
COZUMU:
------------------------------------------------------------------------------------

class A:
    def __init__(self):
        self.x = 10
        
    def dispA(self):
        print(self.x)
    
class B(A):
    def __init__(self):
        A.__init__(self)   # açıkça A'nın __init__ metodunun çağrıldığı anlaşılıyor
        self.y = 20
    
    def dispB(self):
        print(self.y)
 
           
a = A()
a.dispA()           

b = B()
b.dispA()           
b.dispB()

"""

"""
A
B
C
D

Burada D'nin taban sınıfları C, B ve A'dır. D'nin doğrudan taban sınıfı C'dir.
D'nin dolaylı taban sınıfları A ve B'dir.

"""

# dir() fonksiyonu
"""
------------------------------------------------------------------------------------
Built-in dir isimli fonksiyon bir sınıfın ya da bir nesnenin öznitekilklerini 
elde etmek için kullanılmaktadır. dir fonksiyonu parametre olarak bir sınıf 
ismini (yani type türünden bir değişkeni) ya da bir sınıf türünden değişkeni 
alabilmektedir. dir fonksiyonu o sınıf ismi ile ya da o sınıf türünden değişken 
ile kullanılabilecek bütün isimleri string'lerden oluşan bir liste biçiminde 
bize vermektedir. Python programcıları bir sınıfın elemanlarını hatırlamak 
istediklerinde bu fonksiyonu sıkça kullanmaktadır
------------------------------------------------------------------------------------
class Sample:
    x = 10

s = Sample()
s.y = 20
dir(Sample) # x var y yok -> dir fonksiyonu Sample ile kullanılabilecek oznitelikleri gösteriyor
dir(s) # x de var y de var -> dir fonksiyonu s ile kullanılabilecek oznitelikleri gösteriyor

"""


# ---------------- super() fonksiyonu -------------------------
"""
class A:
    def __init__(self):
        print('A.__init__')
        
class B(A):
    def __init__(self):
        A.__init__(self)
        print('B.__init__')
    
class C(A):
    def __init__(self):
        A.__init__(self)
        print('C.__init__')
    
class D(B, C) :
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
    
d = D()

Burada ekrana şunlar çıkacaktır:

A.__init__
B.__init__
A.__init__
C.__init__

------------------------------------------------------------------------------------
İşte bu tür baklava biçiminde yapılan türetmelerde tepedeki taban sınıfın 
__init__ metodunun iki kere çağrılmasını engellemek için super isimli bir 
fonksiyon bulundurulmuştur.
------------------------------------------------------------------------------------

class A:
    def foo(self):
        print('A.foo')

class B(A):
    def foo(self):
        print('B.foo')

class C(B):
    def foo(self):
        print('C.foo')
        
class D(C):
    def foo(self):
        print('D.foo')
        
d = D()

super(B, d).foo()           # A.foo çağrılır
super(C, d).foo()           # B.foo çağrılır  
super(D, d).foo()           # C.foo çağrılır

print(D.__mro__)

-> alttakinden farkı super fonksiyonunun __mro__ sırasına göre işlev yapması

A.foo(d)                    # A.foo çağrılır
B.foo(d)                    # B.foo çağrılır
C.foo(d)                    # C.foo çağrılır

"""
"""
class A:
    def __init__(self):
        super(A, self).__init__
        print('A.__init__')
    
class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')
        
class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')
        
class D(B, C):
    def __init__(self):
        super(D, self).__init__()
        print('D.__init__')
        
d = D()

------------------------------------------------------------------------------------
Aslında super fonksiyonun en önemli işlevi baklava şeklindeki çoklu türetme 
durumunda baklavanın tepesindeki taban sınıfın __init__ metodunun birden fazla
kez çağrılmasını engellemek içindir. Anımsanacağı gibi super(B, d).foo() gibi 
bir çağırmada foo metodunun aranması d değişkeninin ilişkin olduğu sınıfın MRO 
sırasında B sınıfından sonraki sınıftan başlatılmaktadır.
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
Biz bir sınıf yazarken bizden çoklu türetme yapılıp yapılmayacağını bilmediğimize 
göre taban sınıf ismi ile değil super fonksiyonu ile sıradaki sınıfın __init__ 
metodunu çağırmalıyız. İyi teknik __init__ metodu çağrılırken taban sınıf 
isminin değil super fonksiyonunun kullanılmasıdır.
------------------------------------------------------------------------------------
"""

"""
------------------------------------------------------------------------------------
Burada C'nin MRO sırası C, A, B olduğu için C ve A'nin __init__ metotları 
çağrılacaktır ancak B'ninki çağrılmayacaktır.Genellikle object sınıfından türetme
yapıldığında (default durum) programcılar super çağrısıyla __init__ metotlarını 
çağırmazlar. Bu durumda da çoklu türetmede sorunlar çıkabilir. Pekiyi çözüm nedir?
------------------------------------------------------------------------------------
class A:
    def __init__(self):
        print('A.__init__')

class B:
    def __init__(self):
        print('B.__init__')
        
class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')
        
c = C()

------------------------------------------------------------------------------------
Aslında bir sınıfı yazan kişi o sınıfın çoklu türetmede kullanılıp kullanılmayacağını 
belirleyip bunu dokümantasyonda belirtmelidir. Yani sınıfı yazan kişinin sınıfın 
çoklu türetmede kullanılıp kullanılmayacağını baştan öngörebilmesi gerekir.Eğer 
programcının sınıfı çoklu türetmeyi destekleyecekse sınıf object sınıfından 
türetilmiş olsa bile super çağrısıyla MRO sırasına göre sıradaki sınıfın __init__ 
metodunu çağırmalıdır. Eğer sınıfı çoklu türetmeyi desteklemiyorsa bu durumda 
böyle bir çağrı yapmasına gerek yoktur. Örneğin:
------------------------------------------------------------------------------------
class A:
    def __init__(self):
        super(A, self).__init__()
        print('A.__init__')

class B:
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')
        
class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')
           
c = C()
"""

# ---------------- kapsülleme (encapsulation) ------------------
"""
------------------------------------------------------------------------------------
NYPT'nin önemli bir prensibi "kapsülleme (encapsulation)" denilen prensiptir.
Kapsülleme bir kavramın bir sınıfla temsil edilmesi ve sınıfın dışarıyı 
ilgilendirmeyen, iç işleyişe ilişkin olan öğelerinin dış dünyadan gizlenmesi 
anlamına gelmektedir. Bu gizleme hem algısal bir açıklık sağlamakta hem de yanlış 
kullanımları engellemektedir. Aslında kapsülleme dış dünyada da sıklıkla 
karşılaştığımız bir olgudur. Örneğin bir otomobilin pek çok aksamı kaput içerisinde 
gizlenmiştir. Yalnızca kullanıcıyı ilgilendiren kısımları görünür hale 
getirilmiştir. Bir televizyon için de aynı durum söz konusudur. Televizyonu 
kullanabilmemiz için onun karmaşık yapısını bilmemize gerek yoktur.

C++, Java ve C# gibi dillerde kapsülleme için sınıfların "public", "private", 
"protected" gibi bölümleri vardır. Sınıfı yazan kişi birtakım elemanları private 
bölüme yerleştirire o öğelere dışarıdan erişilemez. Sınıfın veri elemanlarının 
(örnek dözniteliklerinin) dış dünyadan gizlenmesine ise "veri elemanlarının 
gizlenmesi (data hiding)" prensibi denilmektedir. Sınıfın veri elemanları iç 
işleyişe ilişkindir. Programcılar da C++, Java ve C# gibi dillerde veri 
elemanlarını sınıfın private bölümine yerleştirerek dış dünyadan gizlerler. 

Ancak Python'da bu anlamda bir gizleme mekanizması yoktur. Yani C++, Java ve C# 
gibi dillerdeki "public", "protected", private" gibi erişim belirten kavramlar 
Python'da bulunmamaktadır. 
------------------------------------------------------------------------------------
"""

#  _ (underscore) 

"""
------------------------------------------------------------------------------------
Python'da her ne kadar C++, Java ve C# gibi dillerde bulunan "public", "private",
"protcted" bölümler olmasa da bir sınıfın bir metodunun ya da nesnenin bir 
özniteliğinin dış dünyadan gizlenmesi isimsel biçimde sağlanmaya çalışılmıştır. 
Öyle ki eğer bir sınıfın ya da nesnenin özniteliğinin ismi '_' ile başlatılırsa 
bu durum diğer dillerdeki private etkisi yaratmaktadır. Ancak bu etki yalnızca 
bir tavsiye oluşturmaktadır. Başı '_' ile başlayan isimler için yorumlayıcı tarafından 
erişimde bir denetleme yapılmamaktadır. Başka bir deyişle biz Python'da sınıfın 
ya da nesnenin özniteliğinin '_' ile başladığını gördüğümüzde "bu özniteliklere 
dışarıdan (sınıfın daşından) erişilmesinin istenmediği" anlamını çıkartmalıyız. 
Ancak yine de biz istersek bu özniteliklere dışarıdan erişebiliriz. Burada bir 
zorlayıcılığın olmadığna yalnızca yazım biçimiyle sınıf kullananlara bir 
tavsiyede bulunulduğuna dikkat ediniz. Örneğin:
------------------------------------------------------------------------------------

class Sample:
    def do_someting_important(self):
        # ....
        self._foo()
        # ....
        self._bar()
        # ....
        self._tar()
        #....
        
    def _foo(self):
        pass
    
    def _bar(self):
        pass
    
    def _tar(self):
        pass
    
s = Sample()

s.do_someting_important()

Burada sınıfın _foo, _bar ve _tar metotlarının dışarıdan çağrılması istenmemektedir.
Bu metotlar yalnızca sınıf içerisindeki diğer metotlardan çağrılmaktadır. Tabiki 
biz istersek gerçekten yine de onları dışarıdan kullanabiliriz. Bunun için yorumlayıcı 
tarafından zorlayıcı bir denetim uygulanmamaktadır.
"""

#  __ (2 underscore) 

"""
------------------------------------------------------------------------------------
Sınıfın ve nesnenin özniteliklerinin dış dünyadan gizlenmesi için diğer bir yöntem 
de isimlerin başına '__' (iki alt tire)getirmektir. Bir isim iki alt tire ile 
başlanarak isimlendirilmişse bu durum bu ismin "dışarıdan kullanımının daha katı 
bir biçimde istenmediği" anlamına gelmektedir. İki alt tire ile verilen isimlere 
gerçekten dışarıdan erişilemez. Ancak _sınıfismi__ öneki ile erişilebilir. Yani 
başka bir deyişle Sample sınıfının  __xxx elemanına biz s.__xxx gibi bir ifadeyle 
erişemeyiz. Ancak s._Sample__xxx ismiyle erişebiliriz. Bunun amacı kişilerin 
ilgili özniteliğe yanlışlıkla erişmelerinin engellenmesidir. Mutlak anlamda 
erişmelerinin engellenmesi değildir. Tabii başı iki alt tire ile başlayan isimlere 
sınıf içerisinden yine iki alt tire ile erişebiliriz. 
------------------------------------------------------------------------------------

class Sample:
    def do_someting_important(self):
        # ....
        self.__foo()
        # ....
        self.__bar()
        # ....
        self.__tar()
        #....
        
    def __foo(self):
        pass
    
    def __bar(self):
        pass
    
    def __tar(self):
        pass
    
s = Sample()
"""


# ---------------- çokbiçimlilik (polymorphism) ------------------ 
"""
Pek çok teorisyene göre bir dilin "nesne yönelimli" olması için dilin şu üç 
özelliği destekliyor olması gerekmektedir:

   - Sınıf kavramı
   - Türetme kavramı
   - Çokbiçimlilik (polymophism)

Eğer bir dilde sınıflar olduğu halde çokbiçimlilik yoksa böyle dillere "nesne 
tabanlı (object based)" diller denilmektedir. Başka bir deyişle dilin nesne 
yönelimli olabilmesi için "çokbiçimli mekanizmaya" sahip olması gerekmektedir. 
C++, Java, C# gibi dillerde çokbiçimli mekanizma bulunmaktadır. 
Dolayısıyla bu diller "nesne yönelimli" dillerdir. 

------------------------------------------------------------------------------------
NYPT'de bir eylem temel işlevi aynı olmak üzere sınıflar arasında farklılıklar 
gösteriyorsa bu eyleme "çokbiçimli" eylem denilmektedir. Örneğin A, B, C, D, E
sınıflarının disp isimli metotları olsun. Bu metotlar kendi sınıflarının birtakım 
elemanlarını kendilerine özgü biçimde ekrana yazdırıyor olsun. Burada disp metodu 
"çokbiçimli" bir metottur. Çünkü çeşitli sınıflarda bu metot vardır. Temel işlevi
sınıf hakkında bilgileri ekrana yazdırmaktır. Ancak her sınıfın disp metodu kendine 
özgüdür ve temel işlevi aynı olmasına karşın birbirlerinden farklıdır.

Örneğin bir personel takip programında iş yerinde çalışan kişilerin görevlerine
göre Worker, Manager, Executive, SalesPerson gibi farklı sınıflarla temsil 
edildiğini düşünelim. Bu sınıfların hepsinde kişilerin maaşlarını hesaplayan 
calculate_salary isimli bir metot olsun. Buradaki maaş hesaplama eylemi 
çokbiçimlidir. Bu sınıfların hepsinde vardır ama her sınıfın maaş hesabı kendine 
özgü bir biçimde yapılmaktadır. Çokbiçimli metotlar farklı sınıflarda aynı isimle 
bulunurlar. Bunların yaptıkları işler ana hatlarıyla aynıdır ancak o sınıfa özgü 
farklılıklar içermektedi
------------------------------------------------------------------------------------
"""

# ---------------- __str__ ----------------
"""
------------------------------------------------------------------------------------
Bir sınıf türünden nesneyi str türüne dönüştürebiliriz. Böyle bir dönüştürme için 
ilgili sınıfın __str__ isimli bir metodunun bulunuyor olması gerekir. s bir sınıf 
türünden değişken olmak üzere str(s) işlemi tamamen s.__str__() ile aynı anlamdadır.
Programcı sınıfın __str__ metodunu bir str nesnesiyle geri döndürmelidir. 

Aslında print fonksiyonu yalnızca string'leri bastırmaktadır. Eğer print 
fonksiyonuna girdiğimiz argüman string değilse print fonksiyonu onu str türüne 
dönüştürüp yazıyı ekrana basmaktadır. s string türünden olmayan bir türden olsun.
 Bu durumda:

 print(s)

ile 

print(str(s))

ya da 

print(s.__str__())

tamamen aynı anlamdadır. Örneğin:
------------------------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
pt = Point(3, 2)

print(pt)           
print(str(pt))          
print(pt.__str__())

------------------------------------------------------------------------------------
Burada biz kendi sınıf nesnemizi print fonksiyonuyla yazdırmak istediğimizde 
aslında print fonksiyonu onu str türüne dönüştürüp yazdırmaktadır. str türüne 
dönüştürme sırasında sınıfımızın __str__ metodu çağrılmaktadır. 
------------------------------------------------------------------------------------
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f'{self.day:02d}/{self.month:02d}/{self.year:04d}'
    
d = Date(4, 10, 2022)
print(d)

k = Date(11, 3, 2008)
print(k)

"""


# ---------------- __repr__ ----------------
"""
------------------------------------------------------------------------------------
__str__ metodunun __repr__ isminde bir benzeri de vardır. __repr__ metodu da 
tıpkı __str__ netodunda olduğu gibi bir string ile geri dönmelidir. Pekiyi iki 
metot arasında ne farklılık vardır? İşte __str__ metodu "daha çok kullanıcıya 
yönelik", __repr__ metodu ise "daha çok programcıya yönelik" bir yazı verme 
iddiasındadır. Tabii bu iki metodun veridiği yazılar aynı da olabilir. Örneğin
Python'ın komut satırında, Spyder'ın komut satırında (IPython) bir değişkeni 
yazıp ENTER tuşuna bastığımızda bu komut satırı programları değişken ile __repr__
metodunu çağırıp buradan elde edilen yazıyı bastırmaktadır. Örneğin:
------------------------------------------------------------------------------------
class Sample:
    def __str__(self):
        return '__str__'
       
    def __repr__(self):
        return '__repr__'
    
s = Sample()
s           # __repr__
print(s)    # __str__


 Aslında programcının bu iki metodu ayrı ayrı yazması da gerekmemektedir. Çünkü:

1) Eğer sınıfın __repr__ metodu varsa fakat __str__ metodu yoksa str türüne 
dönüştürmede __repr__ metodu kullanılmaktadır. Aynı zamanda  komut satırında 
değişken ismi yazılıp ENTER tuşuna basıldığında da __repr__ metodu kullanılılır. 
Yani biz sınıf için yalnızca __repr__ metodunu yazarsak hem str türüne 
dönüştürmelerde hem de komut satırında değişken ismini yazıp ENTER tuşuna 
basıldığında bu metot çağrılacaktır.

2) Sınıfta hem __str__ hem de __repr__ metodu varsa bu durumda str türüne 
dönüştürmede __str__ metodu, komut satırında değişken ismi yazılıp ENTER tuşuna 
basıldığında __repr__ metodu çağrılmaktadır. 

3) Sınıfta yalnızca __str__ metodu varsa str türüne dönüştürmede __str__ metodu 
çağrılır. Komut satırında değişken ismi yazılıp ENTER tuşuna basıldığında 
object sınıfının __repr__ metodu çağrılır. 

"""































