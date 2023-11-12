from abc import ABC
from datetime import date
from calendar import isleap
import math

class Battery(ABC):
	def __init__(self, current_date: date, last_service_date: date):
		self.current_date = current_date
		self.last_service_date = last_service_date
	
	def battery_should_be_serviced(self, years):
		return get_number_of_years_round_down(self.current_date, self.last_service_date) >= years
		# dyears = get_number_of_years_round_down(self.current_date, self.last_service_date)
		# return dyears % years == 0 and dyears != 0
		
	def change_dates(self, current_date: date):
		self.last_service_date = self.current_date
		self.current_date = current_date

class SpindlerBattery(Battery):
	def __init__(self, current_date, last_service_date):
		self.years = 3
		super(SpindlerBattery, self).__init__(current_date, last_service_date)

	def battery_should_be_serviced(self):
		return super().battery_should_be_serviced(self.years)
		
class NubbinBattery(Battery):
	def __init__(self, current_date, last_service_date):
		self.years = 4
		super(NubbinBattery, self).__init__(current_date, last_service_date)
		
	def battery_should_be_serviced(self):
		return super().battery_should_be_serviced(self.years)
		
def get_number_of_years_round_down(to_date,from_date):
	diffyears = to_date.year - from_date.year
	difference  = to_date - from_date.replace(to_date.year)
	days_in_year = isleap(to_date.year) and 366 or 365
	difference_in_years = diffyears + (difference.days + difference.seconds/86400.0)/days_in_year
	return math.floor(difference_in_years)
	
