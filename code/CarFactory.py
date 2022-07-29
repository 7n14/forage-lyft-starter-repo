from battery import nubbin_battery, spindler_battery
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from car import Car

class CarFactory():#This each method create a instances of a car object depending on the type of car being created
    def create_calliope(self,current_date,last_service,current_mileage,last_service_mileage): #calliope: CapuletEngine spindler_battery
        return Car(CapuletEngine,spindler_battery,current_date,last_service,current_mileage,last_service_mileage)

    def create_lissade(self,current_date,last_service,current_mileage,last_service_mileage): #lissade: WilloughbyEngine spindler_battery
        return  Car(WilloughbyEngine,spindler_battery,current_date,last_service,current_mileage,last_service_mileage)

    def create_palindrome(self,current_date,last_service,warning_light_on):#palindrome: SternmanEngine spindler_battery
        return Car(SternmanEngine,spindler_battery,current_date,last_service,warning_light_on)

    def create_rorschach(self,current_date,last_service,current_mileage,last_service_mileage):#rorschach: WilloughbyEngine nubbin_battery
        return Car(WilloughbyEngine,nubbin_battery,current_date,last_service,current_mileage,last_service_mileage)

    def create_thovex(self,current_date,last_service,current_mileage,last_service_mileage):#thovex: CapuletEngine nubbin_battery
        return Car(CapuletEngine,nubbin_battery,current_date,last_service,current_mileage,last_service_mileage)