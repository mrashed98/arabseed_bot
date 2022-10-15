from controllers.movies_controller import MoviesController
from os import system as sys


class MoviesView:

    def __init__(self, settings):
        sys('clear')
        self.movies_controller = MoviesController(settings)
