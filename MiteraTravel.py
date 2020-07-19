import random
import os

ciudades = {
    "Ciudad de México" : "AMLO está en el aeropuerto. No esperes salir pronto",
    "Buenos Aires" : "Hay una manifestación en la Plaza de Mayo",
    "Bogotá" : "Se espera una lluvia muy fuerte",
    "Lima" : "Alianza juega contra la U. No acercarse al estadio.",
    "Santiago de Chile" : "Piñera se bebió un terremoto. Proceda con precaución",
    }

PROBABIIDAD_LLUVIA = {
    "Ciudad de México" : [14, 41, 27, 36, 62, 9, 23],
    "Buenos Aires" : [45, 42, 32, 39, 71, 11, 14],
    "Bogotá" : [67, 74, 68, 61, 84, 91, 66],
    "Lima" : [40, 39, 20, 33, 87, 26, 30],
    "Santiago de Chile" : [32, 41, 39, 59, 70, 49, 28],
    }

def consulta_destino():
    destino = str(input("¿Cual es tu próximo destino? "))
    if destino in ciudades and PROBABIIDAD_LLUVIA:
        print(ciudades[destino])
        print(f"La temperatura será de {random.randint(12, 35)} grados centígrados")
        lluvia = sum(PROBABIIDAD_LLUVIA[destino]) // len(PROBABIIDAD_LLUVIA[destino])
        print(f"La probabilidad para hoy de lluvia es del {lluvia}%")
        lluvia = PROBABIIDAD_LLUVIA[destino]
        lluvia.sort()
        print(f"El día menos lluvioso de la semana tendrá {lluvia[0]}% de probabilidades de lluvia")
    else:
        print("Lo sentimos, no tenemos info de tu destino")
    
def menu_user():
    
    while(True):

        action_user = str(input('''
            ••••••••••••••••••••••••••••••••••••••••••••••
                        T R A V E L // A L E R T
            ••••••••••••••••••••••••••••••••••••••••••••••
            
            Bienvenido administrador! 
            ¿Qué acción quieres llevar a cabo?
                            [C]onsultar información de todos los destinos. 
                            [E]ntrar al agregador de consultas.
                            [R]egresar al menu principal
                            [S]alir
            ''').upper())
        
        if action_user == "C": 
            for ciudad, info in ciudades.items():
                print(ciudad + " : " + info)
        elif action_user == "E":

            ciudad_nueva = input("¿Qué ciudad deseas agregar? ")
            info_nueva = input("¿Que información deseas agregar? ")
            print("Base de datos actualizada")     
            ciudades[ciudad_nueva] = info_nueva

            for ciudad, info in ciudades.items():
                print(ciudad + " : " + info)

        if action_user == "R": 
            os.system ("cls")
            run()
        
        elif action_user == "S":
            quit()

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
    
def run():

    while(True):
 
        action = str(input('''
        ••••••••••••••••••••••••••••••••••••••••••••••
                    T R A V E L // A L E R T
        ••••••••••••••••••••••••••••••••••••••••••••••
        
        Bienvenida/o a SafeTravel.com. Aqui podras consultar sobre lo que está
        sucediendo en tu destino de viaje. 
        ¿Qué acción quieres llevar a cabo?
                        [C]onsultar información de tu destino. 
                        [E]ntrar a tu cuenta de administrador.
                        [S]alir
        ''').upper())

        if action == "C": 
            consulta_destino()

        elif action == "E":
            user = input("Escribe tu nombre de usuario: ")
            password = input("Hola {}, escribe tu contraseña: ".format(user))
            if admin_user(user) and admin_password(password) == True:
                os.system ("cls") 
                menu_user()
            else:
                print("Nombre de usuario o contraseña equivocada")

        elif action == "S":
            quit()
        else:
            print("Elige una opción válida")

if __name__ == '__main__':
    run()