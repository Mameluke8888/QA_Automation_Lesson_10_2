from selenium.webdriver.common.by import By
import time

from browser import Browser
from UIElement import UIElement as Element
from dropdown import Dropdown

from header import Header
from right_menu import RightMenu
from login_page import LoginPage
from registration_page import RegistrationPage

URL = "https://techskillacademy.net/brainbucket"

# May 23rd, 2021
# student Evgeny Abdulin


def test_registration_through_dropdown():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Svetlana")
    registration_form.enter_last_name("Match")
    registration_form.enter_email("svetlana.match2@gmail.com")
    registration_form.enter_telephone("3123405555")
    registration_form.enter_first_line_address("175 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("qwerty123")
    registration_form.confirm_password("qwerty123")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! ' \
                                                          'Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


def test_registration_from_right_menu():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # in Account dropdown select Login option
    header = Header(browser)
    header.open_login_page()

    # click on Register btn in the right menu
    right_menu = RightMenu(browser)
    right_menu.click_registration()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name("Svetlana")
    registration_form.enter_last_name("Match")
    registration_form.enter_email("svetlana.match2@gmail.com")
    registration_form.enter_telephone("3123405555")
    registration_form.enter_first_line_address("175 W Jackson St")
    registration_form.enter_city("Chicago")
    registration_form.select_state("Illinois")
    registration_form.enter_password("qwerty123")
    registration_form.confirm_password("qwerty123")
    registration_form.subscribe_to_newsletters()
    registration_form.agree_to_privacy_policy()

    registration_form.submit_form()

    successful_registration_title = Element(browser, By.XPATH, "//*[@id='content']/h1")
    assert successful_registration_title.get_text() == 'Your Account Has Been Created!'

    successful_registration_subtitle = Element(browser, By.XPATH, "//*[@id='content']/p")
    assert successful_registration_subtitle.get_text() == 'Congratulations! ' \
                                                          'Your new account has been successfully created!'

    time.sleep(5)
    browser.shutdown()


def test_header():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    # in Account dropdown select Login option
    header = Header(browser)
    # header.open_wishlist()
    header.search_for('laptop')
    header.change_currency("eur")

    time.sleep(3)
    browser.shutdown()


def test_login():
    browser = Browser(URL, "Firefox")
    driver = browser.get_driver()

    header = Header(browser)
    header.open_login_page()

    login_page = LoginPage(browser)
    login_page.email_input_type("svetlana.match2@gmail.com")
    login_page.password_input_type("qwerty123")
    time.sleep(1)
    login_page.login_btn.click()

    time.sleep(3)
    browser.shutdown()

if __name__ == "__main__":
    # test_registration_through_dropdown()
    # test_registration_from_right_menu()
    # test_header()
    test_login()
