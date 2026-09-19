def suma(a,b): 
    return a+b #devuelve este resultado a quien llamo la funcion
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b==0:
        return("Error: no se puede dividir para cero.")
    return a/b
numero1=float(input("Ingrese el primer numero: "))
numero2=float (input("Ingrese el segundo numero: "))
operacion=input("Que operacion desea realizar(+, -, *, /)?: ")
if operacion=="+":
    resultado=suma(numero1, numero2)
elif operacion=="-":
    resultado=resta(numero1,numero2)
elif operacion=="*":
    resultado=multiplicacion(numero1, numero2)
elif operacion=="/":
    resultado=division(numero1, numero2)
else:
    resultado="Opcion invalida."

print(f"El resultado es: {resultado}")        


