from .chrome import Chrome
from .firefox import FireFox
import json


class Factory:

    browsers = {
        'chrome': Chrome(),
        'firefox': FireFox(),
    }

    def __init__(self, config):
        data_file = open(config, "r")
        self.config = json.load(data_file)

    def get_driver(self, browser_name: str):

        try:
            driver = self.browsers[browser_name]
            driver.configure_driver(self.config[browser_name])
        except ValueError:
            raise ValueError(f"Value Error for browser_name={browser_name}")

        return driver.initialize_driver()
