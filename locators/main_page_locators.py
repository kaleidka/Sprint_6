from selenium.webdriver.common.by import By

class MainPageSelectors:
    FAQ_BUTTON = (By.ID, "accordion__heading-{}")
    ANSWER_TEXT = (By.ID, "accordion__panel-{}")
    SCROLL_ELEMENT = (By.TAG_NAME, "html")

class IconSelectors:
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LINK = (By.XPATH, "//a[@href='//yandex.ru']")
    MAIN_PAGE_TEXT = (By.XPATH, "//div[contains(text(), 'Привезём его прямо к вашей двери')]")
