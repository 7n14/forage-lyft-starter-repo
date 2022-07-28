from abc import  abstractmethod

from Serviceable import serviceable

class Car(serviceable):
    def __init__(self,engine,battery,current_date,last_service,current_mileage,last_service_mileage):
        super().__init__()
        self.engine = engine(last_service_mileage,current_mileage)
        self.battery = battery(last_service,current_date)

    def __init__(self,engine,battery,current_date,last_service,warning_light_on):
        super().__init__()
        self.engine = engine(warning_light_on)
        self.battery = battery(last_service,current_date)

    @abstractmethod
    def needs_service(self):
        pass
