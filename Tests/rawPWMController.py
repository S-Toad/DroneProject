from PWM_Handler import PWM_Handler

PWM_Handler.intializePWMFreq()

channel = input("Enter PWM channel: ")

while (True):
    power = input("Enter power or q to quit: ")
    
    if power == 'q':
        PWM_Handler.turnOffChannel(channel)
        break
    else:
        power = float(power)
        PWM_Handler.setPower(channel, power)