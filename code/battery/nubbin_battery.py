import datetime
from battery.battery import battery

class nubbin_battery (battery):
    def __init__(self,last_service_date,current_date) -> None:
        super.__init__(self,last_service_date,current_date)

    def needs_service(self):#Needs service every 4 years
        return datetime.timedelta(self.last_service_date,self.current_date)>=datetime.date.year(4)
    