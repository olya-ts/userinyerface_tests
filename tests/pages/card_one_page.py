from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.text_box import TextBox
from framework.elements.dropdown_list import DropDownList
from framework.elements.button import Button
from framework.elements.label import Label
from framework.utils.logger import Logger
from framework.utils.random_util import RandomUtils

from tests.config.test_data import TestData


class CardOnePage(BaseForm):
    __search_condition = By.XPATH
    __psswrd_loc = "//input[@placeholder='Choose Password']"

    __toplevel_domain_loc = "//div[text()='{name}']"

    __psswd_txtbox = TextBox(
        locator=(__search_condition, __psswrd_loc),
        name="Password TextBox"
    )

    __email_txtbox = TextBox(
        locator=(__search_condition, "//input[@placeholder='Your email']"),
        name="Email TextBox"
    )

    __domain_txtbox = TextBox(
        locator=(__search_condition, "//input[@placeholder='Domain']"),
        name="Domain TextBox"
    )

    __toplevel_domain_dropdown = DropDownList(
        locator=(__search_condition, "//div[@class='dropdown__field']"),
        name="TopLevel Domain Dropdown List"
    )

    __terms_and_conditions_checkbox = Button(
        locator=(__search_condition, "//span[contains(@class, 'checkbox__check')]"),
        name="Terms and Conditions Checkbox"
    )

    __next_bttn = Button(
        locator=(__search_condition, "//a[@class='button--secondary']"),
        name="Next Button"
    )

    __send_to_bottom_bttn = Button(
        locator=(__search_condition, "//button[contains(@class, 'help-form__send-to-bottom')]"),
        name="Send To Bottom Button"
    )

    __help_form_title = Label(
        locator=(__search_condition, "//*[@class='help-form__title']"),
        name="Help Form Title"
    )

    __not_really_bttn = Button(
        locator=(__search_condition, "//button[text()='Not really, no']"),
        name="Not Really Button"
    )

    __timer = Label(
        locator=(__search_condition, "//div[contains(@class, 'timer')]"),
        name="Timer"
    )

    toplevel_domains = Label(
        locator=(__search_condition, "//div[@class='dropdown__list-item']"),
        name="TopLevel Domains"
    )

    def __init__(self):
        super().__init__(locator=(CardOnePage.__search_condition, CardOnePage.__psswrd_loc),
                         page_name=self.__class__.__name__)

    def send_random_keys_to_psswd_txtbox(self):
        Logger.info("Clearing the password textbox on " + self.page_name)
        self.__psswd_txtbox.wait_for_clickable()
        self.__psswd_txtbox.clear_field()
        psswd_length = RandomUtils.generate_random_int(TestData.MIN_PSSWD_LENGTH, TestData.MAX_PSSWD_LENGTH)
        psswd = RandomUtils.generate_random_credentials(psswd_length,
                                                        TestData.COMMON_LETTER,
                                                        RandomUtils.generate_random_digit(),
                                                        RandomUtils.generate_random_capital_letter())
        Logger.info("Sending a valid random password " + psswd + " to the password textbox on " + self.page_name)
        self.__psswd_txtbox.send_keys(psswd)

    def send_keys_to_email_txtbox(self):
        Logger.info("Clearing the email textbox on " + self.page_name)
        self.__email_txtbox.wait_for_clickable()
        self.__email_txtbox.clear_field()
        email_length = RandomUtils.generate_random_int(TestData.MIN_EMAIL_LENGTH, TestData.MIN_EMAIL_LENGTH)
        email_name = RandomUtils.generate_random_credentials(email_length, TestData.COMMON_LETTER)
        Logger.info("Sending a valid random email " + email_name + " to the email textbox on " + self.page_name)
        self.__email_txtbox.send_keys(email_name)

    def send_keys_to_domain_txtbox(self):
        Logger.info("Clearing the domain textbox on " + self.page_name)
        self.__domain_txtbox.wait_for_clickable()
        self.__domain_txtbox.clear_field()
        domain_length = RandomUtils.generate_random_int(TestData.MIN_DOMAIN_LENGTH, TestData.MAX_DOMAIN_LENGTH)
        domain_name = RandomUtils.generate_random_credentials(domain_length)
        Logger.info("Sending a valid random domain " + domain_name + " to the domain textbox on " + self.page_name)
        self.__domain_txtbox.send_keys(domain_name)

    def click_toplevel_domain_dropdown(self):
        Logger.info("Clicking on the TopLevel Domain dropdown list on " + self.page_name)
        self.__toplevel_domain_dropdown.wait_for_clickable()
        self.__toplevel_domain_dropdown.js_click()

    def click_terms_and_conditions_checkbox(self):
        Logger.info("Clicking on the Terms and Conditions Checkbox on " + self.page_name)
        self.__terms_and_conditions_checkbox.wait_for_clickable()
        self.__terms_and_conditions_checkbox.js_click()

    def click_next_bttn(self):
        Logger.info("Clicking Next Button on " + self.page_name)
        self.__next_bttn.wait_for_clickable()
        self.__next_bttn.js_click()

    def get_toplevel_domains_list(self):
        Logger.info("Getting TopLevel Domains list on " + self.page_name)
        return self.toplevel_domains.get_list_of_elems_texts()

    def choose_toplevel_domain(self):
        Logger.info("Choosing random TopLevel Domain from the list on " + self.page_name)
        toplevel_domain_name = RandomUtils.select_random_item_from_list(self.get_toplevel_domains_list())
        toplevel_domain = Button(
            locator=(self.__search_condition, self.__toplevel_domain_loc.format(name=toplevel_domain_name)),
            name="Selected TopLevel Domain"
        )
        Logger.info("Clicking on the selected TopLevel Domain with the name " + toplevel_domain_name)
        toplevel_domain.wait_for_clickable()
        toplevel_domain.js_click()

    def close_help_form(self):
        Logger.info("Closing the Help Form on " + self.page_name)
        self.__send_to_bottom_bttn.click()

    def close_cookies_alert(self):
        Logger.info("Closing cookies alert on " + self.page_name)
        self.__not_really_bttn.wait_for_is_visible()
        self.__not_really_bttn.click()

    def check_if_help_form_visible(self):
        Logger.info("Checking if the Help Form on " + self.page_name + " is visible")
        self.__help_form_title.wait_for_invisibility()
        return self.__help_form_title.is_displayed()

    def check_if_cookies_alert_visible(self):
        Logger.info("Checking if the Cookies Alert on " + self.page_name + " is visible")
        return self.__not_really_bttn.is_displayed()

    def get_timer_value(self):
        Logger.info("Getting time from the timer on " + self.page_name)
        return self.__timer.get_text()
