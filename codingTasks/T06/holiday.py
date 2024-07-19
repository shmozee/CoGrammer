
def hotel_cost(num_nights):
    """Calculates the hotel costs assuming the cost is £40 per night"""
    total = num_nights * 40
    return total

def plane_cost(city_flight):
    """Calculates the cost of the flight based on the 4 destinations below"""
    if city_flight == "Rome":
        cost_of_flight = 50
    elif city_flight == "London":
        cost_of_flight = 100
    elif city_flight == "Paris":
        cost_of_flight = 150
    elif city_flight == "Tokyo":
        cost_of_flight = 3000
    return int(cost_of_flight)

def rental_cost(rental_days):
    """Calculates the costs of the rental based at £10 per day"""
    total = rental_days * 10
    return total

def holiday_cost(hotel_cost, plane_cost, rental_cost):
    """Calculates the total cost of the trip"""
    total_holiday_cost = int(hotel_cost) + int(plane_cost) + int(rental_cost)
    return total_holiday_cost



# User inputs

city_flight = input("The city you will be flying to (Rome, London, Paris, Tokyo): ")
num_nights = int(input("The number of nights you will stay at the hotel (£40 per night): "))
rental_days = int(input("The number of days you will be renting a car (£10 per day): "))

# Calulations / Outputs


print("\n" + "Calculations")
print("==========================")
print("Hotel cost: £", hotel_cost(num_nights))
print("Plane cost: £", plane_cost(city_flight))
print("Rental cost: £", rental_cost(rental_days))
print("\n" +"==========================")

print("Total cost: £", holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), rental_cost(rental_days)))
print("==========================")
