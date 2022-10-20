from selenium.webdriver.common.by import By
import pyautogui

from framework.pages.base_form import BaseForm
from framework.elements.button import Button
from framework.elements.check_box import CheckBox
from framework.utils.logger import Logger
from framework.utils.random_util import RandomUtils
from tests.config.test_data import TestData
from tests.config.pyautogui import PyAutoGUI


class CardTwoPage(BaseForm):
    __search_condition = By.XPATH

    __download_image_btn_loc = "//button[contains(@class, 'align__cell')]"

    __interest_base_loc = "//label[@for='{interest}']"

    __unselect_all_bttn = Button(
        locator=(__search_condition, "//input[@id='interest_unselectall']//following::span[@class='checkbox__box']"),
        name="Unselect All Button"
    )

    __upload_bttn = Button(
        locator=(__search_condition, "//a[@class='avatar-and-interests__upload-button']"),
        name="Upload Button"
    )

    __next_bttn = Button(
        locator=(__search_condition, "//button[contains(@class, 'button--stroked')]"),
        name="Next Button"
    )

    interest_checkboxes = CheckBox(
        locator=(__search_condition,
                 "//div[@class='avatar-and-interests__interests-list']//descendant::label"),
        name="Interest Checkboxes"
    )

    def __init__(self):
        super().__init__(locator=(CardTwoPage.__search_condition, CardTwoPage.__download_image_btn_loc),
                         page_name=self.__class__.__name__)

    def click_unselect_all_bttn(self):
        Logger.info("Clicking on the Unselect All Button on " + self.page_name)
        self.__unselect_all_bttn.click()

    def click_next_bttn(self):
        Logger.info("Clicking on the Next Button on " + self.page_name)
        self.__next_bttn.wait_for_clickable()
        self.__next_bttn.click()

    def get_interest_list(self):
        Logger.info("Getting interests list on " + self.page_name)
        checkboxes_list = self.interest_checkboxes.get_list_of_attributes_values("for")
        return list(filter(lambda x: x not in TestData.CHECKBOXES_LIST_TO_EXCLUDE, checkboxes_list))

    def check_interest_checkbox(self, interest_list):
        Logger.info("Selecting the interest on " + self.page_name)
        interest_name = RandomUtils.select_random_item_from_list(interest_list)
        interest_checkbox = CheckBox(
            locator=(self.__search_condition, self.__interest_base_loc.format(interest=interest_name)),
            name="Interest Check Box"
        )
        Logger.info("Clicking on the interest with the name " + interest_name)
        interest_checkbox.click()

        Logger.info("Removing the interest with the name " + interest_name + " from the interest list")
        interest_list.remove(interest_name)

    def upload_image(self):
        Logger.info("Uploading an image on " + self.page_name)
        self.__upload_bttn.click()
        pyautogui.sleep(PyAutoGUI.SLEEP)
        pyautogui.write(TestData.IMAGE_PATH)
        pyautogui.sleep(PyAutoGUI.SLEEP)
        pyautogui.press(PyAutoGUI.ENTER)
