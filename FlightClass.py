
class Flight:
    def __init__(self,flight_num, airline, destination, date_time, boarding_list=[], origin='London'):
        self.flight_num = flight_num
        self.airline = airline
        self.destination = destination
        self.date_time = date_time
        self.boarding_list = boarding_list
        self.origin = origin

    def add_customers(self,customer_list):
        self.boarding_list.extend(customer_list)

    def add_a_customer(self,customer):
        self.boarding_list.append(customer)