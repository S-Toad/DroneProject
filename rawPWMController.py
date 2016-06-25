from Handlers.PWM_Handler import PWM_Handler

pwmHandler = PWM_Handler.intializePWMFreq()
channel = input("Enter PWM channel: ")

while (True):
    power = input("Enter power or q to quit: ")
    
    if power == 'q':
        pwmHandler.turnOffChannel(channel)
        break
    else:
        power = float(power)
        pwmHandler.setPower(channel, power)