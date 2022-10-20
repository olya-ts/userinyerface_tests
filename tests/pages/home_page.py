from selenium.webdriver.common.by import By

from framework.pages.base_form import BaseForm
from framework.elements.button import Button
from framework.elements.link import Link
from framework.utils.logger import Logger


class HomePage(BaseForm):
    __search_condition = By.XPATH
    __no_bttn_loc = "//button[@class='start__button']"
    __no_bttn = Button(
        locator=(__search_condition, __no_bttn_loc),
        name="No Button"
    )
    __go_to_next_page_link = Link(
        locator=(__search_condition, "//a[@class='start__link']"),
        name="Go To The Next Page Link"
    )

    def __init__(self):
        super().__init__(locator=(HomePage.__search_condition, HomePage.__no_bttn_loc),
                         page_name=self.__class__.__name__)

    def click_go_to_next_page_link(self):
        Logger.info("Clicking on the link to go to the next page on " + self.page_name)
        self.__go_to_next_page_link.wait_for_clickable()
        self.__go_to_next_page_link.click()
