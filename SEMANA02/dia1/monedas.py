#CONVERTIR DE SOLES A DOLARES
#CONVERTIR DE DOLARES A SOLES
#ENTRADAS
TIPO_CAMBIO_COMPRA = 3.834
TIPO_CAMBIO_VENTA =  3.851
opcion = 0
while(opcion != 1 and opcion != 2):
    print(" CONVERTIDOR DE MONEDAS 1.0")
    print("""
        [1] CONVERTIR SOLES A DOLARES
        [2] CONVERTIR DOLARES A SOLES  
        """)
    opcion = int(input("ELIJA UNA OPCION :"))
    if(opcion == 1):
        monto_origen = float(input("INGRESE EL MONTO EN SOLES : "))
        #PROCESO
        monto_destino =  monto_origen / TIPO_CAMBIO_VENTA
        #SALIDAS
        print(f"EL MONTO EN DOLARES ES {monto_destino}")
    elif(opcion == 2):
        monto_origen = float(input("INGRESE EL MONTO EN DOLARES : "))
        #PROCESO
        monto_destino =  monto_origen * TIPO_CAMBIO_COMPRA
        #SALIDAS
        print(f"EL MONTO EN SOLES ES {monto_destino}")
    else:
        print("OPCIÓN NO VALIDA")