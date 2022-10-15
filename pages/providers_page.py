from selenium.webdriver.common.by import By


class ProvidersPage:

    def __init__(self, driver):
        self.driver = driver
        self.qualities = {}
        self.init_quality_block()

    def init_quality_block(self):
        quality_blocks = self.driver.find_elements(By.CLASS_NAME, 'DownloadBlock')

        for block in quality_blocks:
            quality_name_container = block.find_element(By.CLASS_NAME, 'TitleCenteral')
            quality_name = quality_name_container.find_element(By.TAG_NAME, 'span').text
            quality_link = block.find_element(By.CLASS_NAME, 'Arabseed').get_attribute('href')
            self.qualities[quality_name] = quality_link

    def get_quality_blocks(self):
        return self.qualities
