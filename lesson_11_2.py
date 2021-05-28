from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as ec
import time

from browser import Browser
from UIElement2 import UIElement as Element
from dropdown2 import Dropdown
from navigation_bar import NavigationBar
from actions_fixed import Actions

URL = "https://techskillacademy.net/brainbucket/index.php"

# May 27th, 2021
# student Evgeny Abdulin

def test_basic():
    """sequential testing clicking on elements"""
    browser = Browser(URL, "Firefox")
    # actions = Actions(browser)
    delay_between_pages = 1.5
    navigation_bar = NavigationBar(browser)
    # sequential clicking on all new elements
    navigation_bar.show_printers()
    time.sleep(delay_between_pages)
    navigation_bar.show_scanners()
    time.sleep(delay_between_pages)
    navigation_bar.show_webcams()
    time.sleep(delay_between_pages)
    navigation_bar.show_all_phones_and_pdas()
    time.sleep(delay_between_pages)
    navigation_bar.show_pdas()
    time.sleep(delay_between_pages)
    navigation_bar.show_phones()
    time.sleep(delay_between_pages)

    time.sleep(3)
    browser.shutdown()

# Exercise #3.1
# --Opening PC will show all PCs. If there are no PCs available, then the message
# "There are no products to list in this category." is displayed
def test_all_pc():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all PCs
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_pcs()

    # calculating number of products in PC category
    number_of_products = len(driver.find_elements_by_class_name("product-thumb"))

    if number_of_products == 0:
        print("There are no products to list in this category.")

    time.sleep(3)
    browser.shutdown()

# Exercise #3.2
# --Opening Mac will show all Macs. The number of items should match the number in the dropdown option:
def test_all_macs():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all Macs
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_mac_desktops()
    # receiving the option of the dropdown as a string
    option_text = navigation_bar._option_text
    # slicing the string to extract the number of Macs
    number_from_option = int(option_text[option_text.find("(")+1:option_text.find(")")])

    # calculating number of products in PC category
    number_of_products = len(driver.find_elements_by_class_name("product-thumb"))

    assert number_of_products == number_from_option

    time.sleep(3)
    browser.shutdown()

# Exercise #3
# --Clicking on all desktops will show available desktops
def test_all_desktops():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # showing all desktops
    navigation_bar = NavigationBar(browser)
    navigation_bar.show_all_desktops()

    time.sleep(3)
    browser.shutdown()


if __name__ == "__main__":
    test_basic()
    # test_all_pc()
    # test_all_macs()
    # test_all_desktops()