from hashlib import new
import unittest
from datetime import datetime

from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
from tires import carrigan_tires, octoprime_tires
import car



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
        last_service_date = today.replace(year=today.year - 4)

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
        new_tires = carrigan_tires.carrigan_tires(0.87,0.82,0.89,0.79)
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery,new_tires)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_be_serviced_2(self):#if service battery not engne
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 60000
        last_service_mileage = 0
        new_tires = carrigan_tires.carrigan_tires(0.87,0.82,0.89,0.79)
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery,new_tires)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_be_serviced_3(self):#service all
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 60001
        last_service_mileage = 0
        new_tires = carrigan_tires.carrigan_tires(0.92,0.89,0.91,0.86)
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery,new_tires)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_be_serviced_4(self):#service only tires
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 50000
        last_service_mileage = 0
        new_tires = carrigan_tires.carrigan_tires(0.92,0.89,0.91,0.86)
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery,new_tires)
        self.assertTrue(test_car_var.needs_service())

    def test_car_should_not_be_serviced(self):#None should be serviced
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        current_mileage = 50000
        last_service_mileage = 0
        new_tires = carrigan_tires.carrigan_tires(0.87,0.82,0.89,0.79)
        engine = willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage)
        battery = spindler_battery.spindler_battery(last_service_date,current_date)
        
        test_car_var = car.Car(engine,battery,new_tires)
        self.assertFalse(test_car_var.needs_service())


class test_carrigan (unittest.TestCase):
    def test_tires_should_be_serviced(self):
        new_tires = carrigan_tires.carrigan_tires(0.92,0.89,0.91,0.86)
        self.assertTrue(new_tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        new_tires = carrigan_tires.carrigan_tires(0.87,0.82,0.89,0.79)
        self.assertFalse(new_tires.needs_service())

class test_octoprime (unittest.TestCase):
    def test_tires_should_be_serviced(self):
        new_tires = octoprime_tires.octoprime_tires(0.91,0.82,0.93,0.84)
        self.assertTrue(new_tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        new_tires = octoprime_tires.octoprime_tires(0.56,0.57,0.58,0.59)
        self.assertFalse(new_tires.needs_service())

if __name__ == '__main__':
    unittest.main()