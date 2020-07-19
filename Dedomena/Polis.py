import csv

cities = {
        "Amsterdam" : "a",
        "Barcelona" : "b",
        "Chicago" : "c",
        "Dubai" : "d",
        "El Paso" :"e",
        "Frankfurt" : "f", 
        "Glasgow" : "g",
        "Helsinki" : "h",
        "Indiana Falls" : "i",
        "Johannesbourg" : "j",
        "Kazan" : "k",
        "Lahore" : "l",
        "Mumbai" : "m",
        "Nassau" : "n",
        "Ottawa" : "o",
        "Panama City" : "c",
        "Quezon City" : "q",
        "Rio de Janeiro" : "r",
        "Sao Paolo" : "s",
        "Tel Aviv" : "t",
        "Urbana" : "u",
        "Victoria" : "v",
        "Warsaw" : "w",
        "York" : "y",
        "Zurich" : "z", 
        }

# class CitiesDataBase:

#         def __init__(self, user, password):
#                 self.user = user
#                 self.password = password

def create():
    
        city = input("What's the name of the city you wish to add? ")
        if city not in cities:
                info = input("What information you wish to add? ")
                print("The data base was updated! ")
                cities[city] = info
        else:
                print("That city is already on the list! ")

def read():

        for city, info in cities.items():
                print(city + " : " + info)

def update():
                
        city = input("What city you want to update? ")
        if city in cities:
                info = input(f"What information you wish to add to {city}? ")
                cities[city] = info
                print("The data was updated")
        else:
                print("The city is not in the Data Base! ")

def delete():
                
        city = input("What city you want to delete? ")
        if city in cities:
                cities.pop(city)
                print("The city was deleted")
        else:
                print("The city is not in the Data Base! ")

def run():

        while(True):

                action = str(input("""
                        ••••••••••••••••••••••••••••••••••••••••••••••
                                   T R A V E L // A L E R T
                        ••••••••••••••••••••••••••••••••••••••••••••••

                        Welcome to Travel Alert. What do you want to do today?

                        [C]reat a new entry
                        [R]ead the database
                        [U]pdate the data base
                        [D]elete a entry
                        [E]xit 

                        """).upper())
        
                if action == "C":
                        create()
                elif action == "R":
                        read()
                elif action == "U":
                        update()
                elif action == "D":
                        delete()
                elif action == "E":
                        quit()
                else:
                        while action != "C" or "R" or "U" or "D" or "E":
                                new_action = input("That's an invalid option. Press any key to try again ")
                                break

if __name__ == "__main__":
    run()

