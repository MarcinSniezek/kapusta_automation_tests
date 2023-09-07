import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from pageObjects.login_register_page import LoginRegisterPage
from pageObjects.reports_page import ReportsPage
from pageObjects.transactions_page import TransactionsPage
from data.test_data import login_data, register_data, transaction_data
from utilities.Utils import Utils


@pytest.fixture(scope="function")
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    else:
        if browser == "ff":
            driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        elif browser == "edge":
            driver = webdriver.Edge(service=Service(executable_path=EdgeChromiumDriverManager().install()))
        else:
            driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    driver.get("https://kapusta-qa.netlify.app/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.login_page = LoginRegisterPage(driver)
    request.cls.reports_page = ReportsPage(driver)
    request.cls.transactions_page = TransactionsPage(driver)
    yield
    driver.quit()


@pytest.fixture(scope="class")
def valid_login_data():
    return login_data['valid']['email'], login_data['valid']['password']


@pytest.fixture(scope="function")
def valid_register_data():
    return Utils.get_random_email(), register_data['valid']['password']


@pytest.fixture(scope="function")
def valid_register_email():
    return Utils.get_random_email()


@pytest.fixture(scope="function")
def valid_description():
    return Utils.get_custom_length_string(transaction_data['valid']['description_length'])


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browser")
