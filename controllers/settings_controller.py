from os.path import exists
import json


class SettingsController:

    def __init__(self):

        self.config_path = "configs/settings.json"
        self.browser = None
        self.movie_path = None
        self.series_path = None

        config_file = exists(self.config_path)
        if config_file:
            self.initialize_config()
        else:
            self.create_config_file()
            self.save_config()

    def initialize_config(self):
        file = open(self.config_path, 'r')
        config = json.load(file)
        self.browser = config['browser']
        self.movie_path = config['movie_path']
        self.series_path = config['series_path']
        file.close()

    def create_config_file(self):
        print("\nPlease Choose one of the following supported Browsers: ")
        print("\n1- Chrome.\n2- FireFox.")
        choice = int(input("\nChoice: "))

        if choice == 1:
            self.browser = "chrome"
        elif choice == 2:
            self.browser = "firefox"
        else:
            print("Invalid Choice please try again !!")
            self.create_config_file()

        self.movie_path = input("\nPlease add the Movie Library Path: ")
        self.series_path = input("\nPlease add the Series Library Path: ")
        print("Thanks.....")

    def save_config(self):
        data = {
            "browser": self.browser,
            "movie_path": self.movie_path,
            "series_path": self.series_path
        }

        file = open(self.config_path, 'w+')
        json_object = json.dumps(data, indent=4)
        file.write(json_object)
        file.close()

    def change_browser(self, browser):
        self.browser = browser
        self.save_config()

    def change_movie_path(self, movie_path):
        self.movie_path = movie_path
        self.save_config()

    def change_series_path(self, series_path):
        self.series_path = series_path
        self.save_config()

    def get_settings(self):
        return self.browser, self.movie_path, self.series_path
