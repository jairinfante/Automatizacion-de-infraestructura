import math

def suma_numeros():
    n = int(input("Ingrese la cantidad de números que desea sumar: "))
    suma = 0
    for _ in range(n):
        numero = int(input("Ingrese un número: "))
        suma += numero
    print("La suma de los números es:", suma)

def producto_numeros():
    n = int(input("Ingrese la cantidad de números que desea multiplicar: "))
    producto = 1
    for _ in range(n):
        numero = float(input("Ingrese un número: "))
        producto *= numero
    print("El producto de los números es:", producto)

def division_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("La división es:", resultado)
    else:
        print("Error: No se puede dividir por cero.")

def factorial_numero():
    n = int(input("Ingrese un número para calcular su factorial: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("El factorial de", n, "es:", factorial)

def tablas_multiplicar():
    num = int(input("Ingrese el número para mostrar su tabla de multiplicar (1 al 10): "))
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

def cuadrado_cubo_numero():
    num = float(input("Ingrese un número para calcular su cuadrado y cubo: "))
    cuadrado = num ** 2
    cubo = num ** 3
    print(f"El cuadrado de {num} es: {cuadrado}")
    print(f"El cubo de {num} es: {cubo}")

def promedio_numeros():
    numeros = []
    while True:
        numero = float(input("Ingrese un número (-1 para detener): "))
        if numero == -1:
            break
        numeros.append(numero)
    if numeros:
        promedio = sum(numeros) / len(numeros)
        print("El promedio es:", promedio)
    else:
        print("No se ingresaron números.")

def maximo_minimo_numeros():
    n = int(input("Ingrese la cantidad de números que desea ingresar: "))
    numeros = []
    for _ in range(n):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)
    if numeros:
        maximo = max(numeros)
        minimo = min(numeros)
        print("El valor máximo es:", maximo)
        print("El valor mínimo es:", minimo)
        print("Total de valores ingresados:", len(numeros))
    else:
        print("No se ingresaron números.")



while True:
    print("\nMenú:")
    print("1. Suma de 'n' números.")
    print("2. Producto entre 'n' números.")
    print("3. División entre 2 números.")
    print("4. Calcular el factorial (n!).")
    print("5. Mostrar tabla de multiplicar.")
    print("6. Calcular cuadrado y cubo de un número.")
    print("7. Calcular promedio de una serie de números.")
    print("8. Encontrar valores máximo y mínimo.")
    print("0. Salir del programa.")

    try:
        opcion = int(input("Ingrese el número de la opción que desea ejecutar: "))
    except ValueError:
        print("Por favor, ingrese un número del menú.")
        continue

    if opcion == 1:
        suma_numeros()
    elif opcion == 2:
        producto_numeros()
    elif opcion == 3:
        division_numeros()
    elif opcion == 4:
        factorial_numero()
    elif opcion == 5:
        tablas_multiplicar()
    elif opcion == 6:
        cuadrado_cubo_numero()
    elif opcion == 7:
        promedio_numeros()
    elif opcion == 8:
        maximo_minimo_numeros()
    elif opcion == 0:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del menú.")
        