import Adafruit_PCA9685
from ESC_Configuration_Handler import ESC_Configuration_Handler

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
        pwm.setPWMFreq(freq)
    
    @classmethod
    def setPower(self, channel, percentPower):
        pwm = self.getPWM()
        tick = round(percentPower * 2)
        pwm.setPWM(channel, 0, tick)
    
    @classmethod
    def turnOffChannel(self, channel):
        pwm = self.getPWM()
        pwm.setPWM(channel, 0, 0)
    
    @classmethod
    def turnOffAllChannels(self):
        for channel in range (0, 16):
            self.turnOffChannel(channel)
        
        self.setPWMFreq(0)