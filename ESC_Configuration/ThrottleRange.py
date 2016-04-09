from Adafruit_PWM_Servo_Driver import PWM
import time

'''
This code should be ran with any new ESC (Electronic Speed Controllers) to configure them to the correct parameters.
Below are parameters that 'you' are able to change to fit with your ideal specifications.
Default settings

A typical ESC will take 20ms (50hz) pulses. In those pulses, 1 ms of being on will be considered the bottom range of your throttle, while 2 is considered the high end.
These values are changeble.

These are in Adafruits ticks, (0-4095). Where 1 tick is pulseHertz/4095
For 50hz, 1ms is about ~205
The default range will be from 200-400 (~0.98ms - ~1.95ms), where each tick is about +0.5% power. 
'''

pulseHertz = 50
bottomTickRange = 200
upperTickRange = 400

channel = raw_input("Enter the ESC channel: ")

pwm = PWM(0x40)
pwm.setPWMFreq(pulseHertz)

pwm.setPWM(channel, 0, upperTickRange)
print "Running high throttle..."
raw_input("Connect battery and hit any key after hearing 2 beeps...")

pwm.setPWM(channel, 0, bottomTickRange)
print "Running low throttle..."
raw_input("Hit any key after all the beeps...")

print "Running at 50% for a short period"
pwm.setPWM(channel, 0, 300)
time.sleep(3)


print "The ESC on channel " + str(channel) + " is set!"
