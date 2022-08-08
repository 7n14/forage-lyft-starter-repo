import unittest
from datetime import datetime

from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
import car
import CarFactory


class test_nubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        test_battery = nubbin_battery.nubbin_battery(last_service_date,today)
        self.assertTrue(test_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        test_battery = nubbin_battery.nubbin_battery(last_service_date,today)
        self.assertFalse(test_battery.needs_service())


class test_spindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        test_battery = spindler_battery.spindler_battery(last_service_date,today)
        self.assertTrue(test_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        test_battery = spindler_battery.spindler_battery(last_service_date,today)
        self.assertFalse(test_battery.needs_service())


class test_capulet (unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        test_engine = capulet_engine.CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        test_engine = capulet_engine.CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(test_engine.needs_service())


class test_willoughby (unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        test_engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(test_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        test_engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(test_engine.needs_service())


class test_sternman (unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        test_engine = sternman_engine.SternmanEngine(warning_light_is_on)
        self.assertTrue(test_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        test_engine = sternman_engine.SternmanEngine(warning_light_is_on)
        self.assertFalse(test_engine.needs_service())


class test_car (unittest.TestCase):
    def test_car_should_be_serviced_1(self):#if service engine not battery
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 60001
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_be_serviced_2(self):#if service battery not engne
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 60000
        last_service_mileage = 0
        
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_be_serviced_3(self):#service both
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 60001
        last_service_mileage = 0
        
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_not_be_serviced(self):#None should be serviced
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 50000
        last_service_mileage = 0

        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery)
        self.assertFalse(test_car_var.needs_service())

if __name__ == '__main__':
    unittest.main()