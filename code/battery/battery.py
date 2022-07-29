from abc import abstractmethod

class battery():
    #The initialization is here due to reducing repating code in the subclasses
    def __init__(self,last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    @abstractmethod#To makes sure every battery subclass has needs_service otherwise car object wont work
    def needs_service(self):
        pass