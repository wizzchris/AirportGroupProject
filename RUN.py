# DROP TABLE Customers
# DROP TABLE Planes
# DROP TABLE Flights
#
#
# CREATE TABLE Customers
# (
# Customername VARCHAR(255),
# Destination VARCHAR(255),
# Passport VARCHAR(255),
# ID VARCHAR(255))hel
#
# CREATE TABLE Planes
# (
# Capacity VARCHAR(255),
# Manufacturer VARCHAR(255),
# Model VARCHAR(255),
# Flights VARCHAR(255),
# Taken VARCHAR(255),
# Plane_ID VARCHAR(255),
# Airline VARCHAR(255))
#
# CREATE TABLE Flights
# (
# Airline VARCHAR(255),
# Destination VARCHAR(255),
# Date_Time VARCHAR(255),
# Origin VARCHAR(255),
# Flight_Name VARCHAR(255),
# Boarding_List VARCHAR(255),
# Plane_Name VARCHAR(255))

from FlightClass import Flight
from PeopleClass import People, Passenger
from PlaneClass import Plane
import pyodbc

# How do we put objects into a database

server = 'localhost,1433'
databse = 'AirportGroupProject'
username = 'SA'
password = 'Passw0rd2018'
# Connection object of db
docker_connect = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + databse + ';UID=' + username + ';PWD=' + password)
cursor = docker_connect.cursor()

plane_database = []
passenger_database = []
flights = []

while True:
    user_answer = input(
        'Hello, what would you like to do?\nType "Help" for help\nType "Exit" for exit\n\n>>> ').strip().lower()

    if user_answer == 'exit':
        break

    elif user_answer == 'help':
        print(
            'The Commands\nType "Help" for help\nType "Exit" to break\n 1.) Type "Register plane" to add a new plane\n 2.) Type "Add passenger" to add a new passenger\n 3.) Type "Add passenger" to flight to add a passenger to a flight manually\n 4.) Type "Boarding list" to see the boarding list\n 5.) Type "Planes" to check the planes\n 6.) Type "Destinations" to check the flights')

    elif user_answer == 'register plane':  # def __init__(self, capacity, manufacturer, model, flights=None, taken='no'):
        print('Register a plane')
        name = input('Please name the plane.\n').strip().lower()
        capacity = input('What is the capacity of the plane?\n').strip().lower()
        manufacturer = input('Who is the manufacturer?\n').strip().lower()
        model = input('What is the model?\n').strip().lower()
        name = Plane(capacity, manufacturer, model)
        print('Plane successfully added')
        plane_database.append(name)

    elif user_answer == 'add passenger':  # def __init__(self, name)
        print('Add a passenger')
        name = input('What is their name?\n').strip().lower()
        passportnum = input('What is their passport number?\n')
        passanger_destination = input('Where are they going?\n')
        name = Passenger(name, passanger_destination)
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
        rows_destinations = cursor.execute(
            'SELECT Destination, Flight_Name AS "Flight Name", Boarding_List AS "Boarding List" FROM Flights WHERE Destination = {}'.format(
                flightdesired))
        while True:
            record = rows_destinations.fetchone()
            if record == None:
                break
            print(record)

    elif user_answer == 'planes':
        rows_planes = cursor.execute('SELECT Manufacturer, Model, Plane_ID AS "Plane ID" FROM Planes')
        while True:
            record = rows_planes.fetchone()
            if record == None:
                break
            print(record)

    elif user_answer == 'destinations':
        for flight in flights:
            print(flight.destination)
        # rows_flights = cursor.execute('SELECT Destination, Flight_Name AS "Flight Name" FROM Flights')
        # while True:
        #     record = rows_flights.fetchone()
        #     if record == None:
        #         break
        #     print(record)

    elif user_answer == 'add flight':  # __init__(self, airline, destination, date_time,origin='London'):
        print('Add a flight')
        name = input('Please name the flight\n')
        airline = input('What is the airline?\n')
        destination = input('What is the destination?\n')
        date_time = input('What is the date and time?\n')
        name = Flight(airline, destination, date_time)
        name.add_flight_num(plane_database)
        flights.append(name)

    else:
        print('Please choose a valid command')
