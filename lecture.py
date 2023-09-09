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

# **'lı argumanlar bir sozluk nesnesi olmak zorundadır. Bu argumanlara iliskin sozluk nesnelerinin anahtarlarının str turunden olmasi gerekir.
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

# "forwarding" bir bir fonksiyonun aldığı parametreleri baska bir fonksiyona argüman olarak iletmesi durumuna denilmektedir. 
# Yukarıdaki örnekte myrint fonksiyonu kendisi hangi argümanlarla çağrılmışsa print fonksiyonunu da o argümanlarla çağırmıştır. 
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
# biz yazdığımız programdaki fonksiyonların ve değişkenlerin import edilerek kullanılmasını istiyorsak
# ve aynı zamanda da onu bağımsız bir program gibi de çalıştırmak istiyorsak kullanilir


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

# ----------- map Fonksionu -----------

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

# Liste içlemleri -> [<ifade> for <değişken> in <dolaşılabilir nesne> [if koşul] ]
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




# Küme içlemleri -> 

# Sözlük içlemleri -> 







































