
import time

from src.pages.home import HomePage
from src.pages.shopping_lists import ShoppinListsPage
from src.pages.common import CommonPage


def test_fast_shopping(driver):
    LIST_NAME = 'my shopping list'
    ITEMS = [
        {
            'name': 'apples',
            'quantity': 4
        },
        {
            'name': 'apricots',
            'quantity': 3
        },
        {
            'name': 'bananas',
            'quantity': 6
        },
        {
            'name': 'blueberries',
            'quantity': 10
        },
        {
            'name': 'cantaloupe',
            'quantity': 2
        },
        {
            'name': 'cherries',
            'quantity': 8
        }
    ]

    home_page = HomePage(driver)
    home_page.click_no_list_selected()

    shopping_lists_page = ShoppinListsPage(driver)
    shopping_lists_page.click_new_list_button()

    # Type list name
    home_page.type_list_name(LIST_NAME)

    common_page = CommonPage(driver)
    common_page.click_add_button()

    for item in ITEMS:
        home_page.click_add_button()
        home_page.type_item_name(item['name'])
        common_page.click_add_button()

    time.sleep(10)