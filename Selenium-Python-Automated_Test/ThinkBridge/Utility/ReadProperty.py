import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\\Vishnu\\PycharmProjects\\ThinkBridge\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        ApplicationUrl = config.get('BaseURL','JabaTalks')
        return ApplicationUrl

    @staticmethod
    def getSharkEmailUrl():
        SharkEmailUrl = config.get('BaseURL', 'SharkEmail')
        return SharkEmailUrl


