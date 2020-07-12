
CIUDADES = {
        "Ciudad de México" : "Hay mucho tráfica de salida al aeropuerto",
        "Buenos Aires" : "Hay una manifestación en la Plaza de Mayo",
        "Bogotá" : "Se espera una lluvia muy fuerte",
        "Lima" : "Alianza juega contra la U. No Acercarse al estadio",
        "Santiago de Chile" : "Piñera se bebió un terremoto. Proceda con precaución",
}

def consulta_destino():
    print("Tendrás un bonito viaje")
    # consulta_ciudades = CIUDADES
    # consulta = []
    
    # for resultado in consulta_ciudades:

def admin_password(password):
    if password == str("Sarajevo82"):
        return True
    else: 
        return False

def admin_user(user): 
    if user == str("Xavi") or str("Dani") or str("Jann"): 
        return True
    else:
        return False
        print("Nombre de usuario o contraseña equivocada")
    # while password == str("Sarajevo82"):
    #         print("Bienvenido administrador! ")      
    #         break


def run():

    while(True):

        action = str(input('''
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

        if(action == "C"):
            destino = str(input("¿Cual es tu próximo destino? "))
            consulta = consulta_destino()
            print(consulta)

            # if consulta_destino == True:
            #     print("Consulta exitosa")
            # else:
            #     print("Lo sentimos. No tenemos información de tu destino")

        elif(action == "E"):
            user = input("Escribe tu nombre de usuario: ")
            password = input("Hola {}, escribe tu contraseña: ".format(user))
            # result_user = admin_user(user)
            if admin_user(user) and admin_password(password) == True:
                print("Bienvenido administrador! ")
            else:
                print("Nombre de usuario o contraseña equivocada")

        elif(action == "S"):
            quit()
        else:
            print("Elige una opción válida")

if __name__ == '__main__':
    run()