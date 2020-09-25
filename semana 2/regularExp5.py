import re
data='From gabriel.omar.r29@gmail.com Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
sppos=data.find(' ',atpos)
print(sppos)
host=data[atpos+1: sppos]
print(host)#este te entrega el dominio del correo electonico

words=data.split()
email=words[1]
pieces=email.split('@')
print(pieces[1])#lo mismo que el codigo anterior pero mas elegante y corto(lo buysca entre los caracteres que no sean espacios)
#y no quiero el parentesis

import re
y=re.findall('@([^ ]*)',data)
print(y)#lo mismo que el anterior pero con la libreria regular expression

y=re.findall('^From .*@([^ ]*)',data)
print(y)#lo mismo que el anterior pero con la libreria regular expression