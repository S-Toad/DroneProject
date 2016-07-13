import configparser

class configHandler:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.config = configparser.ConfigParser()
        self.config.read(self.fileName)
    
    def getConfig(self, section, option):
        optionValue = self.config.get(section, option)
        return optionValue
    
