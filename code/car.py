from Serviceable import serviceable

class Car(serviceable):
    #This initializates car object 
    def __init__(self,engine,battery,tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
   
    #Calls needs_service from engine and battery to see if either or both needs to be serviced
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
