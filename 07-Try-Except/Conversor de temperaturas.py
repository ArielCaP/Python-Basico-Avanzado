try:
    temperatura=float(input("Ingrese la temperatura: "))
    unidad=input("En que unidad está?(C/F): ").upper()
    if unidad=="C":
        resultado=(temperatura*9/5)+32
        print(f"La temperatura en C° {temperatura} a F° es: {resultado}.")
    elif unidad=="F":
        resultado=(temperatura-32)*5/9
        print(f"La temperatura en F° {temperatura} a C° es: {resultado}.")
    else:
        print("Unidad no valida, escribe C o F")
except ValueError:
    print("Debes ingresar in numero valido para la temperatura._____")
"""
----Tipos de errores mas comunes que podemos usar en un except:

ValueError — El tipo de dato es correcto, pero el valor no tiene sentido para la operación (ej: convertir "hola" a número).

ZeroDivisionError — Ocurre al intentar dividir un número entre cero.

TypeError — Ocurre al mezclar tipos de datos incompatibles entre sí (ej: sumar texto con número directamente).

IndexError — Ocurre al intentar acceder a una posición de una lista que no existe.

KeyError — Ocurre al intentar acceder a una clave de un diccionario que no existe.

FileNotFoundError — Ocurre al intentar abrir un archivo que no existe.

NameError — Ocurre al usar una variable que no ha sido definida previamente.

AttributeError — Ocurre al intentar usar un método que no existe para ese tipo de dato.
"""