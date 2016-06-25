import configparser

class ESC_Configuration_Handler:
    
    def __init__(self, reverse):
        self.reverse = reverse
    
    def getConfig():
        fileName = 'ESC_Configuration.ini'
        config = configparser.ConfigParser()
        config.read(fileName)
        
        return config
    
    def returnPulseHertz():
        config = ESC_Configuration_Handler.getConfig()
        pulseHertz = int(config.get('ESC_Config', 'pulseHertz'))
        
        return pulseHertz
    
    def returnBottomTickRange():
        config = ESC_Configuration_Handler.getConfig()
        bottomTickRange = int(config.get('ESC_Config', 'bottomTickRange'))
        
        return bottomTickRange
    
    def returnUpperTickRange():
        config = ESC_Configuration_Handler.getConfig()
        upperTickRange = int(config.get('ESC_Config', 'upperTickRange'))
        
        return upperTickRange
    
    def returnBrakeType():
        config = ESC_Configuration_Handler.getConfig()
        brakeType = int(config.get('ESC_Config', 'brakeType'))
        
        return brakeType
    
    def returnTimingMode():
        config = ESC_Configuration_Handler.getConfig()
        timingMode = int(config.get('ESC_Config', 'timingMode'))
        
        return timingMode
    
    def returnStartForce():
        config = ESC_Configuration_Handler.getConfig()
        startForce = int(config.get('ESC_Config', 'startForce'))
        
        return startForce
    
    def returnControlFrequency():
        config = ESC_Configuration_Handler.getConfig()
        controlFrequency = int(config.get('ESC_Config', 'controlFrequency'))
        
        return controlFrequency
    
    def returnLowVoltageProtection():
        config = ESC_Configuration_Handler.getConfig()
        lowVoltageProtection = int(config.get('ESC_Config', 'lowVoltageProtection'))
        
        return lowVoltageProtection
    
    def returnCutOffMode():
        config = ESC_Configuration_Handler.getConfig()
        cutOffMode = int(config.get('ESC_Config', 'cutOffMode'))
        
        return timingMode
    
    def getReverse():
        return self.reverse