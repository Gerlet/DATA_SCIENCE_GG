"""
ingresar una lista de 5 numeros y retornar el numero mayor de la lista
Ejemplo:
ingrese nro 1: 10
ingrese nro 2: 13
ingrese nro 3: 15
ingrese nro 4: 1
ingrese nro 5: 5

el nro mayor es 15

numeros = []
for contador in range(1,6):
    nuevo_numero = int(input(f'Ingrese nro {contador} :'))
    numeros.append(nuevo_numero)
"""
numeros = [10, 13, 15, 15, 5]
print(numeros)
numero_mayor = numeros[0]

for numero in numeros:
    if(numero > numero_mayor):
        numero_mayor = numero

print(f'El nro mayor es {numero_mayor}')
print(f'El nro mayor es {max(numeros)}')
print(f'El nro menor es {min(numeros)}')

numeros.sort(reverse=True)
print(numeros[0])
print(numeros[1])

