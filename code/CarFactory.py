from battery.nubbin_battery import nubbin_battery
from battery.spindler_battery import spindler_battery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory():
    def create_calliope(self,current_date,last_service,current_mileage,last_service_mileage):
        return Car(CapuletEngine,spindler_battery,current_date,last_service,current_mileage,last_service_mileage)

    def create_lissade(self,current_date,last_service,current_mileage,last_service_mileage):
        return  Car(WilloughbyEngine,spindler_battery,current_date,last_service,current_mileage,last_service_mileage)

    def create_palindrome(self,current_date,last_service,warning_light_on):
        return Car(SternmanEngine,spindler_battery,current_date,last_service,warning_light_on)

    def create_rorschach(self,current_date,last_service,current_mileage,last_service_mileage):
        return Car(WilloughbyEngine,nubbin_battery,current_date,last_service,current_mileage,last_service_mileage)

    def create_thovex(self,current_date,last_service,current_mileage,last_service_mileage):
        return Car(CapuletEngine,nubbin_battery,current_date,last_service,current_mileage,last_service_mileage)