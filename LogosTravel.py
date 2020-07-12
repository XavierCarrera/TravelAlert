
CIUDADES = {
        "Ciudad de México" : "Hay mucho tráfica de salida al aeropuerto",
        "Buenos Aires" : "Hay una manifestación en la Plaza de Mayo",
        "Bogotá" : "Se espera una lluvia muy fuerte",
        "Lima" : "Alianza juega contra la U. No Acercarse al estadio",
        "Santiago de Chile" : "Piñera se bebió un terremoto. Proceda con precaución",
}

def consulta_destino():
    # print("Tendrás un bonito viaje")
    # consulta_ciudades = CIUDADES
    # consulta = []

    # for resultado in consulta_ciudades:

def admins_password(): 

def run():

    mensaje = ''

    while(True):

        opcion = str(input('''
        ••••••••••••••••••••••••••••••••••••••••••••••
                    S A F E // T R A V E L
        ••••••••••••••••••••••••••••••••••••••••••••••
        
        Bienvenida/o a SafeTravel.com. Aqui podras consultar sobre lo que está
        sucediendo en tu destino de viaje. 

        ¿Qué acción quieres llevar a cabo?

                        [C]onsultar información de mi destino. 
                        [E]ntrar a tu cuenta de administrador.
                        [S]alir

        ''').upper())

        if(opcion == "C"):
            destino = int(input("¿Cual es tu próximo destino? "))
            consulta = consulta_destino()
            # print(consulta)

            if consulta_destino == True:
                print("Consulta exitosa")
            else:
                print("Lo sentimos. No tenemos información de tu destino")

        elif(opcion == "E"):
            print("Bienvenido administrador")
            password = str(input("Escribe tu contraseña de acceso: "))

        elif (opcion == "S"):
            quit()
        else:
            print("Elige una opción válida")

if __name__ == '__main__':
    run()