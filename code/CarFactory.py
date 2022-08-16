from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, willoughby_engine, sternman_engine
from tires import carrigan_tires, octoprime_tires
from car import Car

class CarFactory():#This each method create a instances of a car object depending on the type of car being created
    def create_calliope(self,current_date,last_service_date,current_mileage,last_service_mileage,fl,fr,bl,br): #calliope: CapuletEngine spindler_battery carrigan_tires
        return Car(capulet_engine.CapuletEngine(current_mileage,last_service_mileage),spindler_battery.spindler_battery(last_service_date,current_date),carrigan_tires.carrigan_tires(fl,fr,bl,br))#f = front, b = back, l = left, r = right

    def create_lissade(self,current_date,last_service_date,current_mileage,last_service_mileage,fl,fr,bl,br): #lissade: WilloughbyEngine spindler_battery octoprime_tires
        return  Car(willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage),spindler_battery.spindler_battery(last_service_date,current_date),octoprime_tires.octoprime_tires(fl,fr,bl,br))

    def create_palindrome(self,current_date,last_service_date,warning_light_on,fl,fr,bl,br):#palindrome: SternmanEngine spindler_battery carrigan_tires
        return Car(sternman_engine.SternmanEngine(warning_light_on),spindler_battery.spindler_battery(last_service_date,current_date),carrigan_tires.carrigan_tires(fl,fr,bl,br))

    def create_rorschach(self,current_date,last_service_date,current_mileage,last_service_mileage,fl,fr,bl,br):#rorschach: WilloughbyEngine nubbin_battery octoprime_tires
        return Car(willoughby_engine.WilloughbyEngine(current_mileage,last_service_mileage),nubbin_battery.nubbin_battery(last_service_date,current_date),octoprime_tires.octoprime_tires(fl,fr,bl,br))

    def create_thovex(self,current_date,last_service_date,current_mileage,last_service_mileage,fl,fr,bl,br):#thovex: CapuletEngine nubbin_battery carrigan_tires
        return Car(capulet_engine.CapuletEngine(current_mileage,last_service_mileage),nubbin_battery.nubbin_battery(last_service_date,current_date),carrigan_tires.carrigan_tires(fl,fr,bl,br))