from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://github.com/signup")

    # Fill invalid data
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    ).send_keys("invalid_email@example")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    ).send_keys("123")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login"))
    ).send_keys("test_user")

    # Click 'Continue'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    ).click()

    # Check for validation errors
    validation_errors = driver.find_elements(By.CLASS_NAME, "flash-error")
    if validation_errors:
        driver.save_screenshot("validation_error.png")
        print("Screenshot of validation error saved!")

except Exception as e:
    print("An unexpected error occurred during account creation:", e)
    driver.save_screenshot("unexpected_error.png")
    print("Screenshot of unexpected error saved!")

finally:
    input("Press Enter to quit...")
    driver.quit()
