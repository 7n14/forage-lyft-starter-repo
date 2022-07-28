from abc import  abstractmethod

from Serviceable import serviceable

class Car(serviceable):
    def __init__(self,engine,battery,current_date,last_service,current_mileage,last_service_mileage):
        self.engine = engine(last_service_mileage,current_mileage)
        self.battery = battery(last_service,current_date)

    def __init__(self,engine,battery,current_date,last_service,warning_light_on):
        self.engine = engine(warning_light_on)
        self.battery = battery(last_service,current_date)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
