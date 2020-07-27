import time
import random

DAYS_OR_RAIN = (365 / 93) 

def stay_length(total_days):
    
    stay_sequence = [] 

    for _ in range(total_days):
        days = random.randint(1, int(DAYS_OR_RAIN))
        stay_sequence.append(days) 

    return stay_sequence

def rain_simulation(total_days, number_simulations): 
    
    simulations = [] 

    for _ in range(number_simulations):
        rain_sequence = stay_length(total_days)
        simulations.append(rain_sequence)

    any_given_day = 0 
    for day_rain in simulations:
        if 1 in day_rain:
            any_given_day += 1

    chances_any_given_day = any_given_day / number_simulations

    print(f"The chances of rain in any given day during your stay is of {round(chances_any_given_day * 100)} % ")
    print(rain_sequence)

if __name__ == '__main__':
    total_days = int(input("How many days are you staying? "))
    number_simulations = 16000

    comienzo = time.time()
    rain_simulation(total_days, number_simulations)
    final = time.time()
    print(number_simulations)
    print(f"Complejidad algorítmica: {(final - comienzo)}")

        