from Adafruit_PWM_Servo_Driver import PWM
import time
from ConfigParser import SafeConfigParser

'''
This code should be ran with any new ESC (Electronic Speed Controllers) to configure them to the correct parameters.
Below are parameters that 'you' are able to change to fit with your ideal specifications.

Please see ESC_Configuration.INI for summary of configurations
'''

# This takes the raw input from the user and sorts into a list of integers to use.
channel_list = map(int,raw_input("Enter the ESC channel(s), (Example: 12 13 14 15): "))

# This section simply reads from the ESC_Configuration.INI for the values needed
# TODO: Make this into it's own method to keep things clean? 
config = SafeConfigParser()
config.read("ESC_Configuration.INI")
pulseHertz = int(config.get('ESC_Config', 'pulseHertz'))
bottomTickRange = int(config.get('ESC_Config', 'bottomTickRange'))
upperTickRange = int(config.get('ESC_Config', 'upperTickRange'))

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
# TODO: Make each configuration it's own method/file?

print "Will run at 5% for a short period"
time.sleep(3)

for channel in channel_list:
    pwm.setPWM(channel, 0, 210)
time.sleep(3)
pwm.setPWMFreq(0)

print "The ESC on channel " + str(channel) + " is set!"
