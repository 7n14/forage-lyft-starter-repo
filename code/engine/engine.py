from abc import abstractmethod

class engine():
    
    @abstractmethod#To makes sure every engine subclass has needs_service otherwise car object wont work
    def needs_service(self):
        pass