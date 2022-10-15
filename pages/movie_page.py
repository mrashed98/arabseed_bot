from seleniumpagefactory import PageFactory


class MoviePage(PageFactory):

    locators = {


    }

    def __init__(self, driver):
        super(MoviePage, self).__init__(10)
        self.driver = driver
