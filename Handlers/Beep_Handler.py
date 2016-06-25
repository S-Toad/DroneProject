class BeepHandler:
    beepDuration = 1000
    
    def delay(self, beepAmount):
        delayTime = (beepAmount * beepDuration)
        
        delay(delayTime)