import RPi.GPIO as GPIO
import time

delay = 0.0
duration = 0.0
lowerRange = 0.0
higherRange = 0.0
interval = 0.0

while True:
    try:
        delay = float(raw_input("Type a delay between duty cycles in ms: "))
    except ValueError:
        print "Numbers higher than 0 only"
    else:
        if delay < 0:
            print "Numbers higher than 0 only"
        else:
            delay = delay/1000
            break

while True:
    try:
        duration = float(raw_input("Type a duration between duty cycles in ms: "))
    except ValueError:
        print "Numbers higher than 0 only"
    else:
        if duration < 100:
            "Numbers higher than 0 only"
        else:
            duration = duration/1000
            break

while True:
    try:
        lowerRange = float(raw_input("Enter the lower range: "))
    except ValueError:
        print "Numbers between 0-100 only"
    else:
        if lowerRange > 100 or lowerRange < 0:
            print "Numbers between 0-100 only"
        else:
            break

while True:
    try:
        higherRange = float(raw_input("Enter the higher range: "))
    except ValueError:
        print "Numbers between 0-100 only"
    else:
        if higherRange <= lowerRange or higherRange > 100 or higherRange < 0:
            print "Higher range must be higher than " + lowerRange + " and between 0-100"
        else:
            break

while True:
    try:
        interval = float(raw_input("Type a interval between duty cycles: "))
    except ValueError:
        print "Numbers between 0-100 only"
    else:
        if interval > 100 or interval < 0:
            print "Interval must be between 0-100"
        else:
            break

print "Delay: " + str(delay)
print "Duration " + str(duration)
print "Lower limit: " + str(lowerRange)
print "Higher limit: " + str(higherRange)
print "Interval: " + str(interval)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)
p.start(0)


x = 0.0
value = lowerRange

while x < duration:
    x += delay
    
    value += interval
    
    if value >= higherRange:
        if interval > 0:
            interval = interval * -1
        value = higherRange
    elif value <= lowerRange:
        if interval < 0:
            interval = interval * -1
        value = lowerRange
    
    print value
    p.ChangeDutyCycle(value)
    
    time.sleep(delay)

p.stop()
GPIO.cleanup()