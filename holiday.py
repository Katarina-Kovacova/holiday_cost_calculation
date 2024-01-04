# declare variable destinations , store in a list
destinations = ["Barcelona", "Amsterdam", "Rome"]
for destination in destinations:
    print(destination)

# print empty line
print()

# get user to input flight destination for as long as he doesn't enter the destination listed in destinations list
while True:
    city_flight = input("Which city would you like to fly to: ").lower()

# check if user input is one of the destination listed. if it is, break out of the loop
    if city_flight == "barcelona" or city_flight == "amsterdam" or city_flight == "rome":
        break

# ask user to enter the destination again if destination from the list is not entered
    else:
        print("Only choose from the offered destinations please.")


# get user to input how many nights they will be staying at the hotel
while True:
    # check if user enters integer. Ask to re-enter if input is not an integer.
    try:
        num_nights = int(input("Please enter the number of nights you are staying at the hotel: "))
        break
    except ValueError:
        print("Please only enter integers: ")


# get user to input for how many days they will want to rent a car
while True:
    # check if user enters integer. Ask to re-enter if input is not an integer.
    try:
        car_rental_days = int(input("Please enter the number of days for which you will hire a car: "))
        break
    except ValueError:
        print("Please only enter integers: ")

# declare a variable to store cost per night in a hotel
cost_per_night = 105
#

# create function to calculate hotel cost. FUnction takes number of nights as an argument
def hotel_cost(nights_count):
    total_hotel_cost = nights_count * cost_per_night
    return total_hotel_cost

# create function to calculate plane cost. FUnction takes city flight as an argument
def plane_cost(destination):
    pass
    # if destination == "barcelona":
    #     total_plane_cost = flight to barcelona
    # elif destination == "Amsterdam":
    #     total_plane_cost = flight to Amsterdam
    # elif destination == "Rome":
    #     total_plane_cost = flight to Rome
    # else:
    #     print("We do not fly to this destination, please choose from the options above.")
    # return total_plane_cost