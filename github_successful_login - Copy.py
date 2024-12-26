from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Step 1: Open GitHub login page
    driver.get("https://github.com/login")

    # Step 2: Enter correct username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    )
    username_field.send_keys("githubparam03@gmail.com")  # Test account email

    # Step 3: Wait for password field and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password_field.send_keys("22164022yy")  # Test account password

    # Step 4: Click the "Sign In" button to submit the form
    driver.find_element(By.NAME, "commit").click()

    # Step 5: Wait for dashboard (user avatar confirms successful login)
    avatar = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.avatar-user"))
    )

    # Step 6: Take screenshot of successful login
    driver.save_screenshot("successful_login.png")
    print("Screenshot of successful login saved!")

except Exception as e:
    print("An error occurred during login:", e)

    # Check if login actually succeeded before treating it as an error
    if driver.current_url == "https://github.com/":
        driver.save_screenshot("successful_login.png")
        print("Login was successful but caused delay. Screenshot saved!")
    else:
        driver.save_screenshot("error_state.png")
        print("Screenshot of error saved!")

finally:
    input("Press Enter to quit...")
    driver.quit()
