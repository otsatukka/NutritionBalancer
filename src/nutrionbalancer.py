import time
from dispenser import Dispenser
from makemeasurements import Measurements
class NutritionBalancer():
    
    def __init__(self):
        self.dispenser = Dispenser()
        self.measurer = Measurements() 
    def measureValues(self):
        