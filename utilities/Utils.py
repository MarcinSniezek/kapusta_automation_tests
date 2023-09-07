import string
import time
import random


class Utils:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_random_email():
        timestamp = str(int(time.time() * 1000))
        email = f"new-user{timestamp}@example.com"
        return email

    @staticmethod
    def get_custom_length_email(username_length=10, domain="co.uk"):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=username_length))
        email = f"{random_string}@{domain}"
        return email

    @staticmethod
    def get_custom_length_string(length=10, charset=string.ascii_letters):
        return ''.join(random.choices(charset, k=length))

    @staticmethod
    def switch_paginator_options(prev_element, next_element, direction):
        if direction == "prev":
            prev_element.click()
        elif direction == "next":
            next_element.click()
        else:
            raise ValueError("Invalid direction provided. Available options: 'prev', 'next'")

    @staticmethod
    def convert_string_to_float(text):
        cleaned_text = text.replace(" ", "").replace(",", "")
        return float(cleaned_text)

    @staticmethod
    def assert_text_of_the_element(element, expected_text, message):
        actual_text = element.text.strip()
        expected_text = expected_text.strip()
        assert actual_text == expected_text, f"{message}\nExpected: '{expected_text}', Actual: '{actual_text}'"
