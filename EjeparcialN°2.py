try:
    numero_ingresado = int(input("Ingresa un número entero positivo: "))
    if numero_ingresado <= 0:
        print("Por favor, ingresa un número positivo.")
    else:
        for i in range(1, 11):
            numero_multiplicado = numero_ingresado * i
            print(f"{numero_ingresado} * {i} = {numero_multiplicado}")
except ValueError:
    print("Ingresa un número válido.")