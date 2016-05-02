from Adafruit_PWM_Servo_Driver import PWM
import time

'''
This code should be ran with any new ESC (Electronic Speed Controllers) to configure them to the correct parameters.
Below are parameters that 'you' are able to change to fit with your ideal specifications.

A typical ESC will take 20ms (50hz) pulses. In those pulses, 1 ms of being on will be considered the bottom range of your throttle, while 2 is considered the high end.
These values are changeble.

These are in Adafruits ticks, (0-4095). Where 1 tick is pulseHertz/4095
For 50hz, 1ms is about ~205
The default range will be from 200-400 (~0.98ms - ~1.95ms), where each tick is about +0.5% power. 
'''

# These are configurations the user is able to change
# ToDo: Have all configurations available in a seperate config file at root of repo
pulseHertz = 50
bottomTickRange = 200
upperTickRange = 400

# This takes the raw input from the user and sorts into a list of integers to use.
channel_list = map(int,raw_input("Enter the ESC channel(s), (Example: 12 13 14 15): "))

# This sets the address and frequency the adafruit servo driver will use
pwm = PWM(0x40)
pwm.setPWMFreq(pulseHertz)

# We iterate through each of the channels and set them to run at the upper range
for channel in channel_list:
    pwm.setPWM(channel, 0, upperTickRange)
raw_input("Connect battery and hit any key after hearing 2 beeps...")

# We iterate through each of the channels and set them to run at the lower range
for channel in channel_list:
    pwm.setPWM(channel, 0, bottomTickRange)
raw_input("Hit any key after all the beeps...")
# TODO: Use time.sleep() for ease^

print "Will run at 5% for a short period"
time.sleep(3)

for channel in channel_list:
    pwm.setPWM(channel, 0, 210)
time.sleep(3)
pwm.setPWMFreq(0)

print "The ESC on channel " + str(channel) + " is set!"
