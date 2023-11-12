from abc import ABC

class Tires(ABC):
    def __init__(self, tires):
        self.tires = tires
    def tires_should_be_serviced(self):
        pass

class CarriganTires(Tires):
    def __init__(self):
        self.worn_atleast_one = 0.9
    def tires_should_be_serviced(self):
        for tire_wear in self.tires:
            if tire_wear >= self.worn_atleast_one:
                return True
        return False

class OctoprimeTires(Tires):
    def __init__(self):
        self.worn_all = 3
    def tires_should_be_serviced(self):
        return sum(self.tires) >= self.worn_all