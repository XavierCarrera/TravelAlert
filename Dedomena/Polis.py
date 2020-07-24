import csv

def create():

        with open("cities_list.txt", mode='w') as csv_file:
                fieldnames = ["ID", "CITY", "CITY INFO"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                city = input("What's the name of the city you wish to add? ")
                city_info = input(f"What info you wish to add to {city}? ")
                writer.writeheader()
                writer.writerow({"ID": "x", "CITY" : city, "CITY INFO" : city_info})
                                

def read():

        # with open('cities_list.txt', mode='r') as csv_file:
        #         csv_reader = csv.DictReader(csv_file)
        #         line_count = 0
        #         for row in csv_reader:
        #                 if line_count == 0:
        #                 print(row["ID"], row["CITY"], row["CITY INFO"])

        with open('cities_list.txt', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                for row in csv_reader:
                        if line_count == 0:
                                print(row["ID"], row["CITY"], row["CITY INFO"])
                        
        

def update():

        pass
                
        # global cities
        
        # city = input("What city you want to update? ")
        # if city in cities:
        #         info = input(f"What information you wish to add to {city}? ")
        #         cities[city] = info
        #         print("The data was updated")
        # else:
        #         print("The city is not in the Data Base! ")

def delete():

        pass
                
        # global cities
        
        # city = input("What city you want to delete? ")
        # if city in cities:
        #         cities.pop(city)
        #         print("The city was deleted")
        # else:
        #         print("The city is not in the Data Base! ")

def run():

        while(True):

                action = str(input("""
                        ••••••••••••••••••••••••••••••••••••••••••••••
                                   T R A V E L // A L E R T
                        ••••••••••••••••••••••••••••••••••••••••••••••

                        Welcome to Travel Alert. What do you want to do today?

                        [C]reate a new entry
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

