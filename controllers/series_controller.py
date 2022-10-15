from pages.series_page import SeriesPage
from factory.factory import Factory as DriverFactory


class SeriesController:

    def __init__(self, settings):
        self.settings = settings
        self.series_page = None
        self.driver = None

    def initialize_series(self, url):
        factory = DriverFactory("configs/browsers_config.json")
        self.driver = factory.get_driver(self.settings.browser)
        self.series_page = SeriesPage(self.driver, url)
        self.series_page.open()
        self.series_page.initialize_title()
        self.series_page.initialize_episodes()

    def get_desired_episodes(self):
        print(f"Currently uploaded episodes are {self.series_page.get_number_of_episodes}")
        print("Choose the desired episodes using the following patterns:\n")
        print("<Start_Episode>:<End_Episode> , numbers of episodes separated with (,), 0 to download all")

        choice = input("Episodes: ")
        if ":" in choice:
            choice.split(":")
        elif "," in choice:
            choice = choice.split(',')
        elif choice == 0:
            pass
        else:
            print("Invalid choice please try again !!")
            self.get_desired_episodes()

    def download_series(self, url):
        self.initialize_series(url)
        print(f"Series title: {self.series_page.get_title()}")
        print(f"Number of uploaded episodes: {self.series_page.get_number_of_episodes()}")
        print("\n\nEPISODE LIST:\n")
        self.series_page.get_episodes()

    def download_multiple_series(self):
        pass

    def get_all_series(self):
        return print("Currently Under Constructions ... ")

    def get_series_downloaded_episodes(self):
        return print("Currently Under Constructions ... ")

    def get_series_not_downloaded_episodes(self):
        return print("Currently Under Constructions ... ")

