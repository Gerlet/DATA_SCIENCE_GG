capitales = {
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Colombia':'Bogota'
}

#recorrido por claves
for clave in capitales.keys():
    print(clave)

print('*'*50)
#recorrido por valores
for valor in capitales.values():
    print(valor)

print('*'*50)
#recorrido por clave valor
for clave,valor in capitales.items():
    print(f'la capital de {clave} es {valor}')

#DICCIONARY COMPREHENSION
paises = {valor:clave for clave,valor in capitales.items()}
print(paises)