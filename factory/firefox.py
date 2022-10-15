from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


class FireFox:

    def __init__(self):
        self.driver = None
        self.options = None

    def configure_driver(self, config: dict):
        self.options = Options()
        # self.options.binary_location = r'/usr/lib/firefox/firefox'
        for argument in config.values():
            self.options.add_argument(argument)

    def initialize_driver(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=self.options)
        self.driver.maximize_window()
        return self.driver
