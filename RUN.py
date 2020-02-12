from FlightClass import Flight
from PeopleClass import People, Passenger
from PlaneClass import Plane

plane_database = []


flight_class_instance = Flight('100', 'Virgin', 'Bangaladesh', '17/02/2020')


# As a senior member of the airport staff, i want to register a plane.

import PlaneClass
import PeopleClass
import FlightClass


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
        name = PeopleClass.Passenger(name)
        name.add_passport(passportnum)
        print('Passenger successfully added')

    elif user_answer == 'add passenger to flight':
        print('Adding passenger to flight manually')
        passenger = input('Who would you like to add?\n')
        flight_destination = input('What is the destination?\n')
        for person in passengers:
            if person.name == passenger:
                passenger = person
        for flight in flights:
            if flight_destination == flight.destination:
                flight.add_a_customer(passenger)

    elif user_answer == 'boarding list':
        #checks boarding list

    elif user_answer == 'planes':
        #gives list of planes as plane ids

    elif user_answer == 'destinations':
        #checks destinations

    else:
        print('Please choose a valid command')

flight_class_instance.add_plane('100000')

plane_database.append(flight_class_instance)

print(plane_database[0].destination)
