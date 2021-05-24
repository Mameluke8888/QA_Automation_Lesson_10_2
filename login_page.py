from header import Header
from right_menu import RightMenu
from UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        self.email_input = Element(browser, By.ID, "input-email")
        self.password_input = Element(browser, By.ID, "input-password")
        self.login_btn = Element(browser, By.XPATH, "//input[@value='Login']")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

    def email_input_type(self, email_text):
        self.email_input.enter_text(email_text)

    def password_input_type(self, password_text):
        self.password_input.enter_text(password_text)

    def login_btn_click(self):
        self.login_btn.wait_until_visible()
        self.login_btn.click()
