from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TransactionsPage(BasePage):

    # Locators
    HELLO_MESSAGE = "[class^='BalanceModal_modal']"
    EXPENSES_TAB = "//a[text()='Expenses']"
    INCOME_TAB = "//a[text()='Income']"
    CALENDAR_ICON = "[class^='FormTransaction_calendarIcon']"
    DESCRIPTION_FIELD = "[class^='FormTransaction_input']"
    CATEGORY_DROPDOWN_INPUT = "div[class=' css-ackcql']>input"
    CATEGORY_DROPDOWN_FIELD = "div[class=' css-ackcql']"
    AMOUNT_FIELD = "[class^='FormTransaction_calcInput']"
    INPUT_BUTTON = "//button[text()='Input']"
    CLEAR_BUTTON = "//button[text()='Clear']"
    DELETE_BUTTON = "[class^='TransactionList_buttonDelete']"
    REPORTS_PAGE_LINK = "[class^='DataHeader_reportsLink']"

    # Getters
    def get_hello_message(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.HELLO_MESSAGE, 3)

    def get_expenses_tab(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.EXPENSES_TAB)

    def get_income_tab(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.INCOME_TAB)

    def get_calendar_icon(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.CALENDAR_ICON)

    def get_date_picker(self, day_of_the_month):
        return self.wait_for_visibility_of_element(By.CLASS_NAME, f"react-datepicker__day--0{day_of_the_month}")

    def get_description_field(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.DESCRIPTION_FIELD)

    def get_category_dropdown_input_field(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.CATEGORY_DROPDOWN_INPUT)

    def get_category_dropdown_field(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.CATEGORY_DROPDOWN_FIELD)

    def get_amount_field(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.AMOUNT_FIELD)

    def get_input_button(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.INPUT_BUTTON)

    def get_clear_button(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.CLEAR_BUTTON)

    def get_delete_button(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.DELETE_BUTTON)

    def get_delete_buttons(self):
        return self.wait_for_visibility_of_elements(By.CSS_SELECTOR, self.DELETE_BUTTON, 4)

    def get_reports_page_link(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.REPORTS_PAGE_LINK)

    def get_transaction_descr_td(self, description):
        return self.wait_for_visibility_of_element(By.XPATH, f"//td[text()='{description}']", 4)

    def get_month_summary_amount_p(self, month_name):
        return self.wait_for_visibility_of_element(By.XPATH, f"//p[text()='{month_name}']/following-sibling::p")

    def get_month_summary_amount_by_txt(self, month_name, text_in_element, timeout):
        return self.wait_for_text_in_element(By.XPATH, f"//p[text()='{month_name}']/following-sibling::p",
                                             text_in_element, timeout)

    # Interactions with web elements
    def add_new_transaction(self, description, category_name, amount, t_type="expense"):
        if t_type == "expense":
            self.get_expenses_tab().click()
        elif t_type == "income":
            self.get_income_tab().click()
        elif t_type == "not_set":
            pass
        else:
            raise ValueError("Available values: 'expense', 'income', 'not_set'")
        self.get_description_field().send_keys(description)
        self.get_category_dropdown_field().click()
        self.get_category_dropdown_input_field().send_keys(category_name, Keys.ENTER)
        self.get_amount_field().send_keys(amount)
        self.get_input_button().click()

    def add_multiple_transactions(self, description, category_name, amount, number=1):
        for x in range(number):
            self.add_new_transaction(f"{description} {x+1}", category_name, amount)

    def change_transaction_date(self, day_of_the_month=14):
        self.get_calendar_icon().click()
        self.get_date_picker(day_of_the_month).click()

    def clear_transactions(self):
        try:
            transactions = self.get_delete_buttons()
            for t in transactions:
                t.click()
        except TimeoutException:
            pass
