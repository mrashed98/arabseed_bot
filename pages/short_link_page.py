from seleniumpagefactory import PageFactory


class ShortLinkPage(PageFactory):

    locators = {
        "download_btn": ("link_text", "تحميل")
    }

    def __int__(self, driver):
        super(ShortLinkPage, self).__int__(10)
        self.driver = driver

    def get_provider_direct_page(self):
        self.download_btn.click_button()
