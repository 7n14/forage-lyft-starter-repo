

from tires.tires import tires

class carrigan_tires(tires):
    def __init__(self,fl,fr,bl,br):#f = front, b = back, l = left, r = right
        self.tires = [fl,fr,bl,br]
    
    def needs_service(self):
        serivce = False
        for i in self.tires:#goes through each tire to each if any are at 0.9 or worse tire wear if so then the car needs to be serviced
            if i >= 0.9:
                serivce = True
        return serivce