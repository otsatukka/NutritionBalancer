import time
from dispenser import Dispenser
from makemeasurements import Measurements
class NutritionBalancer():
    poolvolume = 1.0 # in liters
    hydroponictankvolume = 10 # in liters
    ecsolutionconcentration = 3 # salinity in mV
    targetPh = 7.0
    targetEc = 0.5
    
    def __init__(self):
        self.dispenser = Dispenser()
        self.measurer = Measurements() 
    
    def control(self):
        fillPool()
        nutrientNeedEc, phCalibSolutionNeeded = determineNutrientNeed()
        self.dispenser.dispenseECML(nutrientNeedEc*1000)
        
        
    def fillPool(self):
        self.dispenser.dispensePoolLiters(poolvolume*1.5) # Over fill
        
    def determineNutrientNeed(self):
        nutrientNeedEc = 0
        phCalibSolutionNeeded = 0 
        humidity, airtemp, watertemp, orp, ph, ec = measurer.makeMeasurements()
        if (ec < targetEc):
            volumeFactor = hydroponictankvolume / poolvolume
            volumetopool = poolvolume / ( ( ecsolutionconcentration - targetEc ) / ( targetEc - ec ) )
            nutrientNeedEc = volumetopool*volumeFactor
        if (ph < targetPh):
            print("Calculate PH balancing")
        return nutrientNeedEc,phCalibSolutionNeeded