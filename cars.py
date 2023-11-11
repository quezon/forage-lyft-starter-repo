import abc

class Serviceable(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'needs_service') and 
                callable(subclass.needs_service))

class Car():
	def __init__(self, engine, battery, name):
		self.engine = engine
		self.battery = battery
		self.name = name

	def needs_service(self):
		if self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced():
			return True
		else:
			return False
