from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.Utils import Utils


class ReportsPage(BasePage):
    # Locators
    MONTH_PAGINATOR_TITLE = "(//p[contains(@class, 'Paginator_titleType__oQ9V4 Paginator_title__dN9GP')])[1]"
    T_TYPE_PAGINATOR_TITLE = "(//p[contains(@class, 'Paginator_titleType__oQ9V4 Paginator_title__dN9GP')])[2]"
    MONTH_PAGINATOR_PREV = "(//button[@aria-label='Previous'])[1]"
    MONTH_PAGINATOR_NEXT = "(//button[@aria-label='Next'])[1]"
    T_TYPE_PAGINATOR_PREV = "(//button[@aria-label='Previous'])[2]"
    T_TYPE_PAGINATOR_NEXT = "(//button[@aria-label='Next'])[2]"
    CATEGORY_IMG = "[class^='CategoriesList_image']"

    # Getters
    def get_month_paginator_title(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.MONTH_PAGINATOR_TITLE)

    def get_t_type_paginator_title(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.T_TYPE_PAGINATOR_TITLE)

    def get_month_paginator_prev(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.MONTH_PAGINATOR_PREV)

    def get_month_paginator_next(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.MONTH_PAGINATOR_NEXT)

    def get_t_type_paginator_prev(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.T_TYPE_PAGINATOR_PREV)

    def get_t_type_paginator_next(self):
        return self.wait_for_visibility_of_element(By.XPATH, self.T_TYPE_PAGINATOR_NEXT)

    def get_category_img(self):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, self.CATEGORY_IMG)

    def get_category_svg_img(self, category_name):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, f"svg[aria-label='{category_name}']")

    # Interactions with elements
    def switch_month(self, direction):
        Utils.switch_paginator_options(self.get_month_paginator_prev(), self.get_month_paginator_next(), direction)

    def switch_transaction_type(self, direction):
        Utils.switch_paginator_options(self.get_t_type_paginator_prev(), self.get_t_type_paginator_next(), direction)
