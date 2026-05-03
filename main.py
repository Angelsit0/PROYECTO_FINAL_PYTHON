user = "Angel"
clave = 32984739
totalgastos = 0

ingreso = input("Ingrese su usuario: ")
documento=int(input("Ingrese su documento: "))
if(user == ingreso ) and (clave == documento):
    print("Usted ha ingresado con exito")
    print("Bienvenido Al Sistema De Control De Gastos (Angel Opera)")
    print("USUARIO: " + user  )
    print("Su documento valido es:", documento)
    print("Cuanto dinero tiene disponible al dia de hoy ")
    dinero=float(input())

    numero_gastos = int(input("Cuantos gastos desea ingresar: "))
    for i in range(numero_gastos):

        gastos_hechos = float(input("Ingrese el gasto " + str(i+1) + ":"))
        totalgastos= totalgastos + gastos_hechos


    print("-----------------------PROCESANDO GASTO-------------------------")
    print(".....")
    print(".....")
    print(".....")
    operacion=(dinero-totalgastos)
    print("Usted gasto hoy un total de ",round(totalgastos,2))
    print("En su cuenta queda un total de ",round(operacion,2))
    if(totalgastos>dinero):
        print(user +", Te has excedido con los gastos hoy ")
    if(operacion<0):
        print(user+ ", Tines una deuda de: ", operacion )
else:
    print("Usted ha introducido algun dato erroneo")