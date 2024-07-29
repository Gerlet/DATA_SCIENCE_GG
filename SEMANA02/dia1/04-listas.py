dias = ["lunes","martes","miercoles"]
print(dias[1])
#agregar un valor a la lista
dias.append("jueves")
dias.append("viernes")
print(dias)
#eliminar valor de la lista
dias.pop(0)
print(dias)
print(dias[1:3])
dias[0] = "domingo"
dias[1] = "lunes"
dias[2] = "martes"
dias[3] = "miercoles"
print(dias)

#recorrer una lista
for contador in range(len(dias)):
    print(dias[contador])

for dia in dias:
    print(dia)