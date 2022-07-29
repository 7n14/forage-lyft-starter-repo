from Serviceable import serviceable

class Car(serviceable):
    #This initializates car object that have engines that require mileage to be checked.
    def __init__(self,engine,battery,current_date,last_service,current_mileage,last_service_mileage):
        self.engine = engine(last_service_mileage,current_mileage)
        self.battery = battery(last_service,current_date)
    #This ilitlizes for car objects that use the sternman engine due to only needing a warning light
    def __init__(self,engine,battery,current_date,last_service,warning_light_on):
        self.engine = engine(warning_light_on)
        self.battery = battery(last_service,current_date)
    #Calls needs_service from engine and battery to see if either or both needs to be serviced
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
