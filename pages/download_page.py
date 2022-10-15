from seleniumpagefactory import PageFactory
from time import sleep


class DownloadPage(PageFactory):

    locators = {
        "init_download_btn": ("link_text", "Free Download"),
        "create_download_link": ("link_text", "Create download link"),
        "Download_btn": ("link_text", "Download")
    }

    def __init__(self, driver):
        super(DownloadPage, self).__init__(10)
        self.driver = driver

    def init_download(self):
        self.init_download_btn.click_button()

    def create_direct_download_link(self):
        sleep(25)
        self.create_download_link.click_button()

    def get_direct_download_link(self):
        self.Download_btn.getAttribute("href")
