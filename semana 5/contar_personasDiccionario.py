contar=dict()
nombres=['csev','cwen','zquian','cwen']
for nombre in nombres:
    if nombre not in contar:
        contar[nombre]=1
    else:
        contar[nombre]=contar[nombre]+1
print(contar)