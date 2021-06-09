import time
from dispenser import Dispenser
from makemeasurements import Measurements
class NutritionBalancer():
    poolvolume = 1.0 # in liters
    hydroponictankvolume = 4 # in liters
    ecsolutionconcentration = 160.0 # salinity in mS
    targetPh = 6.3
    targetEc = 1.2
    
    def __init__(self):
        self.dispenser = Dispenser()
        self.measurer = Measurements() 
        
    def fillPool(self):
        self.dispenser.dispensePoolLiters(self.poolvolume*1.5) # Over fill
        
    def dispensepool(self):
        self.dispenser.dispensePoolLiters(self.poolvolume*2.0) # Over empty
        
    def determineNutrientNeed(self):
        ecNutrientNeeded = 0
        phCalibSolutionNeeded = 0 
        humidity, airtemp, watertemp, orp, ph, ec = self.measurer.makeMeasurements()
        if (ec < 0):
            ec = 0
        if (ec < self.targetEc):
            volumeFactor = self.hydroponictankvolume / self.poolvolume
            volumetopool = self.poolvolume / ( ( self.ecsolutionconcentration - self.targetEc ) / ( self.targetEc - ec ) )
            ecNutrientNeeded = volumetopool*volumeFactor
        if (ph < self.targetPh):
            print("Calculate PH balancing")
        
        return ecNutrientNeeded, phCalibSolutionNeeded
    
    def control(self):
        self.dispenser.dispensePoolLiters(self.poolvolume * 1.5)
        ecNutrientNeeded, phCalibSolutionNeeded = self.determineNutrientNeed()
        
        # dispense and mix the first liquid
        self.dispenser.dispenseFirstLiquid(ecNutrientNeeded * 1000 / 2)
        
        if (ecNutrientNeeded > 0 or phCalibSolutionNeeded > 0): 
            self.dispenser.dispensePoolLiters(self.poolvolume * 2.0) # Over empty
            
        # dispense and mix the second liquid
        self.dispenser.dispenseSecondLiquid(ecNutrientNeeded * 1000 / 2)
        
        if (ecNutrientNeeded > 0 or phCalibSolutionNeeded > 0): 
            self.dispenser.dispensePoolLiters(self.poolvolume * 2.0) # Over empty
        
    def stopPumps(self):
        self.dispenser.stop()
    def getOrp(self):
        return self.measurer.measureORP()
    def getPh(self):
        return self.measurer.measurePH()
    def getEC(self):
        return self.measurer.measureEC()
    def getWaterTemperature(self):
        return self.measurer.measureWaterTemp()
    
    
#nb = NutritionBalancer()
#nb.fillPool()
#nb.getWaterTemperature()
#nb.control()
#ecNutrientNeeded, phCalibSolutionNeeded = nb.determineNutrientNeed()
#print("EC solution needed %.2f"%(ecNutrientNeeded*1000))
