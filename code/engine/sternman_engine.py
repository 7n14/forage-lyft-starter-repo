from engine.engine import engine

class SternmanEngine(engine):
    def __init__(self,warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
