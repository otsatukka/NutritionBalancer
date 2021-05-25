from gpiozero import Motor
from gpiozero import PWMOutputDevice
import time
class Dispenser():
    nutrientdispensercapacity = 39 #ml in min
    pooldispensercapacity = 1.0 #l in min
    def __init__(self):
        self.pooldispenser = Motor(17, 27,pwm=True)
        self.pooldispenserSpeed = PWMOutputDevice(13, active_high=True, initial_value=0, frequency=100, pin_factory=None)
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
        duration = (60 *(amounttodispense / self.pooldispensercapacity))
        self.pooldispenserSpeed.on()#blink(on_time=0, off_time=0, fade_in_time=0.5, fade_out_time=0.5, n=int(duration), background=False)
        self.pooldispenserSpeed.value = 0.4
        time.sleep(duration)
        self.pooldispenser.stop()

dispenser = Dispenser()
#dispenser.stop()
dispenser.dispensePoolLiters(0.1)
#dispenser.dispenseECML(2)