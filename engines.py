from abc import ABC

class Engine(ABC):
	def __init__(self, current_mileage: int, last_service_mileage: int):
		self.current_mileage = current_mileage
		self.last_service_mileage = last_service_mileage
	
	def engine_should_be_serviced(self):
		return self.current_mileage - self.last_service_mileage
		
class CapuletEngine(Engine):
	def engine_should_be_serviced(self):
		return super().engine_should_be_serviced() > 30000
		
class WilloughbyEngine(Engine):
	def engine_should_be_serviced(self):
		return super().engine_should_be_serviced() > 60000

class SternmanEngine(Engine):
	def __init__(self, warning_light_is_on):
		self.warning_light_is_on = warning_light_is_on

	def engine_should_be_serviced(self):
		if self.warning_light_is_on:
			return True
		else:
			return False     
