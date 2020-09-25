import re
x='recibimos un total de $10.00 por las galletitas.'
y=re.findall('\$[0-9.]+',x)
print(y)#obtenemos la ganancia de una venta que esta en un texto
