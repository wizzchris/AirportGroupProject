from FlightClass import Flight
from PeopleClass import People, Passenger
from PlaneClass import Plane

plane_database = []
passenger_database = []

# 1.) As a senior member of the airport staff, i want to register a plane.
flight_class_instance = Flight('100', 'Virgin', 'Bangaladesh', '17/02/2020')

# 2.) I want to register a plane
plane_class_instance = Plane(1000, 'Boeing', 'B141')


# import PlaneClass
# import PeopleClass
# import FlightClass

#
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
#
# flight_class_instance.add_plane('100000')


# TEST
plane_database.append(flight_class_instance)
print(plane_database[0].destination)


passenger_database.append(passenger_1_instance)

print(passenger_database.name)
print(plane_database.destination)
