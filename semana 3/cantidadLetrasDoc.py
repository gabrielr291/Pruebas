documento=open('test.txt')
for linea in documento:
    linea=linea.rstrip()
    if not linea.startswith('De ') : continue
    palabras=linea.split()
    email= palabras[1]
    piezas=email.split('@')
    print(piezas[1])