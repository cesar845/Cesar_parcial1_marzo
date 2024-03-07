celsius_F = 9/5
fahrenheit_C = 5/9
constante = 32

while True:
    print("\nMenú de opciones:")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    print("3. Finalizar")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == '1':
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        fahrenheit = celsius * celsius_F + constante
        print('la temperatura en grados Fahrenheit es: ', fahrenheit)
    elif opcion == '2':
        fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - constante) * fahrenheit_C
        print('La temperatura en grados Celsius es:', celsius)
    elif opcion == '3':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")