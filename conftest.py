import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
