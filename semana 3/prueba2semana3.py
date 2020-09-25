fileName = input("Enter file name: ")
documento = open(fileName)
contador = 0
for linea in documento:
    if not linea.startswith('From'):
        continue
    if linea.startswith('From:'):
        continue
    else:
        linea = linea.split()
        linea = linea[1]
        print(linea)
    contador += 1
print("There were",contador,"lines in the file with From as the first word")