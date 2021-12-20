import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Lounching Chrome......")
        driver.maximize_window()
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path="drivers/msedgedriver.exe")
        print("Lounching Edge......")
        driver.maximize_window()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
