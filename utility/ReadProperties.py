import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Swapnil\PycharmProjects\DemoProjectSwagLabs\configurations\config.ini")


class ReadData:

    @staticmethod
    def readUrl():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def readUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def readPassWd():
        password = config.get('common info', 'password')
        return password
