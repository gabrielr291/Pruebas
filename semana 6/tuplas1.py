x=('glenn','sally','joseph')
print(x[2])
y=(1,9,2)
print(y)
print(max(y))
for iter in y:
    print(iter)#recorremos toda la tupla e imprimimos

(x,y)=(4,'Fred')#podemos asignar 2 variables a tuplas
print(y)
(a,b)=(99,98)
print(a)
d=dict()
d['csev']=2
d['cwen']=4
for(k,v) in d.items():
    print(k,v)

tups=d.items()
print(tups)#lista de tuplas
#construimos variables de 2 iteraciones con k y v

(0,1,2)<(5,1,2)
(0,1,200000)<(0,3,4)
('Jones','Sally')<('Jones','Sam')
('Jones','Sally')>('Adams','Sam')

e={'a':10,'b':1,'c':22}
print(e.items())
orden=sorted(e.items())
print(orden)

t=sorted(e.items())
for k,v in sorted(e.items()):#ordenada por claves
    print(k,v)

tmp=list()
for k,v in e.items():
    tmp.append((v,k))
print(tmp)
tmp=sorted(tmp, reverse=True)
print(tmp)#recorremos los valores y claves y los imprimimos
#desde el mayor al menor

fhand=open('romeo.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for key, val in counts.items():
    newtup=(val,key)
    lst.append(newtup)
lst=sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)

#buscamos en vez de clave valor, valor clave
#y se ordenara desde el mayor al menor

print(sorted([(v,k)for k,v in e.items()]))

#para mas lee LIST COMPREHENSION