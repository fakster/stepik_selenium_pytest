from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_EMAIL_VALIDATION=(By.CSS_SELECTOR,'#id_login-username')
    LOGIN_PASSWORD_VALIDATION=(By.CSS_SELECTOR,'#id_login-password')
    REGISTRATION_EMAIL_VALIDATION = (By.CSS_SELECTOR,'#id_registration-email')
    REGISTRATION_PASSWORD_VALIDATION = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_REPEAT_PASSWORD_VALIDATION = (By.CSS_SELECTOR, '#id_registration-password2')

class ProductPageLocators():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR,'.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,'.alertinner')