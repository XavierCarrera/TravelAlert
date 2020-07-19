import random

DAYS_OR_RAIN = (365 / 182) # Futura integración a datos reales en la nube en vez de hardcoding


# class RainChances:
          
#     def __init__(self, chances):
#         self.chances = chances

def stay_length(total_days):
    
    stay_sequence = [] 

    for _ in range(total_days):
        days = random.randint(1, int(DAYS_OR_RAIN))
        stay_sequence.append(days) 

    return stay_sequence

def rain_simulation(total_days, number_simulations): 
    
    simulations = [] 

    for _ in range(number_simulations):
        stay_sequence = stay_length(total_days)
        simulations.append(stay_sequence)

    any_given_day = 0 
    for day_rain in simulations:
        if 1 in day_rain:
            any_given_day += 1

    chances_any_given_day = any_given_day / number_simulations
    print(f"The chances of rain in any given day during your stay is of {round(chances_any_given_day * 100)} % ")

if __name__ == '__main__':
    total_days = int(input("How long are you staying? "))
    number_simulations = 2000

    rain_simulation(total_days, number_simulations)


    
            