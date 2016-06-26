from Handlers.PWM_Handler import PWM_Handler

channel = input("Enter PWM channel: ")

while (True):
    power = input("Enter power or q to quit: ")
    
    if power == 'q':
        PWM_Handler.turnOffChannel(channel)
        break
    else:
        power = float(power)
        PWM_Handler.setPower(channel, power)