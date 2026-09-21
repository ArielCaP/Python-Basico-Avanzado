#.
while True:#Manejo de errores con try y except n un bucle while 
    try:
        numero=int(input("Ingrese un numero: "))
        print(f"Perfecto ingresaste el numero:{numero}.")
        break
    except:
        print("Numero no valido.")