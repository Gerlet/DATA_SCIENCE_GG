def asteriscos(func):
    def envoltura():
        print('*'*20)
        func()
        print('*'*20)
    return envoltura

@asteriscos
def saludo():
    print("hola mundo")

#saludo = asteriscos(saludo)
saludo()