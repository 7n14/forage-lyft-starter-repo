
from abc import abstractmethod

class tires():
    
    @abstractmethod#To makes sure every tires subclass has needs_service otherwise car object wont work
    def needs_service(self):
        pass