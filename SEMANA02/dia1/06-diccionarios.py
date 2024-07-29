capitales = {
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Colombia':'Bogota'
}

pais = input("Ingrese el pais : ")
if pais in capitales:
    capital = capitales[pais]
    print(f"La capital de {pais} es {capital}")
    eliminar_capital = input('¿desea eliminar la capital(si,no)?')
    if eliminar_capital == 'si':
        capitales.pop(pais)
        print(capitales)
else:
    print(f'no se encontro la capital de {pais}')
    nueva_capital = input(f'Ingrese la capital de {pais} : ')
    capitales.update({pais:nueva_capital})
    print(capitales)
