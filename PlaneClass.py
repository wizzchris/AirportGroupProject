"""
Adds a class called plane
"""

class Plane:
    Plane_id = 0  # Starts the id convention

    def __init__(self, capacity, flights=None, taken='no'):  # Initialises class with capacity

        self.capacity = capacity
        self.plane_id = 'A-P-' + str(Plane.Plane_id)  # Adds the plane id
        Plane.Plane_id += 1  # Adds 1 to the id after creation
        self.Airline = ''  # Allows the plane class to have airline
        if flights is None:
            flights = []
        self.flights = []
        self.taken = taken  # Check to see if plane is taken on a flight
