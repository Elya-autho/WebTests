from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class VKEcosystemPageLocators:
    TITLE_LABEL = (By.XPATH, '//h1[@class="title-h2"]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot(VKEcosystemPageLocators.TITLE_LABEL)