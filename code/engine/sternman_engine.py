from engine.engine import engine

class SternmanEngine(engine):
    def __init__(self,warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):#Needs service when the warning light is on
        #The if statment that was orginally here was not need as stating the obvious, when true return true 
        return self.warning_light_is_on