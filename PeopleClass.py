class People:  # people class
    def __init__(self, name):  # people class has defined attribute name
        self.name = name


class Passenger(People):        # passenger subclass of people

    __passenger_id = 0

    def __init__(self,name, destination):
        super().__init__(name)      # super to give subclass inheritance to main class
        self.__passport = ''
        self.__passenger_id += 1    # adds 1 to the defined passenger id
        Passenger.__passenger_id += 1   # continuously adds 1 to each new instance of a new passenger
        self.destination = destination


  # adds a way to add a passenger to the person
    def add_passport(self,passportnum): # adds a way to add a passport to the person
        self.__passport = passportnum
        return self.__passport


    def check_passport(self): # Returns the passport number
        return self.__passport


    def check_passenger(self): # returns the passenger id
        return self.__passenger_id

# Tests
# person_1 = Passenger('0', 'Bob')
# person_1.add_passport('312313')
# person_1.add_passenger('12441')
# print(person_1.check_passenger())

    def check_passenger(self):  # returns the passenger id
        return self.__passenger_id

    def add_passenger_to_flight(self,flight_list):  #Goes through list of flights to add passenger
        for flight in flight_list:
            if self.destination == flight.destination:
                flight.boarding_list.add_a_customer(self)
<<<<<<< HEAD
=======

#change

>>>>>>> 2d20bcd7e3c36ff1752d7aead39adb17e1eb504f
