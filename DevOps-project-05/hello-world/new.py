import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    # Configure the WebDriver to connect to the Selenium server in the Docker container
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=webdriver.ChromeOptions())
    yield driver
    driver.quit()

def test_script(driver):
    try:
        print("Navigating to the web application...")
        driver.get("http://13.233.58.109:8086/webapp/")

        print("Finding the 'Name' input field...")
        name_input = driver.find_element(By.ID, "Name")

        print("Entering value into the 'Name' field...")
        name_input.send_keys("Your Name")

        # Print the entered name
        print("Entered Name:", name_input.get_attribute("value"))

        print("Waiting for a moment...")
        time.sleep(2)

        print("Finding the 'Mobile' input field...")
        mobile_input = driver.find_element(By.ID, "mobile")

        print("Entering value into the 'Mobile' field...")
        mobile_input.send_keys("Your Mobile Number")

        # Print the entered mobile number
        print("Entered Mobile:", mobile_input.get_attribute("value"))

        # Optional: Submit the form if there is a submit button
        # submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        # submit_button.click()

        print("Waiting for a few seconds to observe the result...")
        time.sleep(5)

        # Capture a screenshot after successful execution
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

        print("Script completed successfully!")

    except Exception as e:
        # Capture a screenshot in case of an exception
        error_screenshot_path = "error_screenshot.png"
        driver.save_screenshot(error_screenshot_path)
        print(f"Error! Screenshot saved: {error_screenshot_path}")
        raise e

# Run the script with pytest
# Use the following command in the terminal:
# pytest --html=report.html script_name.py

