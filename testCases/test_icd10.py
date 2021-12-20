import traceback
import allure
import pytest
from utilities.read_properties import read_Config
from Page_Objects.mainPageObject import mainPageObject


class Test_mainPage:
    icd = read_Config.get_url()

    def test_logo(self, setup):
        self.driver = setup
        self.driver.get(self.icd)
        self.mpo = mainPageObject(self.driver)
        self.driver.implicitly_wait(15)
        status = self.mpo.set_logo()
        if status:
            assert True
        else:
            traceback.format_exc()
            self.driver.save_screenshot(".\\ScreenShot\\test_logo.png")
            print("error")
            self.driver.close()
            assert False


    def test_codes_button_enable(self, setup):
        self.driver.implicitly_wait(10)
        status = self.mpo.set_codes_button_enable()
        if status:
            assert True
        else:
            traceback.format_exc()
            self.driver.save_screenshot(".\\ScreenShot\\test_codes_button_enable.png")
            print("error")
            self.driver.close()
            assert False


    def test_drop_menu(self, setup):
        self.driver.implicitly_wait(10)
        status = self.mpo.set_drop_menu_enable()
        if status:
            assert True
            self.driver.close()
        else:
            traceback.format_exc()
            self.driver.save_screenshot(".\\ScreenShot\\test_drop_menu.png")
            print("error")
            self.driver.close()
            assert False


    def test_search_locate(self):
        self.driver.implicitly_wait(10)
        status = self.mpo.set_search_locate_top()
        if status:
            assert True
        else:
            traceback.format_exc()
            self.driver.save_screenshot(".\\ScreenShot\\test_search_locate.png")
            print("error")
            self.driver.close()
            assert False


    def test_search_corona(self):
        self.driver.implicitly_wait(10)
        status = self.mpo.set_search()
        if status:
            assert True
        else:
            traceback.format_exc()
            self.driver.save_screenshot(".\\ScreenShot\\test_search.png")
            print("error")
            self.driver.close()
            assert False


    def test_check_result(self):
        self.driver.implicitly_wait(10)
        status = self.mpo.set_result()
        if status == "U07.1":
            assert True
            self.driver.close()
        else:
            traceback.format_exc()
            self.driver.save_screenshot(".\\ScreenShot\\test_result.png")
            print("error")
            self.driver.close()
            assert False
