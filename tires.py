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
        for tirewear in self.tires:
            if tirewear >= self.worn_atleast_one:
                return True

class OctoprimeTires(Tires):
    def __init__(self):
        self.worn_all = 3
    def tires_should_be_serviced(self):
        sumwear = 0
        for tirewear in self.tires:
            sumwear += tirewear
        return sumwear >= self.worn_all