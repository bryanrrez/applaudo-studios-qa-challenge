"""Common module."""

from appium.webdriver.common.mobileby import MobileBy


class CommonPage:
    """Common class."""
    ADD_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'ADD')

    def __init__(self, driver):
        self.driver = driver

    def click_add_button(self):
        """Click ADD button."""
        element = self.driver.find_element(*self.ADD_BUTTON)
        element.click()