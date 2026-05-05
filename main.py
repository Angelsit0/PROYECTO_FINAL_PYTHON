import json 
totalgastos = 0
intentos = 0

with open ("config.json","r") as file:
    config = json.load(file)


while(intentos < config["intentos"]):
    user = input("Indique su  usuario: \n")
    password = input("Indique su  documento valido: \n")  
    if(user == config["usuario"]) and (password == config["clave"]):
        print("-------------- Ha ingresado al sistema de Control De Gastos--------------")
        print("Bienvenido " + user + " 🥰 ")

        while(True):
            print("-------------- OPCIONES A ELEGIR-------------- ")
            print("1) Agregar dinero")
            print("2) Agregar Gasto ")
            print("3) Ver historial de movimientos")
            print("4) Ver Balance")
            print("5) Salir")
            opcion=int(input("Seleccione alguna de las opciones: \n"))


            if(opcion == 1): 
                 print("Su saldo disponible es: " + config["saldo"])
                 print("Cuanto dinero desea transferir a su cuenta el dia de hoy: \n")
                 dinero_agregado=float(input())
                 config["saldo"]= config["saldo"]  + dinero_agregado

            
            elif(opcion == 2 ):
                    numero_gastos = int(input("Cuantos gastos desea ingresar: \n"))
                    for i in range(numero_gastos):
                        gastos_hechos = float(input("Ingrese el gasto " + str(i+1) + ":\n"))
                        totalgastos= totalgastos + gastos_hechos
                    print("Usted gasto hoy un total de ",round(totalgastos,2))
            
            elif(opcion == 4):
                 print("Su balance disponible es: ", config["saldo"])

    else:
        print("Datos ingresados erroneos")
        intentos = intentos + 1
        


