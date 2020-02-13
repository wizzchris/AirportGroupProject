""""
Adds a class called flight
"""""
from PeopleClass import Passenger
import pyodbc

server = 'localhost,1433'
database = 'AirportGroupProject'
username = 'SA'
password = 'Passw0rd2018'
# Connection object of db
docker_connect = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = docker_connect.cursor()


class Flight:

    def __init__(self, airline, destination, date_time,origin='London'):  # Starts class with flight number, airline, destination and date time. Allows for future creation of boarding list and origin
        self.flight_num = ''
        self.airline = airline
        self.destination = destination
        self.date_time = date_time
        self.boarding_list = []
        self.origin = origin
        self.plane_name = 'No Name Assigned'
        cursor.execute("INSERT INTO Flights VALUES ('+ self.flight_num + ''

    def add_customers(self, customer_list):  # Starts a class method which adds multiple customers as a list
        self.boarding_list.extend(customer_list)

    def add_a_customer(self, customer):  # Adds a customer to the boarding list, only one customer
        self.boarding_list.append(customer)

    def add_plane(self,plane_name_provided):
        self.plane_name = plane_name_provided

    def add_flight_num(self,plane_list):
        for plane in plane_list:
            if plane.taken == 'no':
                self.flight_num = plane.plane_id
                plane.taken = 'yes'  # Checks to see if plane is taken and adds a flight number to it

    def return_passengers_on_flight(self):
        return self.boarding_list

    def print_passengers_on_flight(self): # method to show passengers on flight
        for i in range(0, len(self.boarding_list)):
            person_dict = self.boarding_list[i]
            print(f"ID: {person_dict._Passenger__passenger_id} || Name: {person_dict.name} || Passport #: {person_dict._Passenger__passport}")