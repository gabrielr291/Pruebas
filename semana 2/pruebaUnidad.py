import re
documento=open('regex_sum_805351.txt')
suma=0
for linea in documento:
    numeros=re.findall('[0-9]+',linea)
    for numero in numeros:
        suma=suma+int(numero)
print(suma)