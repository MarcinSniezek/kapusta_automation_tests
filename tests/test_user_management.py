import pytest
from selenium.common.exceptions import TimeoutException
from data.test_data import login_data, register_data, urls


@pytest.mark.usefixtures("setup")
class TestUserManagement:
    def test_tc2_should_register_new_user_successfully(self, valid_register_data):
        email, password = valid_register_data

        self.login_page.register(email, password)
        self.login_page.wait_for_url(urls['home_page_url'])
        assert urls['home_page_url'] == self.driver.current_url, "Registration failed"

    def test_tc2_should_register_new_user_successfully_with_min_length_password(self, valid_register_email):
        self.login_page.register(valid_register_email, register_data['valid']['password_min_length'])
        self.login_page.wait_for_url(urls['home_page_url'])
        assert urls['home_page_url'] == self.driver.current_url, "Registration failed"

    def test_tc3_should_login_user_with_valid_credentials_and_check_url(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        self.login_page.wait_for_url(urls['home_page_url'])
        assert urls['home_page_url'] == self.driver.current_url, "Login failed"

    @pytest.mark.parametrize(
        "email, password", [(register_data['invalid']['short_email'], register_data['valid']['password']),
                            (register_data['invalid']['single_char_email'], register_data['valid']['password']),
                            (register_data['invalid']['long_email'], register_data['valid']['password']),
                            (register_data['invalid']['email_starts_with_hyphen'], register_data['valid']['password']),
                            (register_data['invalid']['email_ends_with_hyphen'], register_data['valid']['password'])],
        ids=["Email address must be at least 10 characters",
             "Email address username must be at least 2 characters",
             "Email address must not be more than 63 chars",
             "Email address must not start with hyphen",
             "Email address must not end with hyphen"]
    )
    def test_tc4_should_fail_registration_with_invalid_email(self, email, password):
        self.login_page.register(email, password)
        self.login_page.wait_for_url(urls['home_page_url'], 4)
        assert urls['login_page_url'] == self.driver.current_url, \
            "Registration was successful despite entering an invalid email address!"

    @pytest.mark.parametrize("email, password", [(login_data['invalid']['email'], login_data['invalid']['password'])])
    def test_tc5_should_fail_login_with_non_existing_user_data_and_check_url(self, email, password):
        self.login_page.login(email, password)
        self.login_page.wait_for_url(urls['home_page_url'], 4)
        assert urls['login_page_url'] == self.driver.current_url, \
            "Login was successful despite entering an invalid email address!"

    @pytest.mark.parametrize("email, password", [(login_data['invalid']['email'], login_data['invalid']['password'])])
    def test_tc5_should_fail_login_with_non_existing_user_data_and_display_alert(self, email, password):
        self.login_page.login(email, password)
        try:
            self.login_page.get_alert_window()
        except TimeoutException:
            assert False, "Couldn't find alert with error message!"

    def test_tc7_should_display_hello_message_after_successful_registration(self, valid_register_data):
        email, password = valid_register_data

        self.login_page.register(email, password)
        try:
            self.transactions_page.get_hello_message()
        except TimeoutException:
            assert False, "Couldn't find a window with hello message!"

    def test_tc7_should_check_hello_message_txt_after_successful_registration(self, valid_register_data):
        email, password = valid_register_data

        self.login_page.register(email, password)

        expected_txt = "Hello! To get started, enter the current balance of your account!\n" \
                       "You can't spend money until you have it :)"
        actual_txt = self.transactions_page.get_hello_message().text
        assert expected_txt == actual_txt, "Expected different hello message text!"

    def test_tc7_should_disappear_hello_message_after_balance_confirm(self, valid_register_data):
        email, password = valid_register_data

        self.login_page.register(email, password)
        self.transactions_page.set_balance(1000)
        try:
            self.transactions_page.get_hello_message()
        except TimeoutException:
            pass
        else:
            assert False, "Hello message is not disappeared!"

    def test_tc7_should_disappear_hello_message_if_not_login_first_time(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        try:
            self.transactions_page.get_hello_message()
        except TimeoutException:
            pass
        else:
            assert False, "Hello message is not disappeared!"

    def test_tc8_should_logout_user_from_account(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        self.login_page.logout()
        self.login_page.wait_for_url(urls['login_page_url'], 4)

        assert urls['login_page_url'] == self.driver.current_url, "Logout from the user account failed!"

    def test_tc8_should_close_logout_modal_with_cross(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        self.login_page.get_logout_link().click()
        self.login_page.get_modal_close_btn().click()

        try:
            self.login_page.get_modal_window()
        except TimeoutException:
            pass
        else:
            assert False, "Modal window is not disappeared!"

    def test_tc8_should_close_logout_modal_with_cancel_btn(self, valid_login_data):
        email, password = valid_login_data

        self.login_page.login(email, password)
        self.login_page.get_logout_link().click()
        self.login_page.get_modal_cancel_btn().click()

        try:
            self.login_page.get_modal_window()
        except TimeoutException:
            pass
        else:
            assert False, "Modal window is not disappeared!"
