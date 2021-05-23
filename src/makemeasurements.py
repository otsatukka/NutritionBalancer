from SHT20 import SHT20

class Measurements():
    def __init__(self):
        self.sht = SHT20(bus=1)
        
    def measurePH(self):
        print("PH")
    def measureEC(self):
        print("PH")
    def measureORP(self):
        print("PH")
    def measureWaterTemp(self):
        print("PH")
    def measureAirTemp(self):
        print("PH")
    def measureHumidity(self):
        print("PH")

meas = Measurements()
meas.measureEC()