from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    FORGOT_PASSWORD = (By.XPATH, '//*[@tsid="restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    VK_IKON = (By.XPATH, '//*[@data-module="registration/vkconnect"]')
    MAIL_IKON = (By.XPATH, '//*[@data-provider="MAILRU"]')
    YANDEX_IKON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')
    GO_Back_BUTTON = (By.XPATH, '//*[@data-l="t,cancel"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@class="external-oauth-login-help portlet_f"]')
    PROFILE_RECOVERY_BUTTON = (By.NAME, 'st.go_to_recovery')



class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_IKON)
        self.find_element(LoginPageLocators.MAIL_IKON)
        self.find_element(LoginPageLocators.YANDEX_IKON)

    @allure.step("Нажимаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Вводим логин")
    def send_empty_password(self, LOGIN):
        self.attach_screenshot()
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(LOGIN)
        self.click_login()
        return self.get_error_text()
    @allure.step("Заполняем поле логин")
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()
    @allure.step("Заполняем поле пароля")
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.PROFILE_RECOVERY_BUTTON).click()

    @allure.step("Переходим к регистрации")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()


