import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from utilities.Utils import Utils
from data.test_data import transaction_data


@pytest.mark.usefixtures("setup")
class TestTransactions:
    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add new expense transaction", "Add new income transaction"])
    def test_tc9_should_add_new_transaction(self, transaction_type, valid_login_data, valid_description):
        email, password = valid_login_data
        description = valid_description
        amount = transaction_data['valid']['amount']

        self.login_page.login(email, password)

        if transaction_type == "expenses":
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Products", amount)
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Add. income", amount, "income")

        try:
            self.transactions_page.get_transaction_descr_td(description)
        except TimeoutException:
            assert False, "Couldn't find a web element with the description of the new transaction!"

    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add new expense transaction", "Add new income transaction"])
    def test_tc9_should_add_new_transaction_with_amount_check(self, transaction_type, valid_login_data,
                                                              valid_description):
        email, password = valid_login_data
        description = valid_description
        current_month = "September"
        transaction_amount = transaction_data['valid']['amount']
        initial_amount = None

        self.login_page.login(email, password)

        if transaction_type == "expenses":
            self.transactions_page.get_expenses_tab().click()
            text = self.transactions_page.get_month_summary_amount_p(current_month).text
            initial_amount = Utils.convert_string_to_float(text)
            self.transactions_page.add_new_transaction(description, "Products", transaction_amount, "not_set")
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()
            text = self.transactions_page.get_month_summary_amount_p(current_month).text
            initial_amount = Utils.convert_string_to_float(text)
            self.transactions_page.add_new_transaction(description, "Add. income", transaction_amount, "not_set")

        expected_amount = initial_amount + transaction_amount
        expected_amount_str = "{:.2f}".format(expected_amount)

        try:
            self.transactions_page.get_month_summary_amount_by_txt(current_month, expected_amount_str, 5)
        except TimeoutException:
            pass

        actual_amount = \
            Utils.convert_string_to_float(self.transactions_page.get_month_summary_amount_p(current_month).text)

        assert expected_amount == actual_amount, f"Invalid amount: {expected_amount} is not equal to {actual_amount}"

    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add expense transaction", "Add income transaction"])
    def test_tc10_should_not_add_transaction_without_category_and_amount_set(self, transaction_type, valid_login_data,
                                                                             valid_description):
        email, password = valid_login_data
        description = valid_description

        self.login_page.login(email, password)

        if transaction_type == "expenses":
            self.transactions_page.get_expenses_tab().click()
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()

        self.transactions_page.clear_transactions()
        self.transactions_page.get_description_field().send_keys(description)
        self.transactions_page.get_input_button().click()

        try:
            self.transactions_page.get_transaction_descr_td(description)
        except TimeoutException:
            pass
        else:
            assert False, "Shouldn't be possible to add transaction without setting category and amount!"

    @pytest.mark.parametrize("description_length", [21, 2], ids=[
        "Description length should not be more than 20 chars",
        "Description length should not be less than 3 chars"
    ])
    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add expense transaction", "Add income transaction"])
    def test_tc10_should_not_add_transaction_with_invalid_description(self, transaction_type,
                                                                      description_length, valid_login_data):
        email, password = valid_login_data
        description = Utils.get_custom_length_string(length=description_length)
        amount = transaction_data['valid']['amount']

        self.login_page.login(email, password)
        if transaction_type == "expenses":
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Products", amount)
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Add. income", amount, "income")

        try:
            self.transactions_page.get_transaction_descr_td(description)
        except TimeoutException:
            pass
        else:
            assert False, "Shouldn't be possible to add a transaction with a description out of range of 3-20 chars!"

    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add expense transaction", "Add income transaction"])
    def test_tc10_should_not_add_transaction_with_amount_equal_to_zero(self, transaction_type, valid_login_data,
                                                                       valid_description):
        email, password = valid_login_data
        description = valid_description
        amount = 0

        self.login_page.login(email, password)
        if transaction_type == "expenses":
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Products", amount)
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Add. income", amount, "income")

        try:
            self.transactions_page.get_transaction_descr_td(description)
        except TimeoutException:
            pass
        else:
            assert False, "Shouldn't be possible to add a transaction with an amount equal to zero!"

    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add expense transaction", "Add income transaction"])
    def test_tc10_should_not_add_transaction_with_invalid_amount(self, transaction_type, valid_login_data,
                                                                 valid_description):
        email, password = valid_login_data
        description = valid_description
        amount = transaction_data['invalid']['amount']

        self.login_page.login(email, password)
        if transaction_type == "expenses":
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Products", amount)
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()
            self.transactions_page.clear_transactions()
            self.transactions_page.add_new_transaction(description, "Add. income", amount, "income")

        try:
            self.transactions_page.get_transaction_descr_td(description)
        except TimeoutException:
            pass
        else:
            assert False, \
                "Shouldn't be possible to add a transaction with an amount containing letters or special chars!"

    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add expense transaction", "Add income transaction"])
    def test_tc12_should_clear_transaction_data(self, transaction_type, valid_login_data):
        email, password = valid_login_data
        description = Utils.get_custom_length_string()
        amount = transaction_data['valid']['amount']

        self.login_page.login(email, password)

        if transaction_type == "expenses":
            self.transactions_page.get_expenses_tab().click()
            self.transactions_page.get_description_field().send_keys(description)
            self.transactions_page.get_category_dropdown_input_field().send_keys("Products", Keys.ENTER)
        elif transaction_type == "income":
            self.transactions_page.get_income_tab().click()
            self.transactions_page.get_description_field().send_keys(description)
            self.transactions_page.get_category_dropdown_input_field().send_keys("Add. income", Keys.ENTER)

        self.transactions_page.get_amount_field().send_keys(amount)
        self.transactions_page.get_clear_button().click()

        assert self.transactions_page.get_description_field().get_attribute("value") == "", \
            "The data in the field was not cleared properly"
        assert self.transactions_page.get_category_dropdown_field().get_attribute("data-value") == "", \
            "The data in the field was not cleared properly"
        assert self.transactions_page.get_amount_field().get_attribute("value") == "", \
            "The data in the field was not cleared properly"

    @pytest.mark.parametrize("transaction_type", ["expenses", "income"],
                             ids=["Add expense transaction", "Add income transaction"])
    def test_tc13_should_add_transaction_with_date_change(self, transaction_type, valid_login_data, valid_description):
        email, password = valid_login_data
        description = valid_description
        amount = transaction_data['valid']['amount']

        if transaction_type == "expenses":
            category_name = "Products"
        else:
            category_name = "Add. income"

        self.login_page.login(email, password)

        if transaction_type == "income":
            self.transactions_page.get_income_tab().click()

        self.transactions_page.change_transaction_date("01")
        self.transactions_page.clear_transactions()
        self.transactions_page.add_new_transaction(description, category_name, amount, "not_set")
        self.transactions_page.change_transaction_date("01")

        try:
            self.transactions_page.get_transaction_descr_td(description)
        except TimeoutException:
            assert False, f"Couldn't find a web element with the description of the new {transaction_type} transaction!"
