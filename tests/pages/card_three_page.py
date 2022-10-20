from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm


class CardThreePage(BaseForm):
    __search_condition = By.XPATH
    __personal_details_loc = "//*[text()='Personal details']"

    def __init__(self):
        super().__init__(locator=(CardThreePage.__search_condition, CardThreePage.__personal_details_loc),
                         page_name=self.__class__.__name__)
