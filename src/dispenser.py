from gpiozero import Motor
from gpiozero import PWMOutputDevice
import time
class Dispenser():
    nutrientdispensercapacity = 47# 47 based on measurement, 39 #ml in min according to manufacturer
    pooldispensercapacity = 1.5 #l in min
    def __init__(self):
        self.pooldispenser = Motor(17, 27,pwm=False)
        self.pooldispenserSpeed = PWMOutputDevice(13, active_high=True, initial_value=0, frequency=100, pin_factory=None)
        self.firstdispenser = Motor(9, 11,pwm=False)
        self.seconddispenser = Motor(22, 10,pwm=False)
        
    def dispenseFirstLiquid(self, amounttodispense):
        self.firstdispenser.forward()
        print("Dispensing first liquid %.2f" %amounttodispense)
        time.sleep(60*(amounttodispense / self.nutrientdispensercapacity))
        self.firstdispenser.stop()
        
    def dispenseSecondLiquid(self, amounttodispense):
        self.seconddispenser.forward()
        print("Dispensing second liquid %.2f" %amounttodispense)
        time.sleep(60*(amounttodispense / self.nutrientdispensercapacity))
        self.seconddispenser.stop()
    
    def stop(self):
        self.pooldispenser.stop()
        self.firstdispenser.stop()
        
    def dispensePoolLiters(self, amounttodispense):
        duration = (60 *(amounttodispense / self.pooldispensercapacity))
        self.pooldispenser.forward(speed=1.0)
        self.pooldispenserSpeed.value = 1.0
        self.pooldispenserSpeed.on()#blink(on_time=duration, off_time=0, fade_in_time=0.5, fade_out_time=0.5, n=1, background=False)
        self.pooldispenserSpeed.value = 1.0

        time.sleep(duration)
        self.pooldispenser.stop()

#dispenser = Dispenser()
#dispenser.stop()
#dispenser.dispensePoolLiters(1.0)
#dispenser.dispenseECML(20)