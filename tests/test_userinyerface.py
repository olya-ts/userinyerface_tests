from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.urls import Urls
from tests.pages.home_page import HomePage
from tests.pages.card_one_page import CardOnePage
from tests.pages.card_two_page import CardTwoPage
from tests.pages.card_three_page import CardThreePage
from tests.config.test_data import TestData


class TestCardsPages:
    def test_card_one_and_card_two(self, create_browser):
        Logger.step("Step 1. Navigating to the home page and checking if it's open")
        Browser().set_url(Urls.TEST_STAND_URL)
        home_page = HomePage()
        assert home_page.is_opened(), "Home Page hasn't opened"

        Logger.step("Step 2. Clicking the link to go to the next page")
        home_page.click_go_to_next_page_link()
        card_one_page = CardOnePage()
        assert card_one_page.is_opened(), "Card One Page hasn't opened"

        Logger.step("Step 3. Inputting a random valid password, email, accepting the terms of use "
                    "and clicking Next button")
        card_one_page.send_random_keys_to_psswd_txtbox()
        card_one_page.send_keys_to_email_txtbox()
        card_one_page.send_keys_to_domain_txtbox()
        card_one_page.click_toplevel_domain_dropdown()
        card_one_page.choose_toplevel_domain()
        card_one_page.click_terms_and_conditions_checkbox()
        card_one_page.click_next_bttn()
        card_two_page = CardTwoPage()
        assert card_two_page.is_opened(), "Card Two Page hasn't opened"

        Logger.step("Step 4. Choosing 3 random interests, uploading an image and clicking Next button")
        card_two_page.click_unselect_all_bttn()
        interest_list = card_two_page.get_interest_list()
        card_two_page.check_interest_checkbox(interest_list)
        card_two_page.check_interest_checkbox(interest_list)
        card_two_page.check_interest_checkbox(interest_list)
        card_two_page.upload_image()
        card_two_page.click_next_bttn()
        card_three_page = CardThreePage()
        assert card_three_page.is_opened(), "Card Three Page hasn't opened"

    def test_help_form(self, create_browser):
        Logger.step("Step 1. Navigating to the home page and checking if it's open")
        Browser().set_url(Urls.TEST_STAND_URL)
        home_page = HomePage()
        assert home_page.is_opened(), "Home Page hasn't opened"

        Logger.step("Step 2. Clicking the link to go to the next page")
        home_page.click_go_to_next_page_link()
        card_one_page = CardOnePage()
        assert card_one_page.is_opened(), "Card One Page hasn't opened"

        Logger.step("Step 3. Hiding the help form")
        card_one_page.close_help_form()
        assert card_one_page.check_if_help_form_visible() is False, "The help form hasn't disappeared"

    def test_cookies_form(self, create_browser):
        Logger.step("Step 1. Navigating to the home page and checking if it's open")
        Browser().set_url(Urls.TEST_STAND_URL)
        home_page = HomePage()
        assert home_page.is_opened(), "Home Page hasn't opened"

        Logger.step("Step 2. Clicking the link to go to the next page")
        home_page.click_go_to_next_page_link()
        card_one_page = CardOnePage()
        assert card_one_page.is_opened(), "Card One Page hasn't opened"

        Logger.step("Step 3. Accepting the cookies form")
        card_one_page.close_cookies_alert()
        assert card_one_page.check_if_cookies_alert_visible() is False, "The cookies alert hasn't closed"

    def test_timer(self, create_browser):
        Logger.step("Step 1. Navigating to the home page and checking if it's open")
        Browser().set_url(Urls.TEST_STAND_URL)
        home_page = HomePage()
        assert home_page.is_opened(), "Home Page hasn't opened"

        Logger.step("Step 2. Clicking the link to go to the next page")
        home_page.click_go_to_next_page_link()
        card_one_page = CardOnePage()
        assert card_one_page.get_timer_value() == TestData.TIMER_VALUE, "The timer value isn't correct"
