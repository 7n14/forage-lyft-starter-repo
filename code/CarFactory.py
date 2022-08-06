from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
from car import Car

class CarFactory():#This each method create a instances of a car object depending on the type of car being created
    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage): #calliope: CapuletEngine spindler_battery
        return Car(capulet_engine.CapuletEngine(current_mileage,last_service_mileage),spindler_battery.spindler_battery(last_service_date,current_date))

    def create_lissade(self,current_date,last_service_date,current_mileage,last_service_mileage): #lissade: WilloughbyEngine spindler_battery
        return  Car(willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage),spindler_battery.spindler_battery(last_service_date,current_date))

    def create_palindrome(self,current_date,last_service_date,warning_light_on):#palindrome: SternmanEngine spindler_battery
        return Car(sternman_engine.SternmanEngine(warning_light_on),spindler_battery.spindler_battery(last_service_date,current_date))

    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage):#rorschach: WilloughbyEngine nubbin_battery
        return Car(willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage),nubbin_battery.nubbin_battery(last_service_date,current_date))

    def create_thovex(self,current_date,last_service_date,current_mileage,last_service_mileage):#thovex: CapuletEngine nubbin_battery
        return Car(capulet_engine.CapuletEngine(current_mileage,last_service_mileage),nubbin_battery.nubbin_battery(last_service_date,current_date))