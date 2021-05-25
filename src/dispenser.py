from gpiozero import Motor
import time
class Dispenser():
    nutrientdispensercapacity = 39 #ml in min
    pooldispensercapacity = 1.0 #l in min
    def __init__(self):
        self.pooldispenser = Motor(17, 27,pwm=False)
        self.ecdispenser = Motor(22, 10,pwm=False)
        
    def dispenseECML(self, amounttodispense):
        self.ecdispenser.forward()
        time.sleep(60*(amounttodispense / self.nutrientdispensercapacity))
        self.ecdispenser.stop()
    
    def stop(self):
        self.pooldispenser.stop()
        self.ecdispenser.stop()
        
    def dispensePoolLiters(self, amounttodispense):
        self.pooldispenser.forward()
        time.sleep(60 *(amounttodispense / self.pooldispensercapacity))
        self.pooldispenser.stop()

dispenser = Dispenser()
dispenser.stop()
#dispenser.dispensePoolLiters(0.1)
#dispenser.dispenseECML(2)