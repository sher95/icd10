class mainPageObject:
    logo_xpath = "/html/body/div[2]/div/div[1]/a/img"
    codes_button_xpath = '//*[@id="navMenu"]/li[1]/a'
    drop_menu_xpath = '//*[@id="navMenu"]/li[1]/ul'
    search_locate_id = "searchText"
    search_id = "search"
    result_path = "/html/body/div[3]/div/div[1]/div/div[2]/div[1]/strong/a/span/span"




    def __init__(self, driver):
        self.driver = driver

    def set_logo(self):
        self.driver.find_element_by_xpath(self.logo_xpath).is_displayed()

    def set_codes_button_enable(self):
        self.driver.find_element_by_xpath(self.codes_button_xpath).is_displayed()

    def set_drop_menu_enable(self):
        self.driver.find_element_by_xpath(self.codes_button_xpath).click()
        self.driver.find_element_by_xpath(self.drop_menu_xpath).is_displayed()

    def set_search_locate_top(self):
        self.driver.find_element_by_id(self.search_locate_id).is_displayed()

    def set_search(self):
        self.driver.find_element_by_id(self.search_locate_id).send_keys("U07.1")
        self.driver.find_element_by_id(self.search_id).click()

    def set_result(self):
        self.driver.find_element_by_id(self.result_path)
