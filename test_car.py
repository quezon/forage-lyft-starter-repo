import sys
import unittest
from datetime import datetime
from car_factory import CarFactory

class TestCalliope(unittest.TestCase):
    def setUp(self):
        self.carFactory = CarFactory()

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = self.carFactory.create_calliope(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = self.carFactory.create_calliope(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
    def setUp(self):
        self.carFactory = CarFactory()

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_glissade(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_glissade(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = self.carFactory.create_glissade(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = self.carFactory.create_glissade(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.carFactory = CarFactory()

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False

        car = self.carFactory.create_palindrome(current_date,last_service_date,warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_is_on = False

        car = self.carFactory.create_palindrome(current_date,last_service_date,warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = self.carFactory.create_palindrome(last_service_date,last_service_date,warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = self.carFactory.create_palindrome(last_service_date,last_service_date,warning_light_is_on)
        self.assertFalse(car.needs_service())

class TestRorschach(unittest.TestCase):
    def setUp(self):
        self.carFactory = CarFactory()

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = self.carFactory.create_rorschach(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = self.carFactory.create_rorschach(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    def setUp(self):
        self.carFactory = CarFactory()
        
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_thovex(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = self.carFactory.create_thovex(current_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = self.carFactory.create_thovex(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = self.carFactory.create_thovex(last_service_date,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
