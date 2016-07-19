import ConfigParser

class ConfigHandler:
    def __init__(self, fileName, section):
        self.fileName = fileName
        self.section = section
        self.reload()
    
    def getSectionData(self, section, option):
        optionValue = self.config.get(section, option)
        return optionValue
    
    def getData(self, option):
        optionValue = self.config.get(self.section, option)
        return optionValue
        
    def setSection(self, section):
        self.section = section
    
    def hasSection(self, section):
        return self.config.has_section(section)
    
    def reload(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.fileName)