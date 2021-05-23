from gpiozero import Motor
import time
class Dispenser():
    nutrientdispensercapacity = 39 #ml in min
    pooldispensercapacity = 1.0 #l in min
    def __init__(self):
        self.pooldispenser = Motor(17, 27,pwm=False)
        self.phdispenser = Motor(22, 10,pwm=False)
        
    def dispensePHML(amounttodispense)
        self.phdispenser.forward()
        sleep(60*(amounttodispense / nutrientdispensercapacity))
        self.phdispenser.stop()
        
    def dispensePoolLiters(amounttodispense)
        self.pooldispenser.forward()
        sleep(60 *(amounttodispense / pooldispensercapacity))
        self.pooldispenser.stop()