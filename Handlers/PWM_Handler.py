import Adafruit_PCA9685
from ESC_Configuration_Handler import ESC_Configuration_Handler
from time import sleep

#TODO: Make an instance of this class and pass it around?

class PWM_Handler():
    
    @classmethod
    def getPWM(self):
        pwm = Adafruit_PCA9685.PCA9685()
        return pwm
        
    @classmethod
    def intializePWMFreq(self):
        freq = ESCConfigurationHandler.returnPulseHertz()
        self.setPWMFreq(freq)
    
    @classmethod
    def setPWMFreq(self, freq):
        pwm = self.getPWM()
        pwm.set_pwm_freq(freq)
    
    @classmethod
    def setPower(self, channel, percentPower):
        pwm = self.getPWM()
        tick = int(round(percentPower * 2))
        pwm.set_pwm(channel, 0, tick)
    
    @classmethod
    def turnOffChannel(self, channel):
        pwm = self.getPWM()
        pwm.set_pwm(channel, 0, 0)
    
    @classmethod
    def turnOff(self):
        pwm = self.getPWM()
        pwm.set_all_pwm(0, 0)
        sleep(0.5)
        self.setPWMFreq(0)