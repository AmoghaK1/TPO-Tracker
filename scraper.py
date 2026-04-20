from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import config


def start_driver():
    options = Options()

    options.add_argument("--headless=new")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver

def login(driver):
    driver.get(config.TPO_URL)

    wait = WebDriverWait(driver, 15)

    # Wait for username field to appear
    username_input = wait.until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
    )

    password_input = driver.find_element(By.XPATH, '//input[@type="password"]')

    # Enter credentials
    username_input.send_keys(config.USERNAME)
    password_input.send_keys(config.PASSWORD)

    # Click login
    login_button = driver.find_element(By.XPATH, '//button')
    login_button.click()

    # Wait for next page (dashboard)
    time.sleep(5)

    print("✅ Logged in")

def get_companies(driver):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import config

    # Go to companies page
    driver.get(config.COMPANY_PAGE)

    wait = WebDriverWait(driver, 15)

    # Wait for company titles (green bar text like IBM)
    elements = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//div[contains(@class,"v-card__title")]')
        )
    )

    companies = []

    for el in elements:
        name = el.text.strip()
        if name:
            companies.append(name)

    print("📊 Companies Found:", companies)

    return companies