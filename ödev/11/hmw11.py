# Solution 1
with open('teste.txt', 'w+', encoding='utf-8') as f:
    f.write("LeBron James(goat)\nGabe Vincent(Heat culture and injured)\nAustin Reeves(I'm him)\nRui Hachimura(Japanese)\nAnthony Davis(Defensive player of the year)")
    f.seek(0)
    s= f.read()
    print(s)
print()
def mygrep(text):
    res= s.split('\n')
    found= [index for index, item in enumerate(res) if text in item]
    if found:
        for i in range(len(found)):
            print(f"<{found[i]}>: {res[found[i]]}")

mygrep('him')



