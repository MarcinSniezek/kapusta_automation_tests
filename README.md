# kapusta_automation_tests
Automation tests for test application *"Kapu$ta. Smart Finance"*.

<br><br>

# Application data
[App URL](https://kapusta-qa.netlify.app/) <br>
[App Design](https://www.figma.com/file/m2DLMAhjLHuQOPuIdwnGAI/Kapusta?type=design&node-id=19401-155&mode=design)

<br><br>

# Manual tests documentation
[Link to Google Docs folder](https://drive.google.com/drive/folders/1T_k8YQGS61pcbfhbJL8I2zSkQ_UfrUqH?usp=drive_link)

<br><br>

# Project requirements:
* Python 3.9
* Pytest
* Selenium
* Web-driver manager

<br><br>

# User manual:

<br>

## Run tests for a single module
`pytest -v -s .\test_transactions.py`

<br>

## Run a single test from a file with many tests
`pytest -v -s -k="test_tc3_should_login_user_with_valid_credentials_and_check_url"`

<br>

## Run tests on a diferent browser (the default is Chrome)
`pytest -v -s --browser=ff .\test_reports.py` <br>
`pytest -v -s --browser=edge .\test_reports.py`

<br><br>

# Future plans
Adding the functionality of creating logs and reports from performed tests.
