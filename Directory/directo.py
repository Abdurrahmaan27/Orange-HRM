import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Directory:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 13)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def search_by_name(self):
        name_locator = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        dropdown1 = (By.CLASS_NAME, "oxd-autocomplete-option")
        search_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        clear_button_locator = (By.CSS_SELECTOR, "button[type='reset']")

        try:
            name_input = self.driver.find_element(name_locator)
            name_input.send_keys("pet")
            time.sleep(2)
            drop = self.driver.find_element(*dropdown1)
            for i in drop:
                if i.text == "Peter Mac Anderson":
                    i.click()
            search_button = self.driver.find_element(search_button_locator)
            search_button.click()
            time.sleep(5)

            clear_button = self.wait_for_element(clear_button_locator)
            clear_button.click()
            time.sleep(2)  # Wait for the page to reset
        except Exception as e:
            print(f"Error during name search: {e}")

        return self

    def filter_by_job_title(self, title):
        job_title_locator = (By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
        automation = (By.XPATH, "//span[text()='Automaton Tester']")
        search_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        clear_button_locator = (By.CSS_SELECTOR, "button[type='reset']")

        try:
            job_title_dropdown = self.driver.find_element(job_title_locator)
            job_title_dropdown.click()
            time.sleep(2)
            automation_tester = self.driver.find_element(automation)
            automation_tester.click()
            time.sleep(3)
            search_button = self.wait_for_element(search_button_locator)
            search_button.click()
            time.sleep(5)
            try:
                no_records_message = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='No Records Found']"))
                )
                print("Message Displayed:", no_records_message.text)  # Print the message
            except:
                print("No 'No Records Found' message displayed.")

            clear_button = self.driver.find_element(clear_button_locator)
            clear_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error during job title filtering: {e}")

        return self

    def filter_by_location(self, location):
        location_locator = (By.CSS_SELECTOR, "select[name='location']")
        search_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        clear_button_locator = (By.CSS_SELECTOR, "button[type='reset']")

        try:
            location_dropdown = self.wait_for_element(location_locator)
            location_dropdown.send_keys(location)  # Select location from dropdown
            time.sleep(2)

            search_button = self.wait_for_element(search_button_locator)
            search_button.click()
            time.sleep(5)

            clear_button = self.wait_for_element(clear_button_locator)
            clear_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error during location filtering: {e}")

        return self

    def search_by_name_and_filter(self, name, title=None, location=None):
        self.search_by_name(name)

        if title:
            self.filter_by_job_title(title)

        if location:
            self.filter_by_location(location)

        return self

