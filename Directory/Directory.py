import time
from selenium.webdriver.common.by import By
from utility.Basepage import Basepage


class Directory(Basepage):
    # TO VALIDATE THE DIRECTORY DROPDOWN
    page = (By.LINK_TEXT, "Directory")
    drop1 = (By.XPATH, "//div[@class='--toggle']//button[@type='button']")
    searc = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    name = (By.XPATH, "//span[contains(text(),'Sania')]")
    search = (By.CSS_SELECTOR, "button[type='submit']")
    reset = (By.CSS_SELECTOR, "button[type='reset']")
    drop2 = (By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
    dropdata = (By.XPATH, "//span[normalize-space()='Chief Executive Officer']")
    drop3 = (By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[2]")
    dropdat = (By.XPATH, "//span[normalize-space()='New York Sales Office']")

    def __init__(self, driver):
        super().__init__(driver)

    # DIRECT TO DIRECTORY PAGE
    def directory(self):
        self.hrm_btn_click(self.page)
        time.sleep(3)
        self.hrm_btn_click(self.drop1)
        time.sleep(1)
        self.hrm_btn_click(self.drop1)

    # VALIDATE EMPLOYEE DETAILS
    def search_employee_by_name(self):
        self.hrm_send_keys(self.searc, "Sania")
        time.sleep(3)
        self.hrm_btn_click(self.name)
        time.sleep(2)
        self.hrm_btn_click(self.search)
        time.sleep(4)
        self.hrm_btn_click(self.reset)
        time.sleep(3)

    # VALIDATE JOB TITLE FILTER
    def job_title_filter(self):
        self.hrm_btn_click(self.drop2)
        time.sleep(3)
        self.hrm_btn_click(self.dropdata)
        time.sleep(3)
        self.hrm_btn_click(self.search)
        time.sleep(4)
        self.hrm_btn_click(self.reset)
        time.sleep(3)

    # VALIDATE LOCATION FILTER
    def location_filter(self):
        self.hrm_btn_click(self.drop3)
        time.sleep(3)
        self.hrm_btn_click(self.dropdat)
        time.sleep(3)
        self.hrm_btn_click(self.search)
        time.sleep(4)
        self.hrm_btn_click(self.reset)
        time.sleep(3)
