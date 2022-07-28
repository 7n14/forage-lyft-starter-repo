from abc import abstractmethod

class serviceable():
    @abstractmethod
    def needs_service(self):
        pass