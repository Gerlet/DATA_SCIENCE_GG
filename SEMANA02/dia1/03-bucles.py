tabla = int(input("INGRESE LA TABLA A MULTIPLICAR : "))

for contador in range(1,13,1):
    print(f"{tabla} x {contador} = {tabla * contador}")

contador = 1
while(contador <= 12):
    print(f"{tabla} x {contador} = {tabla * contador}")
    contador += 1
