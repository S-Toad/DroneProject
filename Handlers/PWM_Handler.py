import Adafruit_PCA9685
from escConfigurationHandler import ESC_Configuration_Handler

class PWM_Handler():
    
    def getPWM():
        pwm = Adafruit_PCA9685.PCA9685()
        return pwm
    
    def intializePWMFreq():
        pwm = PWM_Handler.getPWM()
        freq = ESCConfigurationHandler.returnPulseHertz()    
        pwm.setPWMFreq(freq)
    
    def setPWMFreq(freq):
        pwm = PWM_Handler.getPWM()   
        pwm.setPWMFreq(freq)
    
    def setPower(channel, percentPower):
        pwm = PWM_Handler.getPWM()
        tick = round(percentPower * 2)
        pwm.setPWM(channel, 0, tick)
    
    def turnOffChannel(channel):
        pwm = PWM_Handler.getPWM()
        pwm.setPWM(channel, 0, 0)
    
    def turnOffAllChannels():
        pwm = PWM_Handler.getPWM()
        for channel in range (0, 16):
            PWM_Handler.turnOffChannel(channel)
        
        PWM_Handler.setPWMFreq(0)