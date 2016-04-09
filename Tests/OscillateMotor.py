from Adafruit_PWM_Servo_Driver import PWM
import time

delay = float(raw_input("Type a delay between speed changes in ms: "))
duration = float(raw_input("Type a duration for the oscillation: "))
lowerPowerRange = float(raw_input("Enter the lower power range: "))
higherPowerRange = float(raw_input("Enter the higher power range: "))
powerStep = float(raw_input("Enter the step for power: "))
channel = int(raw_input("Enter the ESC channel: "))

delay = delay/1000
duration = duration/1000
  
print "---------------------"
print "Delay: " + str(delay)
print "Duration " + str(duration)
print "Lower limit: " + str(lowerPowerRange)
print "Higher limit: " + str(higherPowerRange)
print "Power Step: " + str(powerStep)
print "Channel: " + str(channel)
print "---------------------"

pwm = PWM(0x40)
pwm.setPWMFreq(50)
pwm.setPWM(channel, 0, 200)

raw_input("Hit any keys after hearing the beeps...")


timeElapsed = 0.0
powerLevel = lowerPowerRange
tickValue = 200 + int(powerLevel * 2)

while timeElapsed < duration:
    
    pwm.setPWM(channel, 0, tickValue)
    
    if powerLevel >= higherPowerRange:
        if powerStep > 0:
            powerStep = powerStep * -1   
    elif powerLevel <= lowerPowerRange:
        if powerStep < 0:
            powerStep = powerStep * -1
    
    powerLevel += powerStep
    tickValue = 200 + int(powerLevel * 2)
    timeElapsed += delay
    
    print "Power level: " + str(powerLevel) + "%"
    
    time.sleep(delay)
