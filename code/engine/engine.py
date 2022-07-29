from abc import abstractmethod

class engine():
    #Two sperate initialization for the 2 different types of engines, one require tracking of mileage and the other a warning light
    def __init__(self, current_mileage,last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
    
    def __init__(self,warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    @abstractmethod#To makes sure every engine subclass has needs_service otherwise car object wont work
    def needs_service(self):
        pass