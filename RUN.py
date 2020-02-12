from FlightClass import Flight
from PeopleClass import People, Passenger
from PlaneClass import Plane

plane_database = []
passenger_database = []

flight_class_instance = Flight('100', 'Virgin', 'Bangaladesh', '17/02/2020')

# 1.) As a senior member of the airport staff, i want to register a plane.
flight_class_instance.add_plane('100000')

# TEST
# plane_database.append(flight_class_instance)
# print(plane_database[0].destination)


passenger_database.append(passenger_1_instance)
print(passenger_database[0].name)
