from tires.tires import tires

class octoprime_tires(tires):
    def __init__(self,fl,fr,bl,br) -> None:#f = front, b = back, l = left, r = right
        self.tires = [fl,fr,bl,br]
    
    def needs_service(self):
        temp = 0
        for i in self.tires:#Loops through all the tires and adds the wear to temp for checking if they equal or more than 3
            temp += i
        if temp >= 3:
            return True
        else:
            return False