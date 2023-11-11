from datetime import date
from cars import Car

from engines import CapuletEngine, WilloughbyEngine, SternmanEngine
from batteries import SpindlerBattery, NubbinBattery

class CarFactory:
	def __init__(self):
		pass

	def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
		engine = CapuletEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(current_date, last_service_date)

		return Car(engine, battery, "Calliope")

	def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(current_date, last_service_date)

		return Car(engine, battery, "Glissade")

	def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
		engine = SternmanEngine(warning_light_on)
		battery = SpindlerBattery(current_date, last_service_date)

		return Car(engine, battery, "Palindrome")

	def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(current_date, last_service_date)

		return Car(engine, battery, "Rorschach")

	def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
		engine = CapuletEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(current_date, last_service_date)

		return Car(engine, battery, "Thovex")