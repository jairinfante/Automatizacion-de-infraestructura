print("(1) CONVERSION DE GRADOS DE TEMPERATURA")
print("(2) HORAS DE TRABAJO DE UN EMPLEADO")
print("(3) COBRO DEL VALOR DE IVA DE UN PRODUCTO COMPRADO")
print("(4) PRESENTACION DE TEXTO EN PANTALLA")
print("(5) PRESENTACION DE CARACTERES EN PANTALLA")
print("(6) PRESENTACION DE VALORES EN PANTALLA")
print("(7) PRESENTACION DE FORMATO DEM TIPOS DE DATOS")
print("(8) TRABAJANDO CON NUMEROS ENTEROS Y ROLES")
print("(9) DEFINIENDO EL TIPO DE DATO")
print("(10) UTILIZANDO TIPOS DE DATOS PARA LA RESOLUCION DE UN EJERCICO")
print("(11) UTILIZANDO TIPOS DE DATOS PARA GEOMETRIA")
print("(12) UTILIZANDO LA LIBRERIA MATH")
print("(13) UTILIZANDO LA LIBRERIA MATH X2")
print("(14) ENCUENTRA EL CUADRADO DE UN NUMERO")

catalogo = input("Escoge el ejercicio de tu preferencia ")

match catalogo:
    case "1": 
        F = input ("Ingresar un valor")
        C = round((int(F)-32)/1.8)
        print("C: ", C) 
    case "2":
        CHT = input("Ingrese horas de trabajo: ")
        print("Costos hora: ", end = " ")
        PPH = input()
        sueldo = int(CHT) * int(PPH)
        print("Sueldo es: ",sueldo)
    case "3":
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = 1 
        subtotal = cantidad * precio
        IVA = subtotal * 0.12
        total =  subtotal + IVA
        print("Subtotal: ",subtotal)
        print("IVA: ",IVA)
        print("total: ",total)
    case "4":
        print('Victor Infante')
        print("Victor Infante")
        print("\tVictor\tInfante")
        print("\tVictor Infante\t",end = " ")
        print("\nVictor", "Infante", sep= "", end= "")
        print("\nVictor", "Infante",end="")
    case "5":
        print("***************")
        print("*             *")
        print("*             *")
        print("***************")
    case "6":
        nombre = "Mi amigo Sebastian"
        numero1 = 25
        logico1 = False;
        lista = [21,22,23,24,25]
        print(nombre)
        print(numero1)
        print(logico1)
        print(lista[2])
    case "7":
        t = "palabra,"
        n = 23
        print("Una palabra,",t,"ahora un numero", n)
        m = "Una palabra, {} ahora un numero '{}'".format(t,n)
        print(m)
        print(3 * t + t)
    case "8":
        x = 7 / 5
        y = 17 / 3
        z = 17 // 3
        w = 17 % 3
        v = 7 ** 2
        u = 7^2
        print(x)
        print(y)
        print(z)
        print(w)
        print(v)
        print(u)
    case "9":
        numero = int()
        numero = 4
        sueldo = float()
        sueldo = 2600
        print(numero," ",sueldo)
    case "10":
        import math
        r = 1
        p = 2 * r * math.pi
        a = math.pi * r * r
        print("Perimetro: ", p)
        print("Area: ", a)
    case "11":
        lado = 3 
        n = 5
        ap = 2
        p = lado * n
        A = p * ap
        print("Perimetro: ",p)
        print("Area: ", A)
    case "12":
        import math
        a = 3
        b = 4
        c1 = math.sqrt(a*a + b*b)
        c2 = math.hypot(a,b)
        print("Hipotenusa: ",c1)
        print("Hipotenusa: ",c2)
    case "13":
        import math
        a = 3
        b = 4
        c = 5
        angulo = 53.13010235415598
        h = a / math.cos(angulo * math.pi/180)
        print("Hipotenusa: ",h)
        identidad = 3 / 5
        te = math.acos(identidad)
        print("Angulo: ",te * 180/math.pi)
        # ////////////
    case "14":
        import math
        Num = int(input("Escribe un numero"))
        Result = Num * Num
        print("Cuadrado del numero: ", Result)
    case "15":
        from math import pi
        
        def Volumen(r, h):
            v = pi * r**2 * h
            return v
        
        Altura = float(input("Altura = "))
        Radio = float(input("Radio = "))

        vol = Volumen (Radio , Altura)
        print("\nV =", vol)
    case "16":
        import math
        cateto1 = float(input("Introducir el Primer cateto: "))
        cateto2 = float(input("Introducir el Segundo cateto: "))

        hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
        print("Hipotenusa: ", hipotenusa)
    case "17":
        import math

        Num1 = int(input("Escribe un numero"))
        Num2 = int(input("Escribe un numero"))

        Result = Num1 + Num2

        print("Resultado", Result)
    case"18":
        import math

        Num1 = int(input("Escribe un numero"))
        Num2 = int(input("Escribe un numero"))

        Result = Num1 - Num2

        print("Resultado", Result)
    case "19":
        import math

        Num1 = int(input("Escribe un numero"))
        Num2 = int(input("Escribe un numero"))

        Result = Num1 * Num2

        print("Resultado", Result)
    case "20":
        import math

        Num1 = int(input("Escribe un numero"))
        Num2 = int(input("Escribe un numero"))

        Result = Num1 / Num2

        print("Resultado", Result)
    case "20":
        for i in range(1, 34):

            resultado = 3 * i
            print(f"3 x {i} = {resultado}\n")
    case _:
        print("No existe esta eleccion:( ")



#region codigo sin uso(Investigacion pendiente)

# #%% 
# F = input ("Ingresar un valor")
# C = round((int(F)-32)/1.8)
# print("C: ", C) 

# #%%
# CHT = input("Ingrese horas de trabajo: ")
# print("Costos hora: ", end = " ")
# PPH = input()
# sueldo = int(CHT) * int(PPH)
# print("Sueldo es: ",sueldo)

# #%%
# cantidad = int(input("Ingrese la cantidad del producto"))
# precio = 1 
# subtotal = cantidad * precio
# IVA = subtotal * 0.12
# total =  subtotal + IVA
# print("Subtotal: ",subtotal)
# print("IVA: ". IVA)
# print("total: ",total)

# #%%
# print('Victor Infante')
# print("Victor Infante")
# print("\tVictor\tInfante")
# print("\tVictor Infante\t",end = " ")
# print("\nVictor", "Infante", sep= "", end= "")
# print("\nVictor", "Infante",end="")

# #%%
# print("***************")
# print("*             *")
# print("*             *")
# print("***************")

# #%%
# nombre = "Mi amigo Sebastian"
# numero1 = 25
# logico1 = False;
# lista = [21,22,23,24,25]
# print(nombre)
# print(numero1)
# print(logico1)
# print(lista[2])

#%%
# t = "palabra,"
# n = 23
# print("Una palabra,",t,"ahora un numero", n)
# m = "Una palabra, {} ahora un numero '{}'".format(t,n)
# print(m)
# print(3 * t + t)

#%%
# x = 7 / 5
# y = 17 / 3
# z = 17 // 3
# w = 17 % 3
# v = 7 ** 2
# u = 7^2
# print(x)
# print(y)
# print(z)
# print(w)
# print(u)

# #%%
# numero = int()
# numero = 4
# sueldo = float()
# sueldo = 2600
# print(numero," ",sueldo)

#%%
# import math
# r = 1
# p = 2 * r * math.pi
# a = math.pi * r * r
# print("Perimetro: ", p)
# print("Area: ", a)

# #%%
# lado = 3 
# n = 5
# ap = 2
# p = lado * n
# A = p * ap
# print("Perimetro: ",p)
# print("Area: ", A)

#%%
# import math
# a = 3
# b = 4
# c1 = math.sqrt(a*a + b*b)
# c2 = math.hypot(a,b)
# print("Hipotenusa: ",c1)
# print("Hipotenusa: ",c2)

# #%%
# import math
# a = 3
# b = 4
# c = 5
# angulo = 53.13010235415598
# h = a / math.cos(angulo * math.pi/180)
# print("Hipotenusa: ",h)
# identidad = 3 / 5
# te = math.acos(identidad)
# print("Angulo: ",te * 180/math.pi)

#endregion
