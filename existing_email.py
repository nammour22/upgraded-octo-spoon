from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Step 1: Go to the Signup Page
    driver.get("https://github.com/signup")
    
    # Step 2: Fill the Form with Existing Email
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    ).send_keys("githubparam03@gmail.com")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    ).send_keys("22164022yy")
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login"))
    ).send_keys("amamam213432")
    
    # Take a screenshot before clicking continue
    driver.save_screenshot("before_continue_click.png")
    
    # Step 3: Click the Continue Button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
    )
    continue_button.click()
    
    # Wait for error message
    time.sleep(2)  # Add a short wait to ensure the error appears
    
    # Step 4: Take Screenshot After Error Appears
    driver.save_screenshot("error_state.png")
    print("Screenshot of error saved after click.")

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("unexpected_error.png")
    print("Screenshot of unexpected error saved.")

finally:
    driver.quit()
