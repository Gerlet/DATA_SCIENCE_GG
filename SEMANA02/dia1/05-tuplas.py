dias = ("lunes","martes","miercoles","jueves")
print(dias)
dias = list(dias)
print(type(dias))
dias.append("vienes")
dias = tuple(dias)
print(type(dias))

for dia in dias:
    print(dia)