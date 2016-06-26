import configparser

class ESC_Configuration_Handler:

    @classmethod
    def getConfig(self, option):
        fileName = '../ESC_Configuration.INI'
        config = configparser.ConfigParser()
        config.read(fileName)
        
        optionValue = config.get('ESC_Config', option)
        
        return option
    
    @classmethod
    def returnPulseHertz(self):
        pulseHertz = int(self.getConfig('pulseHertz'))
        
        return pulseHertz
    
    @classmethod
    def returnBottomTickRange(self):
        bottomTickRange = int(self.getConfig('bottomTickRange'))
        
        return bottomTickRange
    
    @classmethod
    def returnUpperTickRange(self):
        upperTickRange = int(self.getConfig('upperTickRange'))
        
        return upperTickRange
    
    @classmethod
    def returnBrakeType(self):
        brakeType = int(self.getConfig('brakeType'))
        
        return brakeType
    
    @classmethod
    def returnTimingMode(self):
        timingMode = int(self.getConfig('timingMode'))

        return timingMode
    
    @classmethod
    def returnStartForce(self):
        startForce = int(self.getConfig('startForce'))
        
        return startForce
    
    @classmethod
    def returnControlFrequency(self):
        controlFrequency = int(self.getConfig('controlFrequency'))
        
        return controlFrequency
    
    @classmethod
    def returnLowVoltageProtection(self):
        lowVoltageProtection = int(self.getConfig('lowVoltageProtection'))
        
        return lowVoltageProtection
    
    @classmethod
    def returnCutOffMode(self):
        cutOffMode = int(self.getConfig('cutOffMode'))
        
        return cutOffMode
