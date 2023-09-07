from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginRegisterPage(BasePage):
    # Locators
    EMAIL_INPUT = "email"
    PASSWORD_INPUT = "password"
    REGISTRATION_BUTTON = "//button[text()='REGISTRATION']"
    LOGIN_BUTTON = "//button[text()='LOG IN']"
    ALERT_WINDOW = "//div[@role='alert']"

    def get_email_input_field(self):
        return self.wait_for_visibility_of_element(By.ID, self.EMAIL_INPUT)

    def get_password_input_field(self):
        return self.wait_for_visibility_of_element(By.ID, self.PASSWORD_INPUT)

    def get_registration_button(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.REGISTRATION_BUTTON)

    def get_login_button(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.LOGIN_BUTTON)

    def get_alert_window(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.ALERT_WINDOW, 2)

    def register(self, username, password):
        self.get_email_input_field().send_keys(username)
        self.get_password_input_field().send_keys(password)
        self.get_registration_button().click()

    def login(self, username, password):
        self.get_email_input_field().send_keys(username)
        self.get_password_input_field().send_keys(password)
        self.get_login_button().click()
