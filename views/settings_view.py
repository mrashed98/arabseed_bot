from controllers.settings_controller import SettingsController
from os import system as sys


class SettingsView:

    def __init__(self):
        sys('clear')
        self.settings_controller = SettingsController()
        self.main_display()

    def display_settings(self):
        browser, movie_path, series_path = self.settings_controller.get_settings()
        print("Your current Settings:\n")
        print(f"Browser --> {browser}")
        print(f"Movie Path --> {movie_path}")
        print(f"Series Path --> {series_path}")

    def change_settings(self):
        print("1- Change Browser")
        print("2- Change Movies Path")
        print("3- Change Series Path")
        print("4- Return to Previous Page")
        print("5- Exit")
        choice = int(input("\nChoice: "))
        if choice == 1:
            self.change_browser()
        elif choice == 2:
            self.change_movie_path()
        elif choice == 3:
            self.change_series_path()
        elif choice == 4:
            return
        elif choice == 5:
            quit()
        else:
            print("Invalid Input please try again !!")
            self.change_settings()
        self.change_settings()

    def change_browser(self):
        print("\nPlease Choose one of the following supported Browsers: ")
        print("\n1- Chrome.\n2- FireFox.")
        choice = int(input("\nChoice: "))

        browser = 'chrome'

        if choice == 1:
            browser = "chrome"
        elif choice == 2:
            browser = "firefox"
        else:
            print("Invalid Choice please try again !!")
            self.change_browser()
        self.settings_controller.change_browser(browser)

    def change_movie_path(self):
        movie_path = None
        movie_path = input("\nPlease add the new Movie Library Path: ")
        self.settings_controller.change_movie_path(movie_path)

    def change_series_path(self):
        series_path = None
        series_path = input("\nPlease add the new Series Library Path: ")
        self.settings_controller.change_series_path(series_path)

    def main_display(self):
        print("Settings Page")
        print("1- Display Settings")
        print("2- Change Settings")
        print("3- Return to Main Menu")
        print("4- Exit")

        choice = int(input("\nChoice: "))

        if choice == 1:
            self.display_settings()
        elif choice == 2:
            self.change_settings()
        elif choice == 3:
           return
        elif choice == 4:
            quit()
        else:
            print("Invalid choice please try again\n\n")
        self.main_display()
