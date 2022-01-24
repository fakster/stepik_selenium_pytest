from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, " login is't substring of current Url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_VALIDATION),'Email input in Login is not presented'
        self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_VALIDATION), 'Password input in Login is not presented'
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_VALIDATION),'Email input in registration is not presented'
        self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_VALIDATION), 'Password input in Registration is not presented'
        self.is_element_present(
            *LoginPageLocators.REGISTRATION_REPEAT_PASSWORD_VALIDATION), 'Repeat password input in Registration is not presented'
        assert True