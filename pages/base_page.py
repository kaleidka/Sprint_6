import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Ожидание и поиск элемента")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self):
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание URL")
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Открытие страницы")
    def open(self, url):
        self.driver.get(url)

    @staticmethod
    def format_selector(locator, param):
        return locator[0], locator[1].format(param)

    @allure.step("Выполнение JS-скрипта")
    def execute_js(self, script, arg):
        self.driver.execute_script(script, arg)