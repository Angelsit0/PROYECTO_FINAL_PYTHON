import json

def leer_json():
#Abro y leo el archvio config.json a su vez lo defino con una variable "config" a la cual llamo al momento de usar los datos del .json
    with open ("config.json","r") as file:
        config = json.load(file)
        return config

def guardar_json():
     with open ("config.json","w") as file:
          json.dump(config,file)

def historial_json():
     with open ("historial.json","r") as file:
          historial = json.load(file)
          return historial
           
           
        
    
def menu_principal():
    while(True):
    
        print("-----------------------------------------")
        print("🐍---💵SISTEMA DE GASTOS PYANGEL💵---🐍")
        print("-----------------------------------------")
        primeras_opciones=print("1. Iniciar sesión \n2. Salir del sistema")
        print("------------------------------------------")
        print("Bienvenido Al sistema 🐍PYNGEL🐍 \nmaneje sus finanzas de la mejor manera")
        print("\n💵💵💵|AHORA NO MAS PREOCUPACION|💵💵💵\nCon 🐍 PYNGEL🐍 tendras todas tu salud económica a la mano y seras conciente de como manejas tu dinero\n")
        print("🐍---💵Ingrese su opción a realizar💵---🐍")
        primeras_opciones=input()
        if primeras_opciones == "1":
            login()
            
        elif primeras_opciones == "2":
            print("\n🐍---CERRANDO SISTEMA---🐍")
            print("Ha salido con exito del sistema")
            break
        else:
             primeras_opciones
             print("\n🐍--- Error, Ingrese por pantalla una opción valida ---🐍\n")
             

def login():
    intentos = 0
    login=False
 #Aqui abro un ciclo while para ejecutar el bloque de codigo del login continuamente hasta que se hagan 3 intentos y se cierre el sistema 
    while(intentos < config["intentos"]):
    #Imprimo una interfaz del login del usuario introduce usuario y documento
        print("______________________________________________ \n")
        print("\n🐍---Bienvenido al sistema Pyngel su billetera virtual---🐍")
        print("______________________________________________")
        
        user = input("Indique su  usuario: \n")
        print("______________________________________________")
        password = input("Indique su  documento valido: \n")  
        print("____________________________________________________________________________")

    #Abro un condicional if para validar que el usuario y documento sean los correctos de ser correcto entrara al sistema de lo contrario se permitiran 3 intentos hasta cerrar el sistema
        if(user == config["usuario"]) and (password == config["clave"]):
        
    #Imprimo una interfaz de ingreso al sistema
            print("\n🐍---Bienvenido al sistema Pyngel su billetera virtual---🐍")
            print("Bienvenido " + user + " 🥰 ")
            login=True
            break

        else:
            print("Datos ingresados \nERRONEOS")
            intentos = intentos + 1
        
    if (login):
        menu_secundario()

def menu_secundario():
        
    totalgastos = 0
    
#Abro ciclo while para crear un menu interactivo de opciones para poder redirigir al usuario a lo que necesita 
    while(True):
        print("🐍--- BALANCE PYNGEL ---🐍")
        print("Su balance disponible es: ", config["saldo"])
        print("-------------- OPCIONES A ELEGIR-------------- ")
        print("1) Agregar dinero")
        print("2) Agregar Gasto ")
        print("3) Ver historial de movimientos")
        print("4) Ver Balance")
        print("5) Cerrar Sesión")
        opcion=int(input("Seleccione alguna de las opciones: \n"))
        

#opcion 1 (Nos muestra nuestro dinero, podemos agregar nuestro dinero se suma a este dinero que tenia)
        if(opcion == 1): 
                print("\n🐍---  DINERO PYNGEL ---🐍")
                print("Su saldo disponible es: " + str(config["saldo"]))
                print("Cuanto dinero desea transferir a su cuenta el dia de hoy:")
                dinero_agregado=float(input())
                config["saldo"]= config["saldo"]  + dinero_agregado
                guardar_json()
                historial=historial_json()

                operacion_agregar= {
                     "operacion" : "ingreso",
                     "saldo" : dinero_agregado
                }
                historial.append(operacion_agregar)
                with open ("historial.json","w") as file:
                    json.dump(historial,file)

                
                

#opcion 2 (Podemos ingresar cuantos gastos hicimos y de cuanto fue, muestra cuanto se gasto, se hace la operacion de cuanto queda)
        elif(opcion == 2 ):
# Vuelvo totalgastos a 0 al entrar, para que no arrastre la suma si entras a esta opción dos veces seguidas
                totalgastos = 0 
                print("\n🐍--- GASTOS PYNGEL ---🐍")
                numero_gastos = int(input("Cuantos gastos desea ingresar: \n"))
                for i in range(numero_gastos):
                    gastos_hechos = float(input("Ingrese el gasto " + str(i+1) + ":\n"))
                    totalgastos= totalgastos + gastos_hechos
                print("Usted gasto hoy un total de ",round(totalgastos,2))
                
                if(config["saldo"] < gastos_hechos):
                     print("Esta operacion no es posible, su gasto es mayor a su saldo disponible.")
                else:
                     config["saldo"]= config["saldo"]  - totalgastos
                     historial=historial_json()
                     operacion_gasto={
                          "operacion":"gasto",
                          "saldo": totalgastos
                     }
                     historial.append(operacion_gasto)
                     with open("historial.json","w") as file:
                          json.dump(historial,file)

                


#opcion 3 (Muestra lo que se haya guardado en el historial.json)      
        elif(opcion == 3 ):
                print("-------------- HISTORIAL DE MOVIMIENTOS--------------")
                historial=historial_json()
                with open ("historial.json","r") as file:
                    historial = json.load(file)
                    print(historial)

#opcion 4 (Muestra el balance disponible actual de nuestro usuario)    
        elif(opcion == 4):
                
                print("Su balance disponible es: ", config["saldo"])

#opcion5 (Sale del sistema y muestra un mensaje de salida se usa(break))               
        elif(opcion == 5):
                print("\n🐍--- CERRAR SESIÓN PYNGEL ---🐍")
                print("Ha cerrado sesión con exito")
                break
        else:
             print("\n🐍--- Error, Ingrese por pantalla una opción valida ---🐍\n")
   


config=leer_json()
menu_principal()

