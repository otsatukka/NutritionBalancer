from SHT20 import SHT20
from uFire_EC import uFire_EC
from uFire_pH import uFire_pH
from uFire_ORP import uFire_ORP

class Measurements():
    def __init__(self):
        self.sht = SHT20(bus=1)
        self.ec = uFire_EC(i2c_bus=1)
        self.ph = uFire_pH(bus=1)
        self.orp = uFire_ORP(bus=1)
        
    def measurePH(self):
        self.ph.measurepH()
        print("mV: " + str(ph.mV))
        print("pH: " + str(ph.pH))
        print("pOH: " + str(ph.pOH))
        
    def measureEC(self):
        self.ec.measureEC()
        print("mS: " + str(ec.mS))
        
    def measureORP(self):
        self.orp.measureORP()
        print("mV: " + str(orp.mV))
        print("Eh: " + str(orp.Eh))

    def measureWaterTemp(self):
        print("Water temp %.2f" %self.ec.measureTemp())
        
    def measureAirTemp(self):
        print("Air temp %.2f" %self.sht.temperature())
        
    def measureHumidity(self):
        print("Humidity %.2f" %self.sht.humidity())

meas = Measurements()
meas.measureEC()