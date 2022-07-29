from engine.engine import engine

class CapuletEngine(engine):
    def __init__(self, current_mileage,last_service_mileage):
        super.__init__(self,current_mileage,last_service_mileage)

    def needs_service(self):#Needs service every 30,000 miles
        return self.current_mileage - self.last_service_mileage > 30000