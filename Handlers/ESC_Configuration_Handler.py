import configparser

class ESC_Configuration_Handler:

    @classmethod
    def getConfig(self):
        fileName = 'ESC_Configuration.ini'
        config = configparser.ConfigParser()
        config.read(fileName)
        
        return config
    
    @classmethod
    def returnPulseHertz(self):
        config = self.getConfig()
        pulseHertz = int(config.get('ESC_Config', 'pulseHertz'))
        
        return pulseHertz
    
    @classmethod
    def returnBottomTickRange(self):
        config = self.getConfig()
        bottomTickRange = int(config.get('ESC_Config', 'bottomTickRange'))
        
        return bottomTickRange
    
    @classmethod
    def returnUpperTickRange(self):
        config = self.getConfig()
        upperTickRange = int(config.get('ESC_Config', 'upperTickRange'))
        
        return upperTickRange
    
    @classmethod
    def returnBrakeType(self):
        config = self.getConfig()
        brakeType = int(config.get('ESC_Config', 'brakeType'))
        
        return brakeType
    
    @classmethod
    def returnTimingMode(self):
        config = self.getConfig()
        timingMode = int(config.get('ESC_Config', 'timingMode'))
        
        return timingMode
    
    @classmethod
    def returnStartForce(self):
        config = self.getConfig()
        startForce = int(config.get('ESC_Config', 'startForce'))
        
        return startForce
    
    @classmethod
    def returnControlFrequency(self):
        config = self.getConfig()
        controlFrequency = int(config.get('ESC_Config', 'controlFrequency'))
        
        return controlFrequency
    
    @classmethod
    def returnLowVoltageProtection(self):
        config = self.getConfig()
        lowVoltageProtection = int(config.get('ESC_Config', 'lowVoltageProtection'))
        
        return lowVoltageProtection
    
    @classmethod
    def returnCutOffMode(self):
        config = self.getConfig()
        cutOffMode = int(config.get('ESC_Config', 'cutOffMode'))
        
        return timingMode
