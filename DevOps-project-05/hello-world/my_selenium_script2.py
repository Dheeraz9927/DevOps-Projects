from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Configure the WebDriver to connect to the Selenium server in the Docker container
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=webdriver.ChromeOptions())

try:
    print("Navigating to the web application...")
    driver.get("http://13.233.58.109:8086/webapp/")

    print("Finding the 'Name' input field...")
    name_input = driver.find_element(By.ID, "Name")

    print("Entering value into the 'Name' field...")
    name_input.send_keys("mac")

    # Print the entered name
    print("Entered Name:", name_input.get_attribute("value"))

    print("Waiting for a moment...")
    time.sleep(2)

    print("Finding the 'Mobile' input field...")
    mobile_input = driver.find_element(By.ID, "mobile")

    print("Entering value into the 'Mobile' field...")
    mobile_input.send_keys("11111111")

    # Print the entered mobile number
    print("Entered Mobile:", mobile_input.get_attribute("value"))

    print("Waiting for a moment...")
    time.sleep(2)

   

    print("Finding the 'Email' input field...")
    email_input = driver.find_element(By.ID, "email")

    print("Entering value into the 'Email' field...")
    email_input.send_keys("demo@gmail.com")

    # Print the entered email
    print("Entered Email:", email_input.get_attribute("value"))
   
    print("Waiting for a few seconds to observe the result...")
    time.sleep(5)


    print("Finding the 'password' input field...")
    psw_input = driver.find_element(By.ID, "psw")

    print("Entering value into the 'Password' field...")
    psw_input.send_keys("123@123")

    # Print the entered psw
    print("Entered psw:", psw_input.get_attribute("value"))
   
    print("Waiting for a few seconds to observe the result...")
    time.sleep(5)
   
    print("Finding the 'Password-Repeat-Repeat' input field...") 
    # Fix the variable name and use By.CSS_SELECTOR
    Repeat_Password_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Repeat Password"]')

    print("Entering value into the 'Password-Repeat' field...")
    Repeat_Password_input.send_keys("123@123")

    # Print the entered psw-repeat
    print("Entered Repeat Password:", Repeat_Password_input.get_attribute("value"))

    print("Waiting for a few seconds to observe the result...")
    time.sleep(5)

    # Find the submit button by type attribute
    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

    # Click the 'Submit' button
    print("Clicking the 'Submit' button...")
    submit_button.click()

    print("Waiting for a few seconds to observe the result...")
    time.sleep(5)

   
    

    print("Script completed successfully!")

finally:
    print("Closing the WebDriver...")
    # Close the WebDriver
    driver.quit()
