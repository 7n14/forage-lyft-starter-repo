import unittest
from datetime import datetime

from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
import car
import CarFactory


class test_nubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        pass

    def test_battery_should_not_be_serviced(self):
        pass


class test_spindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        pass

    def test_battery_should_not_be_serviced(self):
        pass


class test_capulet (unittest.TestCase):
    def test_engine_should_be_serviced(self):
        pass

    def test_engine_should_not_be_serviced(self):
        pass


class test_willoughby (unittest.TestCase):
    def test_engine_should_be_serviced(self):
        pass

    def test_engine_should_not_be_serviced(self):
        pass


class test_sternman (unittest.TestCase):
    def test_engine_should_be_serviced(self):
        pass

    def test_engine_should_not_be_serviced(self):
        pass


class test_car (unittest.TestCase):
    def test_init_ilitlizes_correctly_1(self):
        pass

    def test_init_ilitlizes_correctly_2(self):
        pass

    def test_car_should_be_serviced_1(self):#if service engine not battery
        pass

    def test_car_should_be_serviced_2(self):#if service battery not engne
        pass

    def test_car_should_be_serviced_3(self):#service both
        pass

    def test_car_should_not_be_serviced(self):
        pass


class test_factory (unittest.TestCase):
    def test_create_calliope(self):
        pass

    def create_lissade(self):
        pass

    def create_palindrome(self):
        pass

    def create_rorschach(self):
        pass

    def create_thovex(self):
        pass
