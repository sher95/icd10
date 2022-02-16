import traceback
from utilities.read_properties import read_Config

codes = read_Config.get_url()


class Test_icd10:
    def test_logo(self, setup):
        driver = setup
        driver.get(codes)
        driver.implicitly_wait(15)
        driver.maximize_window()
        status = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img").is_displayed()
        if status:
            assert True
        else:
            traceback.format_exc()
            driver.save_screenshot(".\\ScreenShot\\test_logo.png")
            print("error")
            assert False

    def test_codes_button_enable(self, setup):
        driver = setup
        driver.get(codes)
        driver.implicitly_wait(10)
        driver.maximize_window()
        status = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').is_enabled()
        if status:
            assert True
        else:
            traceback.format_exc()
            driver.save_screenshot(".\\ScreenShot\\test_code_button.png")
            print("error")
            assert False

    def test_drop_menu_enable(self, setup):
        driver = setup
        driver.get(codes)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
        status = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/ul').is_displayed()
        if status:
            assert True
        else:
            traceback.format_exc()
            driver.save_screenshot(".\\ScreenShot\\test_drop_menu.png")
            print("error")
            assert False

    def test_search_locate(self, setup):
        driver = setup
        driver.get(codes)
        driver.implicitly_wait(10)
        driver.maximize_window()
        status = driver.find_element_by_id('searchText').is_displayed()
        if status:
            assert True
        else:
            traceback.format_exc(setup)
            driver.save_screenshot(".\\ScreenShot\\test_search_locate.png")
            print("error")
            assert False

    def test_search_corona(self, setup):
        driver = setup
        driver.get(codes)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element_by_id('searchText').send_keys("U07.1")
        driver.implicitly_wait(10)
        driver.find_element_by_id('search').click()
        status = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/div[1]/strong/a/span/span")
        if status:
            assert "U07.1" in status.text
        else:
            traceback.format_exc()
            driver.save_screenshot(".\\ScreenShot\\test_search.png")
            print("error")
            assert False
