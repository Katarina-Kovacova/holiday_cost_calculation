# declare constant variables to store cost per night in a hotel, car rental cost per day and flight costs
COST_PER_NIGHT = 100
DAILY_CAR_RENTAL_COST = 20
FLIGHT_TO_BARCELONA = 150
FLIGHT_TO_AMSTERDAM = 200
FLIGHT_TO_ROME = 180
TOTAL_PLANE_COST = 0


# define welcoming function that prints
def destination_menu():
    barcelona = "Barcelona"
    amsterdam = "Amsterdam"
    rome = "Rome"
    print(f"Hello! Welcome to our holiday calculator!"
          f"Please choose from our destinations menu: {barcelona}, {amsterdam} or {rome}")


def city_choice():
    # get user to input flight destination for as long as he doesn't enter the destination listed in destinations list
    while True:
        city_flight = input("Which city would you like to fly to: ").lower()

    # check if user input is one of the destination listed. if it is, break out of the loop
        if city_flight == "barcelona" or city_flight == "amsterdam" or city_flight == "rome":
            break

    # ask user to enter the destination again if destination from the list is not entered
        else:
            print("Only choose from the offered destinations please.")
    return city_flight


def nights_at_hotel():
    # get user to input how many nights they will be staying at the hotel
    while True:
        # check if user enters integer. Ask to re-enter if input is not an integer.
        try:
            num_nights = int(input("Please enter the number of nights you are staying at the hotel: "))
            break
        except ValueError:
            print("Please only enter integers: ")
    return num_nights


def how_many_car_days():
    # get user to input for how many days they will want to rent a car
    while True:
        # check if user enters integer. Ask to re-enter if input is not an integer.
        try:
            car_rental_days = int(input("Please enter the number of days for which you will hire a car: "))
            break
        except ValueError:
            print("Please only enter integers: ")
    return car_rental_days


# create function to calculate hotel cost. FUnction takes number of nights as an argument
def hotel_cost(nights_count):
    total_hotel_cost = nights_count * COST_PER_NIGHT
    return total_hotel_cost


# create function to calculate plane cost. Function takes city flight as an argument
def plane_cost(town):
    if town == "barcelona":
        return FLIGHT_TO_BARCELONA
    elif town == "amsterdam":
        return FLIGHT_TO_AMSTERDAM
    elif town == "rome":
        return FLIGHT_TO_ROME


def car_rental(rental_days):
    total_car_cost = rental_days * DAILY_CAR_RENTAL_COST
    return total_car_cost


def holiday_cost(hotel_costs, plane_costs, car_rentals_costs):
    total_holiday_cost = hotel_costs + plane_costs + car_rentals_costs
    return f"Total holiday cost is £{total_holiday_cost}."


if __name__ == "__main__":
    destination_menu()
    city = city_choice()
    num_nights_at_hotel = nights_at_hotel()
    num_car_days = how_many_car_days()
    hotel_price = hotel_cost(num_nights_at_hotel)
    plane_price = plane_cost(city)
    car_days = car_rental(num_car_days)
    print(holiday_cost(hotel_price, plane_price, car_days))
