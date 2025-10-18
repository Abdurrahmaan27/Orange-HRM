#OrangeHRM Selenium Automation (Python - POM Framework)

This repository contains an automated test suite for the **OrangeHRM Demo Website**  
👉 [https://opensource-demo.orangehrmlive.com/](https://opensource-demo.orangehrmlive.com/)  

The project follows the **Page Object Model (POM)** design pattern using **Selenium WebDriver**, **Pytest**, and **Python** to ensure scalability, readability, and 
maintainability of test scripts.


#Project Structure


## Tech Stack

- **Language:** Python  
- **Testing Framework:** Pytest  
- **Automation Tool:** Selenium WebDriver  
- **Browser Driver Management:** WebDriver Manager  
- **Design Pattern:** Page Object Model (POM)  
- **Environment Management:** dotenv  

---

## Prerequisites

Make sure you have the following installed on your system:

- [Python 3.9+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/)
- pip (Python package manager)

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/<Abdurrahmaan27>/OrangeHRM-Automation.git
   cd OrangeHRM-Automation

2. **Create a virtual environment** (recommended)
   python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

3. **Install dependencies**
pip install -r requirements.txt

Run a specific test file (example: login.py):
pytest testCases/login.py -v

To view browser actions while debugging (headed mode):
pytest --headed -v


**Framework Workflow**

1.**BasePage**
Contains reusable Selenium methods (click, send_keys, get_title, etc.).
All page classes inherit from it.

2.**Page Classes (POM)**
Each page (e.g., Login, Maintenance) has its own class with web locators and page-specific actions.

3.**Test Cases**
Call the respective page class and methods to perform actions and assertions.

from testCases.login import Login

def test_valid_login(setup):
    login = Login(setup)
    login.login("Admin", "admin123")
    assert "Dashboard" in login.get_title("OrangeHRM")
