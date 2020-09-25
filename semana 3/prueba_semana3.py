nombre = input("Enter file name: ")
documento = open(nombre)
lista=list()
for linea in documento:
    linea=linea.rstrip()
    linea=linea.split()
    for lineas in linea:
        if lineas not in lista:
            lista.append(lineas)
lista.sort()
print(lista)