import Adafruit_PCA9685
from ESC_Configuration_Handler import ESC_Configuration_Handler
from time import sleep

class PWMHandler():
    
    def __init__(self, escConfigHandler):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.escConfigHandler = escConfigHandler
        
    def intializePWMFreq(self):
        freq = self.escConfigHandler.returnPulseHertz()
        self.setPWMFreq(freq)
            
    def setPWMFreq(self, freq):
        self.pwm.set_pwm_freq(freq)
    
    def setPower(self, channel, percentPower):
        tick = int(round(percentPower * 2))
        self.pwm.set_pwm(channel, 0, tick)
    
    def turnOffChannel(self, channel):
        self.pwm.set_pwm(channel, 0, 0)
    
    def turnOff(self):
        self.pwm.set_all_pwm(0, 0)
        sleep(0.5)
        self.setPWMFreq(0)