"""Home Page module."""

import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.helpers.helpers import type_text


class HomePage:
    """Home Page class."""
    NO_LIST_SELECTED = (MobileBy.ACCESSIBILITY_ID, 'No list selected')
    ADD_BUTTON = (MobileBy.CLASS_NAME, 'android.widget.Button')
    ADD_NEW_SHOPPING_LIST_VIEW = (MobileBy.ACCESSIBILITY_ID, 'Add new shopping list')
    LIST_NAME_EDIT_TEXT = (MobileBy.XPATH, '//*[@text="Write shopping list name here..."]')
    ITEM_NAME_EDIT_TEXT = (MobileBy.XPATH, '//*[@text="Write item name here..."]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_no_list_selected(self):
        """Cick on No list selected."""
        element = self.driver.find_element(*self.NO_LIST_SELECTED)
        element.click()

    def type_list_name(self, list_name):
        """Type list name.

        Arguments
        ---------
        list_name : (str)
            List name.
        """
        # Wait until modal is visible
        self.wait.until(EC.visibility_of_element_located(self.ADD_NEW_SHOPPING_LIST_VIEW))

        type_text(list_name, self.driver)

    def type_item_name(self, item_name):
        """Type item name.

        Arguments
        ---------
        item_name : (str)
            Item name.
        """
        # Wait until modal is visible
        self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME_EDIT_TEXT))

        type_text(item_name, self.driver)

    def click_add_button(self):
        """Click on Add (+) button."""
        # self.wait.until(EC.visibility_of_all_elements_located(self.ADD_BUTTON))

        elements = self.driver.find_elements(*self.ADD_BUTTON)
        time.sleep(3)
        elements[1].click()