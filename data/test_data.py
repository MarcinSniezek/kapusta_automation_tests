import string
from utilities.Utils import Utils

urls = {
    "login_page_url": "https://kapusta-qa.netlify.app/",
    "home_page_url": "https://kapusta-qa.netlify.app/transactions/expenses",
    "reports_page_url": "https://kapusta-qa.netlify.app/reports"
}

login_data = {
    "valid": {
        "email": "new-user@example.com",
        "password": "test1234"
    },
    "invalid": {
        "email": "non-existing-user@example.com",
        "password": "unknown123"
    }
}

register_data = {
    "valid": {
        "password": "test1234",
        "password_min_length": "test123"
    },
    "invalid": {
        "short_email": Utils.get_custom_length_email(2),
        "single_char_email": Utils.get_custom_length_email(1),
        "long_email": Utils.get_custom_length_email(63),
        "email_starts_with_hyphen": f"-{Utils.get_random_email()}",
        "email_ends_with_hyphen": f"{Utils.get_random_email()}-"
    }
}

transaction_data = {
    "valid": {
        "description_length": 20,
        "amount": 100
    },
    "invalid": {
        "long_description_length": 21,
        "short_description_length": 2,
        "amount": Utils.get_custom_length_string(charset=string.ascii_letters + string.punctuation)
    }
}
