from abc import abstractmethod

class serviceable():
    #This abstract to make sure that every object that inherits from the class has a needs_service object
    @abstractmethod
    def needs_service(self):
        pass