import re
x='mis 2 numeros favoritos son el 19 y el 42'
y=re.findall('[0-9]+',x)
print(y)#devuelve una lista de los numeros que le pedi