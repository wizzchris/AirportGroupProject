from FlightClass import Flight
from PeopleClass import *

daniel = Passenger('Daniel', '1234')
daniel.add_passport('1234')
geoff = Passenger('Geoff', '4321')
geoff.add_passport('4321')

flight1 = Flight('EZY', 'CDG', '2020/02/12', origin='LHR')

flight1.add_customers([daniel, geoff])
#flight1.add_a_customer(geoff)

flight1.print_passengers_on_flight()