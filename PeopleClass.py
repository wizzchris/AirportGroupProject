import pyodbc       # to use database methods

server = 'localhost,1433'
databse = 'AirportGroupProject'
username = 'SA'
password = 'Passw0rd2018'
# Connection object of db
docker_connect = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + databse + ';UID=' + username +
    ';PWD=' + password)         # connecting to Microsoft SQL Server
cursor = docker_connect.cursor()    # created cursor which will run commands on SQL through python

class People:  # people class

    def __init__(self, name):  # people class method which is called when memory is allocated to new object
        self.name = name

class Passenger(People):  # passenger subclass of people


    __passenger_id = 0

    def __init__(self, name, destination):
        super().__init__(name)  # super to give subclass inheritance to main class
        self.__passport = ''
        self.destination = destination
        __passport_sql = 'Null'

        self.__passenger_id_id = 'A-P-' + str(Passenger.__passenger_id)

        Passenger.__passenger_id += 1   # continuously adds 1 to each new instance of a new passenger making it unique
        self.destination = destination

        Passenger.__passenger_id += 1   # continuously adds 1 to each new instance of a new passenger


        cursor.execute("INSERT INTO Customers VALUES "
                       "('" + str(self.name) + "', '" + str(self.destination) + "',  " + __passport_sql + ", + '" +
                       str(self.__passenger_id) + "')")     # executing code to SQL
        docker_connect.commit()

    # Methods

    def add_passport(self,passportnum): # adds a way to add a passport to the person
        self.__passport = passportnum
        return self.__passport

    def check_passport(self): # Returns the passport number
        return self.__passport

    def check_passport(self):  # Returns the passport number
        return self.__passport

    def check_passenger(self):  # returns the passenger id
        return self.__passenger_id


    def check_passenger(self):  # returns the passenger id
        return self.__passenger_id

    def add_passenger_to_flight(self, flight_list):  # Goes through list of flights to add passenger
        for flight in flight_list:
            if self.destination == flight.destination:
                flight.boarding_list.add_a_customer(self)

