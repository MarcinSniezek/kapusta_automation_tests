from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    HOME_PAGE_LINK = "//a[@alt='homepage']"
    BALANCE_FIELD = "[class^='Balance_input']"
    CONFIRM_BALANCE_BUTTON = "//button[text()='CONFIRM']"
    LOGOUT_LINK = "[class^='UserLogOut_logOutTextBtn']"
    MODAL_WINDOW = "[class^='Modal_modalContainer']"
    MODAL_CLOSE_BUTTON = "[class^='Modal_closeBtn']"
    MODAL_CONFIRM_BUTTON = "//button[text()='YES']"
    MODAL_CANCEL_BUTTON = "//button[text()='NO']"

    # Waits
    def wait_for_visibility_of_element(self, locator_type, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.visibility_of_element_located((locator_type, locator)))
        return element

    def wait_for_visibility_of_elements(self, locator_type, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(ec.visibility_of_all_elements_located((locator_type, locator)))
        return elements

    def wait_for_text_in_element(self, locator_type, locator, text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.text_to_be_present_in_element((locator_type, locator), text))
        return element

    def wait_for_url(self, expected_url, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.url_to_be(expected_url))
        except TimeoutException:
            pass

    # Getters
    def get_home_page_link(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.HOME_PAGE_LINK)

    def get_balance_field(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.BALANCE_FIELD)

    def get_confirm_balance_button(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.CONFIRM_BALANCE_BUTTON)

    def get_logout_link(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.LOGOUT_LINK)

    def get_modal_window(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.MODAL_WINDOW, 4)

    def get_modal_close_btn(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.MODAL_CLOSE_BUTTON)

    def get_modal_confirm_btn(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.MODAL_CONFIRM_BUTTON)

    def get_modal_cancel_btn(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.MODAL_CANCEL_BUTTON)

    # Interactions with elements
    def logout(self):
        self.get_logout_link().click()
        self.get_modal_confirm_btn().click()

    def set_balance(self, amount):
        self.get_balance_field().send_keys(amount)
        self.get_confirm_balance_button().click()
