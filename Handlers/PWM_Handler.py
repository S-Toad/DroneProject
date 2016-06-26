import Adafruit_PCA9685
from ESC_Configuration_Handler import ESC_Configuration_Handler
from time import sleep

#TODO: Make an instance of this class and pass it around?

class PWM_Handler():

    debug = False
    
    @classmethod
    def getPWM(self):
        pwm = Adafruit_PCA9685.PCA9685()
        return pwm
        
    @classmethod
    def intializePWMFreq(self):
        freq = ESCConfigurationHandler.returnPulseHertz()
        self.setPWMFreq(freq)
        
        if debug:
            print("PWM frequency is set at: " + freq)
            
    
    @classmethod
    def setPWMFreq(self, freq):
        pwm = self.getPWM()
        pwm.set_pwm_freq(freq)
        
        if debug:
            print("PWM frequency is set at " + freq + " Hz.")
    
    @classmethod
    def setPower(self, channel, percentPower):
        pwm = self.getPWM()
        tick = int(round(percentPower * 2))
        pwm.set_pwm(channel, 0, tick)
        
        if debug:
            print("Channel " + channel + " was set at " + percentPower + ".")
    
    @classmethod
    def turnOffChannel(self, channel):
        pwm = self.getPWM()
        pwm.set_pwm(channel, 0, 0)
        
        if debug:
            print("Channel " + channel + " was turned off.")
    
    @classmethod
    def turnOff(self):
        pwm = self.getPWM()
        pwm.set_all_pwm(0, 0)
        sleep(0.5)
        self.setPWMFreq(0)
        
        if debug:
            print("PWM Servo Driver was turned off.")