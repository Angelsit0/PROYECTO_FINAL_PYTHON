#Importo el .json para poder leer los datos y usarlos 
import json 
#Defino varibables necesarias para crear acumuladores
totalgastos = 0
intentos = 0

#Abro y leo el archvio config.json a su vez lo defino con una variable "config" a la cual llamo al momento de usar los datos del .json
with open ("config.json","r") as file:
    config = json.load(file)

#Aqui abro un ciclo while para ejecutar el bloque de codigo del login continuamente hasta que se hagan 3 intentos y se cierre el sistema 
while(intentos < config["intentos"]):

#Imprimo una interfaz del login del usuario introduce usuario y documento
    print("______________________________________________ \n")
    print("Bienvenido al sistema Pyngel su billetera virtual")
    print("______________________________________________")
    user = input("Indique su  usuario: \n")
    print("______________________________________________")
    password = input("Indique su  documento valido: \n")  
    print("____________________________________________________________________________")

#Abro un condicional if para validar que el usuario y documento sean los correctos de ser correcto entrara al sistema de lo contrario se permitiran 3 intentos hasta cerrar el sistema
    if(user == config["usuario"]) and (password == config["clave"]):\
    
#Imprimo una interfaz de ingreso al sistema
        print("-------------- Ha ingresado al sistema de Control De Gastos--------------")
        print("Bienvenido " + user + " 🥰 ")

#Abro ciclo while para crear un menu interactivo de opciones para poder redirigir al usuario a lo que necesita 
        while(True):
            print("-------------- OPCIONES A ELEGIR-------------- ")
            print("1) Agregar dinero")
            print("2) Agregar Gasto ")
            print("3) Ver historial de movimientos")
            print("4) Ver Balance")
            print("5) Salir")
            opcion=int(input("Seleccione alguna de las opciones: \n"))

#opcion 1 (Nos muestra nuestro dinero, podemos agregar nuestro dinero se suma a este dinero que tenia)
            if(opcion == 1): 
                 print("Su saldo disponible es: " + str(config["saldo"]))
                 print("Cuanto dinero desea transferir a su cuenta el dia de hoy:")
                 dinero_agregado=float(input())
                 config["saldo"]= config["saldo"]  + dinero_agregado

#opcion 2 (Podemos ingresar cuantos gastos hicimos y de cuanto fue, muestra cuanto se gasto, se hace la operacion de cuanto queda)
            elif(opcion == 2 ):
                    numero_gastos = int(input("Cuantos gastos desea ingresar: \n"))
                    for i in range(numero_gastos):
                        gastos_hechos = float(input("Ingrese el gasto " + str(i+1) + ":\n"))
                        totalgastos= totalgastos + gastos_hechos
                    print("Usted gasto hoy un total de ",round(totalgastos,2))
                    config["saldo"]= config["saldo"]  - totalgastos

#opcion 4 (Muestra el balance disponible actual de nuestro usuario)    
            elif(opcion == 4):
                 print("Su balance disponible es: ", config["saldo"])
 
 #opcion5 (Sale del sistema y muestra un mensaje de salida se usa(break))               
            elif(opcion == 5):
                 print("Ha salido con exito del sistema")
                 break

    else:
        print("Datos ingresados erroneos")
        intentos = intentos + 1
        


