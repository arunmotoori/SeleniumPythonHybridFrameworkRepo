import configparser

config = configparser.RawConfigParser()
config.read("configurations/config.ini")


class ReadProperties:

    @staticmethod
    def get_browser():
        browser = config.get('common data','browser')
        return browser

    @staticmethod
    def get_url():
        url = config.get('common data','url')
        return url

