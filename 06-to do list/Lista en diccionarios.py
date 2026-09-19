tareas=[]
def agregar_tareas(tareas):
    descripcion= input("Escribe la nueva tarea😯: ")
    tarea={"descripcion":descripcion,"completada":False}
    tareas.append(tarea)
    print("Tarea agregada con exito.")


def ver_tareas(tareas):
    if len(tareas)==0:
        print("No hay tareas rgistradas.")
    else:
        for i in range(len(tareas)): #len es una funcion que convierte toda lista en un numero(cuantos elementos tiene)
            estado="✅" if tareas[i]["completada"] else "❌" #if en una sola linea es un operador terniario
            print(f"{i+1}, {estado} {tareas[i]['descripcion']}")


def completar_tarea(tareas):
    ver_tareas(tareas)
    numero=int(input("Que tarea quieres marcar como completada?(numero): "))
    indice=numero-1
    if indice>=0 and indice < len(tareas):
        tareas[indice]["completada"]=True
        print("Tarea macada como completada.")
    else:
        print("Ese numero no existe en la lista")


def eliminar_tarea(tareas):
    ver_tareas(tareas)
    numero=int(input("Que tarea deseas eliminar?(numero)"))
    indice= numero-1
    if indice >=0 and indice < len(tareas):
        tareas.pop(indice)
        print("Tarea eliminada.")
    else:
        print("Ese numero no existe en la lista.")


while True:
    print("\n---MENU---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion=input("Elige una opcion: ")

    if opcion=="1":
        agregar_tareas(tareas)
    elif opcion=="2":
        ver_tareas(tareas)
    elif opcion=="3":
        completar_tarea(tareas)
    elif opcion=="4":
        eliminar_tarea(tareas)
    elif opcion=="5":
        print("Hasta luego..")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
