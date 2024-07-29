def suma(n1,n2):
    resultado = n1 + n2
    return resultado


r1 = suma(3,4)
r2 = suma(r1,8)
print(r2)

#parametros ars y kwags
def sumainfinito(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

r3 = sumainfinito(3,4,5,10,20)
print(r3)

def calculadora(**kwargs):
    ope = kwargs.get('ope')
    n1 = kwargs.get('n1')
    n2 = kwargs.get('n2')

    if(ope == "suma"):
        resultado = n1 + n2
    elif(ope == "resta"):
        resultado = n1 - n2
    else:
        resultado = "operacion incorrecta"

    return resultado

r4 = calculadora(n1=5,n2=2,ope='suma')
print(r4)