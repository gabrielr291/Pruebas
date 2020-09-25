import re
x='From: Using the : character'
y=re.findall('^F.+:',x)
print(y)#nos devuelve todo el string de x aunque solo queremos el FROM:
y=re.findall('^F.+?:',x)
print(y)#añadiendo el ? nos cortara hasta la primera parte que es lo que queremos

