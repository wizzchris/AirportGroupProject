"""
Adds a class called plane
"""
import pyodbc # Imports the library so that we can

server = 'localhost,1433'
databse = 'AirportGroupProject'
username = 'SA'
password = 'Passw0rd2018'
# Connection object of db called Airport Group Project
docker_connect = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + databse + ';UID=' + username + ';PWD=' + password)
cursor = docker_connect.cursor()


class Plane:
    Plane_id = 0  # Starts the id convention

    def __init__(self, capacity, manufacturer, model, flights=None, taken='no'):  # Initialises class with capacity
        self.capacity = capacity
        self.plane_id = 'A-P-' + str(Plane.Plane_id)  # Adds the plane id
        Plane.Plane_id += 1  # Adds 1 to the id after creation
        self.Airline = ''  # Allows the plane class to have airline
        if flights is None:
            flights = []
            flights_sql = 'Null'
        self.flights = flights
        self.taken = taken  # Check to see if plane is taken on a flight
        self.plane_id = 'A-P-' + str(Plane.Plane_id)  # Adds the plane id
        Plane.Plane_id += 1  # Adds 1 to the id after creation
        self.Airline = ''
        airline_sql = 'Null'  # Allows the plane class to have airline
        self.manufacturer = manufacturer
        self.model = model

        cursor.execute("INSERT INTO Planes (Capacity, Manufacturer, Model, Flights, Taken, Plane_ID, Airline)VALUES ('" + str(self.capacity) + "', '" + str(self.manufacturer) + "', '" + str(self.model) + "', '" + flights_sql + "', '" + str(self.taken) + "', '" + str(self.plane_id) + "', '" + airline_sql + "')")  #Adds a new row to the database in table planes

    def add_flights(self, flight_list):  # Add the flights the plane is going to take
        for flight in flight_list:
            if flight.flight_num == self.plane_id:
                self.flights.append(flight.destination)
        for flight in self.flights:
            cursor.execute(
                'INSERT INTO Planes VALUES (' + self.capacity + ', ' + self.manufacturer + ', ' + self.model + ', ' + flight + ', ' + self.taken + ', ' + self.plane_id + ', ' + self.Airline + ')')

