from views.movies_view import MoviesView
from views.series_view import SeriesView
from views.settings_view import SettingsView
from controllers.settings_controller import SettingsController
from os import system as sys


class MainView:

    def __init__(self):
        sys('clear')
        self.settings = SettingsController()
        self.run()

    def run(self):
        print("Welcome to Arabseed Bot")
        print("1- Movies Screen")
        print("2- Series Screen")
        print("3- Settings Screen")
        print("4- Exit")

        choice = int(input("\nChoice: "))

        if choice == 1:
            MoviesView(self.settings)
        elif choice == 2:
            SeriesView(self.settings)
        elif choice == 3:
            SettingsView()
        elif choice == 4:
            quit()
        else:
            print("Invalid Input please try again !!")
        self.run()

