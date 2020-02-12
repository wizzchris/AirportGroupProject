

class Plane:
    Plane_id = 0

    def __init__(self,capacity):

        self.capacity = capacity
        self.plane_id = 'A-P-' + str(Plane.Plane_id)
        Plane.Plane_id += 1
        self.Airline = ''
