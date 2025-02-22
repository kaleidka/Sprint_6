from selenium.webdriver.common.by import By

class OrderButtonSelectors:
    TOP_ORDER_BUTTON = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[contains(text(),'Заказать')]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(text(),'Заказать')]")

class OrderStepOneSelectors:
    FORM_HEADER = (By.XPATH, ".//div[contains(text(),'Для кого самокат')]")
    NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    METRO_DROPDOWN = (By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//div/button[contains(text(),'Далее')]")

class OrderStepTwoSelectors:
    FORM_HEADER = (By.XPATH, "//div[contains(text(), 'Про аренду')]")
    DATE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DATE_SELECT = (By.XPATH, ".//div[@role='option' and (contains(text(), '{}'))]")
    DAY_SELECT = (By.XPATH, ".//div[contains(@aria-label, '{}-е')]")
    PERIOD_FIELD = (By.XPATH, ".//div[@class='Dropdown-placeholder' and (contains(text(), '* Срок аренды'))]")
    COMMENT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and (contains(text(), 'Заказать'))]")
    CONFIRM_BUTTON = (By.XPATH, ".//button[contains(text(), 'Да')]")
    SUCCESS_MESSAGE = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")
    COLOR_SELECT = (By.ID, "{}")
