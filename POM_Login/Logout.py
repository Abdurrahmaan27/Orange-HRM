import time

from selenium.webdriver.common.by import By
from utility.Basepage import Basepage


class Logout(Basepage):
    click = (By.CSS_SELECTOR, '.oxd-userdropdown-name')
    Logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.hrm_btn_click(self.click)
        self.hrm_btn_click(self.Logout)
        time.sleep(3)

