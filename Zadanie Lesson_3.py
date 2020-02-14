from pip._vendor.progress import counter

a = open('text.txt', 'r', encoding='UTF-8')
text = a.read()
#1
b = text.replace('.','').replace(',','').replace('-',' ').replace('«','').replace('»','').replace('!','').replace('?','').replace('—','').replace(';','').replace(':','').replace('(','').replace(')','')
print(b)
#2
c = list(b.split())
print(c)
#3
d = list(map(lambda x: x.lower(), c))
print(d)
#4
e = {}
for i in range (len(d)):
    e[d[i]] = d.count(d[i])
print(e)
#5
f=list(e.items())
f.sort(key = lambda i: i[1], reverse=True)
print(f[0:5])
f = set (c)
print(len(f))
#6
import pymorphy2
j = pymorphy2.MorphAnalyzer()
g = str()
for word in d:
    word = j.parse(word)[0]
    g += word.normal_form + " "
d = list(g.split())
print(d)
