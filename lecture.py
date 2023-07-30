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
    if cmd =='':
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
#1- Bir karşılaştıma sonucunda elde edilen değerin bir değişkene atandığı durumlarda. Örneğin:
result = 100 if a % 2 == 0 else 200

#2- Fonksiyon ya da metot çağrımlarında argüman olarak koşul operatörü bazen yazımı kısaltmak için kullanılabilmektedir. Örneğin:
# val = int(input('Bir sayı giriniz:'))
# print('çift' if val % 2 == 0 else 'tek')

#3- return ifadelerinde de koşul operatörü bazı durumlarda tercih edilmektedir. Örneğin:
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

#  Parametredeki "*" gerçek bir parametre değildir. Yani asagidaki foo fonksiyonunun 4 parametresi vardir
def foo(a, b, *, c, d=10):
    pass
# '*'ın sagindaki tüm parametreler cagrim sirasinda isimli argumanlarla cagrilmak zorundadir.



def foo(a, b, /, c = 100, d = 200):
        pass # Fonksiyonun parametre listesinde bir parametre yalnızca '/' biciminde girilmişse
# bu durum "onun solundaki tum parametreler argumanlarin pozisyonel olarak girilmesi gerektigi" anlamina gelmektedir.














