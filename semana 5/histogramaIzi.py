contar=dict()
nombres=['csev','cwen','csev','zqian','cwan']
for nombre in nombres:
    contar[nombre]=contar.get(nombre,0)+1
print(contar)