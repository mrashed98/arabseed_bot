from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By
from models.series import *


class SeriesPage(PageFactory):

    locators = {
        "title_container": ('class_name', 'BreadCrumbs'),
        "episodes_container": ('class_name', 'ContainerEpisodesList')
    }

    def __init__(self, driver, url):
        super(SeriesPage, self).__init__(10)
        self.driver = driver
        self.series = Series(url)

    def open(self):
        self.driver.get(self.series.link)

    def initialize_episodes(self):
        episode_list = self.episodes_container.find_elements(By.TAG_NAME, 'a')
        for episode in episode_list:
            episode_number = episode.find_element(By.TAG_NAME, 'em').get_text()
            episode_link = episode.get_attribute('href')+"/download"
            self.series.add_episode(Episode(episode_number, episode_link))

    def initialize_title(self):
        series_title = self.title_container.find_elements(By.TAG_NAME, 'li')[3].text
        self.series.set_series_title(series_title)

    def get_episodes(self):
        for episode in self.series.episodes:
            print(f"Episode Number #{episode.episode_number} --> Link: {episode.episode_link}")
        return self.series.episodes

    def get_title(self):
        return self.series.title

    def get_number_of_episodes(self):
        return len(self.series.episodes)
