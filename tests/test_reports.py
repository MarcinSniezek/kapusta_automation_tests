import pytest
from selenium.common.exceptions import TimeoutException
from utilities.Utils import Utils
from data.test_data import urls


@pytest.mark.usefixtures("setup")
class TestReports:
    def test_tc16_should_direct_user_to_reports_page(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        self.transactions_page.get_reports_page_link().click()
        self.transactions_page.wait_for_url(urls['reports_page_url'])

        assert urls['reports_page_url'] == self.driver.current_url, \
            "The actual URL is not the reports page URL!"

    def test_tc15_should_back_to_home_page_after_clicking_logo(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        self.transactions_page.get_reports_page_link().click()
        self.transactions_page.wait_for_url(urls['reports_page_url'])
        self.reports_page.get_home_page_link().click()
        self.login_page.wait_for_url(urls['home_page_url'])

        assert urls['home_page_url'] == self.driver.current_url, \
            "The actual URL is not the homepage URL!"

    def test_tc16_should_not_be_possible_to_switch_to_next_month(self, valid_login_data):
        email, password = valid_login_data
        current_month_name = "SEPTEMBER 2023"

        self.login_page.login(email, password)
        self.transactions_page.get_reports_page_link().click()
        self.transactions_page.wait_for_url(urls['reports_page_url'])
        self.reports_page.switch_month("next")

        Utils.assert_text_of_the_element(self.reports_page.get_month_paginator_title(), current_month_name,
                                         "Possibility of switching to the next month after the current month "
                                         "should be disabled!")

    def test_tc16_should_be_possible_to_switch_to_prev_month(self, valid_login_data):
        email, password = valid_login_data
        prev_month_name = "AUGUST 2023"

        self.login_page.login(email, password)
        self.transactions_page.get_reports_page_link().click()
        self.transactions_page.wait_for_url(urls['reports_page_url'])
        self.reports_page.switch_month("prev")

        Utils.assert_text_of_the_element(self.reports_page.get_month_paginator_title(), prev_month_name,
                                         "Should be possible to switch to the month before the current month ")

    @pytest.mark.parametrize("switch_direction", ["prev", "next"],
                             ids=["Go to the previous option", "Go to the next option"])
    def test_tc16_switch_transaction_type_and_verify_paginator_title(self, switch_direction, valid_login_data):
        email, password = valid_login_data
        expected_pag_title = "INCOME"

        self.login_page.login(email, password)
        self.transactions_page.get_reports_page_link().click()
        self.transactions_page.wait_for_url(urls['reports_page_url'])
        self.reports_page.get_category_img().click()
        self.reports_page.switch_transaction_type(switch_direction)

        Utils.assert_text_of_the_element(self.reports_page.get_t_type_paginator_title(), expected_pag_title,
                                         "Unexpected paginator title after switch")

    def test_tc16_should_display_categories_on_graph_descending_by_transactions_amount(self, valid_login_data):
        email, password = valid_login_data
        description = Utils.get_custom_length_string()

        self.login_page.login(email, password)

        try:
            self.transactions_page.clear_transactions()
        except TimeoutException:
            pass

        self.transactions_page.add_new_transaction(description, 'Transport', 10, "expense")
        self.transactions_page.add_new_transaction(description, 'Transport', 20, "expense")
        self.transactions_page.add_new_transaction(description, 'Health', 30, "expense")
        self.transactions_page.add_new_transaction(description, 'Health', 40, "expense")

        self.transactions_page.get_reports_page_link().click()
        self.reports_page.get_category_img().click()

        element1 = self.reports_page.get_category_svg_img("Health")
        element2 = self.reports_page.get_category_svg_img("Transport")

        x1 = element1.location['x']
        x2 = element2.location['x']

        assert x1 < x2, "The image of the category with a more significant transaction amount should be on the left!"
