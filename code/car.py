from Serviceable import serviceable

class Car(serviceable):
    #This initializates car object 
    def __init__(self,engine,battery):
        self.engine = engine
        self.battery = battery
   
    #Calls needs_service from engine and battery to see if either or both needs to be serviced
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
