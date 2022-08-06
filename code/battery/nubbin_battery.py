from battery.battery import battery
from utils import add_years_to_date

class nubbin_battery (battery):
    def __init__(self,last_service_date,current_date) -> None:
        #super.__init__(self,last_service_date,current_date)
        super(nubbin_battery, self).__init__(last_service_date,current_date)

    def needs_service(self):#Needs service every 4 years
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
    