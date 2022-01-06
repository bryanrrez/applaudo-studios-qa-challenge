"""Shopping Lists module."""

from appium.webdriver.common.mobileby import MobileBy


class ShoppinListsPage:
    """Shopping Lists class."""
    NEW_LIST_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'NEW LIST')

    def __init__(self, driver):
        self.driver = driver

    def click_new_list_button(self):
        """Click NEW LIST button."""
        element = self.driver.find_element(*self.NEW_LIST_BUTTON)
        element.click()