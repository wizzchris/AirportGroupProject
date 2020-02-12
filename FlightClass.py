""""
Adds a class called flight
"""""

class Flight:

    def __init__(self,flight_num, airline, destination, date_time, boarding_list= None, origin='London'):  #Starts class with flight number, airline, destination and date time. Allows for future creation of boarding list and origin
        self.flight_num = flight_num
        self.airline = airline
        self.destination = destination
        self.date_time = date_time
        if boarding_list == None:  #Allows change to empty list if boarding list is empty
            boarding_list = []
        self.boarding_list = boarding_list
        self.origin = origin
        self.plane_name = 'No Name Assigned'

    def add_customers(self,customer_list):  #Starts a class method which adds multiple customers as a list
        self.boarding_list.extend(customer_list)

    def add_a_customer(self,customer):  #Adds a customer to the boarding list, only one customer
        self.boarding_list.append(customer)

    def add_plane(self,plane_name_provided):
        self.plane_name = plane_name_provided