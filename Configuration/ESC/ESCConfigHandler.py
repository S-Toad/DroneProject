from Handlers.ConfigHandler import ConfigHandler

class ESCConfigHandler(ConfigHandler):
    fileName = 'ESC_Configuration.INI'
    section = 'ESC_Config'
    
    def __init__(self):
        ConfigHandler.__init__(self, self.fileName)
    
    def returnPulseHertz(self):
        pulseHertz = int(self.getConfig(self.section, 'pulseHertz'))
        return pulseHertz
    
    def returnBottomTickRange(self):
        bottomTickRange = int(self.getConfig(self.section, 'bottomTickRange'))
        return bottomTickRange
    
    def returnUpperTickRange(self):
        upperTickRange = int(self.getConfig(self.section, 'upperTickRange'))
        return upperTickRange
    
    def returnBrakeType(self):
        brakeType = int(self.getConfig(self.section, 'brakeType'))
        return brakeType
    
    def returnTimingMode(self):
        timingMode = int(self.getConfig(self.section, 'timingMode'))
        return timingMode
    
    def returnStartForce(self):
        startForce = int(self.getConfig(self.section, 'startForce'))
        return startForce
    

    def returnControlFrequency(self):
        controlFrequency = int(self.getConfig(self.section, 'controlFrequency'))
        return controlFrequency
    

    def returnLowVoltageProtection(self):
        lowVoltageProtection = int(self.getConfig(self.section, 'lowVoltageProtection'))
        return lowVoltageProtection
    
    def returnCutOffMode(self):
        cutOffMode = int(self.getConfig(self.section, 'cutOffMode'))
        return cutOffMode