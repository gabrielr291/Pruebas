import re
x='From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('\S+@\S+',x)
print(y)#para conseguir un correo electronico debemos hacer lo sgte

y=re.findall ('^From (\S+@\S+)',x)
print(y)