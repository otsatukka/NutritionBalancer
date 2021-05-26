import time
from dispenser import Dispenser
from makemeasurements import Measurements
class NutritionBalancer():
    poolvolume = 1.0 # in liters
    hydroponictankvolume = 10 # in liters
    ecsolutionconcentration = 50 # salinity in mS
    targetPh = 7.0
    targetEc = 0.7
    
    def __init__(self):
        self.dispenser = Dispenser()
        self.measurer = Measurements() 
    
    def control(self):
        fillPool()
        ecNutrientNeeded, phCalibSolutionNeeded = determineNutrientNeed()
        self.dispenser.dispenseECML(ecNutrientNeeded*1000)
        dispensepool()
                
    def fillPool(self):
        self.dispenser.dispensePoolLiters(self.poolvolume*1.5) # Over fill
        
    def dispensepool(self):
        self.dispenser.dispensePoolLiters(self.poolvolume*2.0) # Over empty
        
    def determineNutrientNeed(self):
        ecNutrientNeeded = 0
        phCalibSolutionNeeded = 0 
        humidity, airtemp, watertemp, orp, ph, ec = self.measurer.makeMeasurements()
        if (ec < self.targetEc):
            volumeFactor = self.hydroponictankvolume / self.poolvolume
            volumetopool = self.poolvolume / ( ( self.ecsolutionconcentration - self.targetEc ) / ( self.targetEc - ec ) )
            ecNutrientNeeded = volumetopool*volumeFactor
        if (ph < self.targetPh):
            print("Calculate PH balancing")
        return ecNutrientNeeded, phCalibSolutionNeeded
    
    def stopPumps(self):
        self.dispenser.stop()
    def getEC(self):
        return self.measurer.measureEC()
#nb = NutritionBalancer()
#ecNutrientNeeded, phCalibSolutionNeeded = nb.determineNutrientNeed()
#print("EC solution needed %.2f"%(ecNutrientNeeded*1000))
