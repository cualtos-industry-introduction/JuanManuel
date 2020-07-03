lista = []
salida="No"
registro=0
def agregar():
    nuevo_usuario={}
    nuevo_usuario['nombre']=input("Nombre de usuario: ")
    nuevo_usuario['apellido']=input("Apellifo de usuario: ")
    nuevo_usuario['numero_de_medidor']=input("Número de medidor de usuario: ")
    lista.append(nuevo_usuario)
def buscar(numerodemedidor):
    while registro in lista:
        print(registro[0])

while(salida == "No"):
    entrada = input("Escribe la opción a efectuar: ")
    if entrada == "Nuevo":
        agregar()
        print("Usuario agregado")
    elif (entrada == "Mostrar"):
        print(lista[:])
        
    elif (entrada == "Bucar"):
        #busca=input("Número de medidor a buscar: ")
        #buscar(busca)
    elif (entrada == "salir"):
        exit()
    else:
        print("Opción no válida")