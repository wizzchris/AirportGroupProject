from FlightClass import Flight
from PeopleClass import People, Passenger
from PlaneClass import Plane

plane_database = []


flight_class_instance = Flight('100', 'Virgin', 'Bangaladesh', '17/02/2020')


# As a senior member of the airport staff, i want to register a plane.
flight_class_instance.add_plane('100000')

plane_database.append(flight_class_instance)

print(plane_database[0].destination)