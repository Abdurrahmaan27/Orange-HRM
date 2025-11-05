import time
from selenium.webdriver.common.by import By
from utility.Basepage import Basepage

class Maintenance(Basepage):
    # TO VALIDATE ADMIN
    page = (By.LINK_TEXT, "Maintenance")
    password = (By.NAME, "password")
    enter = (By.XPATH, "//button[normalize-space()='Confirm']")
    click = (By.XPATH, "(//span[@class='oxd-topbar-body-nav-tab-item'])[1]")
    click2 = (By.XPATH, "(//a[normalize-space()='Employee Records'])[1]")
    time.sleep(5)
    input = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1] ")
    clck = (By.XPATH, "(//button[normalize-space()='Search'])[1]")
    # PURGING RECORDS
    purge = (By.XPATH, "//a[normalize-space()='Candidate Records']")
    vacancy = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    payroll = (By.XPATH, "(//span[normalize-space()='Payroll Administrator'])[1]")
    pur1 = (By.XPATH, "(//button[normalize-space()='Purge All'])[1]")
    pur2 = (By.XPATH, "(//button[normalize-space()='Yes, Purge'])[1]")
    # TO ACCESS RECORDS
    record1 = (By.LINK_TEXT, "Access Records")
    record2 = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    record3 = (By.XPATH, "//div[@class='oxd-autocomplete-wrapper']//div[1]//span[1]")

    record4 = (By.XPATH, "(//button[normalize-space()='Download'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def maintenance(self):
        self.hrm_btn_click(self.page)
        time.sleep(3)
        self.hrm_send_keys(self.password, "admin123")
        time.sleep(3)
        self.hrm_btn_click(self.enter)
        time.sleep(3)
        self.hrm_btn_click(self.click)
        time.sleep(3)
        self.hrm_btn_click(self.click2)
        time.sleep(3)
        self.hrm_send_keys(self.input, "abcd")
        time.sleep(3)
        self.hrm_btn_click(self.clck)

    def purge_records(self):
        self.hrm_btn_click(self.click)
        time.sleep(3)
        self.hrm_btn_click(self.purge)
        time.sleep(3)
        self.hrm_send_keys(self.vacancy, "Payroll Administrator")
        time.sleep(3)
        self.hrm_btn_click(self.payroll)
        time.sleep(2)
        self.hrm_btn_click(self.clck)
        time.sleep(3)
        self.hrm_btn_click(self.pur1)
        time.sleep(3)
        self.hrm_btn_click(self.pur2)
        time.sleep(2)

    def access_records(self):
        self.hrm_btn_click(self.record1)
        time.sleep(3)
        self.hrm_send_keys(self.record2, "John")
        time.sleep(4)
        self.hrm_btn_click(self.record3)
        time.sleep(3)
        self.hrm_btn_click(self.clck)
        time.sleep(3)
        self.hrm_btn_click(self.record4)
        time.sleep(4)
