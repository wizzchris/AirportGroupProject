class People():     # people class
    def __init__(self, name):   # people class has defined attribute name
        self.name = name

class Passenger(People):        # passenger subclass of people

    __passenger_id = 0

    def __init__(self, __passport_no, __passenger_id, name):
        super().__init__(name)      # super to give subclass inheritance to main class
        self.__passport = __passport_no
        self.__passenger_id += 1    # adds 1 to the defined passenger id
        Passenger.__passenger_id += 1   # continuously adds 1 to each new instance of a new passenger

