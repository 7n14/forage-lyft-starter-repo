from engine.engine import engine

class WilloughbyEngine(engine):
    def __init__(self, current_mileage,last_service_mileage):
        super.__init__(self,current_mileage,last_service_mileage)

    def needs_service(self):#Needs to be service every 60,000 miles
        return self.current_mileage - self.last_service_mileage > 60000