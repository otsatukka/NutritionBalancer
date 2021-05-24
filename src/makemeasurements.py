from SHT20 import SHT20
from uFire_EC import uFire_EC
from uFire_pH import uFire_pH
from uFire_ORP import ufire_orp

class Measurements():
    def __init__(self):
        self.sht = SHT20(bus=1)
        self.ec = uFire_EC(i2c_bus=1)
        self.ph = uFire_pH(i2c_bus=1)
        self.orp = ufire_orp(address=0x2f, i2c_bus=1)
        
    def measurePH(self):
        self.ph.measurepH()
        print("mV: " + str(self.ph.mV))
        print("pH: " + str(self.ph.pH))
        print("pOH: " + str(self.ph.pOH))
        
    def measureEC(self):
        self.ec.measureEC()
        print("EC mS: " + str(self.ec.mS))
        
    def measureORP(self):
        self.orp.measureORP()
        print("mV: " + str(self.orp.mV))
        print("Eh: " + str(self.orp.Eh))

    def measureWaterTemp(self):
        print("Water temp %.2f" %self.ec.measureTemp())
        
    def measureAirTemp(self):
        print("Air temp %.2f" %self.sht.temperature())
        
    def measureHumidity(self):
        print("Humidity %.2f" %self.sht.humidity())
    
    def makeMeasurements(self):
        humidity = self.measureHumidity()
        airtemp = 0#self.measureAirTemp()
        watertemp = self.measureWaterTemp()
        orp = self.measureORP()
        ph = self.measurePH()
        ec = self.measureEC()
        return humidity, airtemp, watertemp, orp, ph, ec
        
meas = Measurements()
meas.makeMeasurements()