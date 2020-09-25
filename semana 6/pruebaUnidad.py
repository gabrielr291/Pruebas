name = input("Ingrese Nombre de archivo:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for linea in handle:
    if not linea.startswith("From "):
        continue
    else:
        linea=linea.split()
        linea=linea[5]
        linea=linea[0:2]
        d[linea]=d.get(linea,0)+1
lista=list()
for val,count in d.items():
    lista.append((val,count))
lista.sort()
for val,count in lista:
    print(val,count)