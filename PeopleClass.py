class People:  # people class
    def __init__(self, name):  # people class has defined attribute name
        self.name = name


class Passenger(People):  # passenger subclass of people
    __passenger_counter = 0

    def __init__(self, name, __passport):
        super().__init__(name)  # super to give subclass inheritance to main class
        self.__passport = __passport
        self.__passenger_id = Passenger.__passenger_counter  # adds 1 to the defined passenger id
        Passenger.__passenger_counter += 1  # continuously adds 1 to each new instance of a new passenger

  # adds a way to add a passenger to the person
    def add_passport(self,passportnum): # adds a way to add a passport to the person
        self.__passport = passportnum
        return self.__passport

    def add_passenger(self, passengernum): # adds a way to add a passenger to the person
        self.__passenger_id = passengernum
        return passengernum

    def check_passport(self):  # Returns the passport number
        return self.__passport

    def check_passenger(self):  # returns the passenger id
        return self.__passenger_id

