import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://the-internet.herokuapp.com/login"


@pytest.fixture
def driver():
    """Set up and tear down WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


def login(driver, username, password):
    """Helper function to perform login action."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def get_flash_message(driver):
    """Get the flash message text from the page."""
    flash = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    return flash.text


class TestLogin:
    """Test suite for the-internet login page."""

    def test_login_success(self, driver):
        """TC-01: Verify successful login and logout."""
        driver.get(BASE_URL)
        assert "Login Page" in driver.page_source

        login(driver, "tomsmith", "SuperSecretPassword!")
        flash_text = get_flash_message(driver)
        assert "You logged into a secure area!" in flash_text

        driver.find_element(By.CSS_SELECTOR, "a.button").click()
        flash_text = get_flash_message(driver)
        assert "You logged out of the secure area!" in flash_text

    def test_login_failed_wrong_password(self, driver):
        """TC-02: Verify login fails with incorrect password."""
        driver.get(BASE_URL)
        assert "Login Page" in driver.page_source

        login(driver, "tomsmith", "Password!")
        flash_text = get_flash_message(driver)
        assert "Your password is invalid!" in flash_text

    def test_login_failed_username_not_found(self, driver):
        """TC-03: Verify login fails with non-existent username."""
        driver.get(BASE_URL)
        assert "Login Page" in driver.page_source

        login(driver, "tomholland", "Password!")
        flash_text = get_flash_message(driver)
        assert "Your username is invalid!" in flash_text
