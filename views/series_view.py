from controllers.series_controller import SeriesController
from os import system as sys


class SeriesView:

    def __init__(self, settings):
        sys('clear')
        self.series_controller = SeriesController(settings)
        self.run()

    def download_single_series(self):
        url = input("\nPlease Type the series url: ")
        self.series_controller.download_series(url)

    def download_multiple_series(self):
        pass

    def download_episodes_for_previously_downloaded_series(self):
        pass

    def run(self):
        print("Series Page:")
        print("1- Download single series")
        print("2- Download Multiple Series")
        print("3- Download Episodes for previously downloaded series")
        print("4- Return to Main Menu")
        print("5- Exit")

        choice = int(input("\nChoice: "))

        if choice == 1:
            self.download_single_series()
        elif choice == 2:
            self.download_multiple_series()
        elif choice == 3:
            self.download_episodes_for_previously_downloaded_series()
        elif choice == 4:
            pass
        elif choice == 5:
            quit()
        else:
            print("Invalid Input try again !! \n\n")
        self.run()
