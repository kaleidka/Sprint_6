import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseActions:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание и поиск элемента")
    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url(self, link):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(link))

    @allure.step("Открытие страницы")
    def open(self, url):
        self.driver.get(url)

    @staticmethod
    def format_selector(locator, param):
        return locator[0], locator[1].format(param)

    def execute_js(self, script, arg):
        self.driver.execute_script(script, arg)
