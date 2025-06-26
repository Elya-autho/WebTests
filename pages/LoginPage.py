from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.ID,'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH, '//*[@id="qrCode-3407364914"]/span')
    FORGOT_PASSWORD = (By.XPATH, '//*[@tsid="restore"]')
    REGISTER_BUTTON = (By.XPATH,'//*[@data-l="t,register"]')

    VK_IKON = (By.XPATH, '//*[@data-module="registration/vkconnect"]')
    MAIL_IKON =(By.XPATH, '//*[@data-provider="MAILRU"]')
    YANDEX_IKON = (By.XPATH,'//*[@data-l="t,yandex"]')
    QR_TAB = (By.XPATH,'//*[@data-l="t,qr_tab"]')


class LoginPageHelper(BasePage):
    pass
