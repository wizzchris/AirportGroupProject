from FlightClass import Flight
from PeopleClass import People, Passenger
from PlaneClass import Plane

plane_database = []

flights = []

passenger_database = []

# 1.) As a senior member of the airport staff, i want to register a plane.


# 0.) As a senior member of the airport staff, i want to register a plane.

flight_class_instance = Flight('100', 'Virgin', 'Bangaladesh', '17/02/2020')
plane_database.append(flight_class_instance)
flight_class_instance = Flight('100', 'Virgin', 'Bangaladesh', '17/02/2020')

# 2.) I want to register a plane
plane_class_instance = Plane(1000, 'Boeing', 'B141')


import PlaneClass
import PeopleClass
import FlightClass


# while True:
#     user_answer = input('Hello, what would you like to do?\nType Help for help\nType Exit for exit').strip().lower()
#
#     if user_answer == 'exit':
#         break
#
#     elif user_answer == 'help':
#         print('The Commands\nHelp for help\nExit to break')
#
#     elif user_answer == 'register plane':
#         #adds a plane
#
#     elif user_answer == 'add passenger':
#         #adds passenger
#
#     elif user_answer == 'add passenger to flight':
#         #adds passenger to flight
#
#     elif user_answer == 'boarding list':
#         #checks boarding list
#
#     elif user_answer == 'planes':
#         #gives list of planes as plane ids
#
#     elif user_answer == 'destinations':
#         #checks destinations
#
#     else:
#         print('Please choose a valid command')

while True:
    user_answer = input('Hello, what would you like to do?\nType Help for help\nType Exit for exit\n').strip().lower()

    if user_answer == 'exit':
        break

    elif user_answer == 'help':
        print('The Commands\nHelp for help\nExit to break\nRegister plane to add a new plane\nAdd passenger to add a new passenger\nAdd passenger to flight to add a passenger to a flight manually\nBoarding list to see the boarding list\nPlanes to check the planes\nDestinations to check the flights')

    elif user_answer == 'register plane':  #def __init__(self, capacity, manufacturer, model, flights=None, taken='no'):
        print('Register a plane')
        name = input('Please name the plane.\n').strip().lower()
        capacity = input('What is the capacity of the plane?\n').strip().lower()
        manufacturer = input('Who is the manufacturer?\n').strip().lower()
        model = input('What is the model?\n').strip().lower()
        name = PlaneClass.Plane(capacity,manufacturer,model)
        print('Plane successfully added')
        plane_database.append(name)

    elif user_answer == 'add passenger':  #    def __init__(self, name)
        print('Add a passenger')
        name = input('What is their name?\n').strip().lower()
        passportnum = input('What is their passport number?\n')
        passanger_destination = input('Where are they going?\n')
        name = PeopleClass.Passenger(name, passanger_destination)
        name.add_passport(passportnum)
        name.add_passenger_to_flight(flights)
        passenger_database.append(name)
        print('Passenger successfully added')

    elif user_answer == 'add passenger to flight':
        print('Adding passenger to flight manually')
        passenger = input('Who would you like to add?\n')
        flight_destination = input('What is the destination?\n')
        for person in passenger_database:
            if person.name == passenger:
                passenger = person
        for flight in flights:
            if flight_destination == flight.destination:
                flight.add_a_customer(passenger)
        print('Passenger successfully added')

    elif user_answer == 'boarding list':
        print('Boarding list')
        flightdesired = input('What is the destination you want to check on?\n')
        for flight in flights:
            if flightdesired == flight.destination:
                for person in flight.boarding_list:
                    print(person.name)

    elif user_answer == 'planes':
        for plane in plane_database:
            print(str(plane.plane_id) + ' ' + str(plane.destination))

    elif user_answer == 'destinations':
        for flight in flights:
            print(flight.destination)

    elif user_answer == 'add flight':  #__init__(self, airline, destination, date_time,origin='London'):
        print('Add a flight')
        name =input('Please name the flight\n')
        airline = input('What is the airline?\n')
        destination = input('What is the destination?\n')
        date_time = input('What is the date and time?\n')
        name = FlightClass.Flight(airline,destination,date_time)
        name.add_flight_num(plane_database)
        flights.append(name)

    else:
        print('Please choose a valid command')

flight_class_instance.add_plane('100000')


# # TEST
# plane_database.append(flight_class_instance)
# print(plane_database[0].destination)
#
#
# passenger_database.append(passenger_1_instance)

#
# print(passenger_database.name)
# print(plane_database.destination)

print(passenger_database[0].name)
print(plane_database[0].destination)

# while True:
#     user_answer = input('Hello, what would you like to do?\nType Help for help\nType Exit for exit').strip().lower()
#
#     if user_answer == 'exit':
#         break
#
#     elif user_answer == 'help':
#         print('The Commands\nHelp for help\nExit to break')
#
#     elif user_answer == 'register plane':
#         #adds a plane
#
#     elif user_answer == 'add passenger':
#         #adds passenger
#
#     elif user_answer == 'add passenger to flight':
#         #adds passenger to flight
#
#     elif user_answer == 'boarding list':
#         #checks boarding list
#
#     elif user_answer == 'planes':
#         #gives list of planes as plane ids
#
#     elif user_answer == 'destinations':
#         #checks destinations
#
#     else:
#         print('Please choose a valid command')
